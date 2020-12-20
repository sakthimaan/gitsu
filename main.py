import os
import yaml
import user_input
from parsesshconfig import parseSSHConfig
from os import listdir
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def select(config_file):
    profileList, profile_dict = readConfig(config_file)
    result = user_input.get_choice("Select git account", profileList)
    try:
        os.system(f"git config --global user.name \"{profile_dict[result]['user.name']}\"")
        os.system(
            f"git config --global user.email \"{profile_dict[result]['user.email']}\""
        )
        ssh_key = profile_dict[result]["user.ssh"]
        if ssh_key:
            parseSSHConfig(ssh_key)
    except Exception as e:
        print("Error in setting Git config values", e)


def create(config_file):
    ssh_keys = listdir(os.path.expanduser("~/.ssh/"))
    print(ssh_keys)
    input()
    user_input.screen_clear()
    _, profile_dict = readConfig(config_file)
    profile_name = input("Enter profile name")
    user_input.screen_clear()
    profile_dict[profile_name] = {}
    profile_dict[profile_name]["user.name"] = input("\nEnter git username:\t")
    user_input.screen_clear()
    profile_dict[profile_name]["user.email"] = input("\nEnter git Email:\t")
    user_input.screen_clear()
    profile_dict[profile_name]["user.ssh"] = prompt('Enter git ssh key: ', completer=WordCompleter(ssh_keys))
    user_input.screen_clear()
    writeConfig(config_file, profile_dict)

def Delete(config_file):
    profile_list, profile_dict = readConfig(config_file)
    toDelete = user_input.get_choice("Profile to Delete", profile_list)
    print(toDelete)
    del profile_dict[toDelete]
    writeConfig(config_file,profile_dict)


def writeConfig(config_file, profile_dict):
    with open(config_file, "w+") as file:
        yaml.dump(profile_dict, file)
        file.close()


def readConfig(config_file):
    profileList = []
    if os.path.exists(config_file):
        with open(config_file) as file:
            profile_dict = yaml.load(file, Loader=yaml.FullLoader)
            file.close()
    for key in profile_dict:
        profileList.append(key)
    return profileList, profile_dict


if __name__ == "__main__":
    os.system("clear")
    config_file = os.path.expanduser("~/.config/gitsu-py/config.yml")
    os.makedirs(os.path.dirname(config_file), exist_ok=True)
    choices = ["Select", "Create", "Update", "Delete"]
    crud = user_input.get_choice("User Choice", choices)
    print(crud)
    if crud == "Select":
        select(config_file)
    if crud == "Create":
        create(config_file)
    if crud == "Delete":
        Delete(config_file)

import os
import yaml
import user_input
from parsesshconfig import parseSSHConfig
from os import listdir
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def select(config_file):
    user_list = {}
    gitsu_list = []
    if os.path.exists(config_file):
        with open(config_file) as file:
            user_list = yaml.load(file, Loader=yaml.FullLoader)
        print(type(user_list))
    for key in user_list:
        gitsu_list.append(key)
    result = user_input.get_choice("Select git account", gitsu_list)
    try:
        os.system(f"git config --global user.name \"{user_list[result]['user.name']}\"")
        os.system(
            f"git config --global user.email \"{user_list[result]['user.email']}\""
        )
        ssh_key = user_list[result]["user.ssh"]
        if ssh_key:
            parseSSHConfig(ssh_key)
    except Exception as e:
        print("Error in setting Git config values", e)


def create(config_file):
    ssh_keys = listdir(os.path.expanduser("~/.ssh/"))
    print(ssh_keys)
    input()
    user_input.screen_clear()
    profile_dict = {}
    if os.path.exists(config_file):
        with open(config_file) as file:
            profile_dict = yaml.full_load(file)
            file.close()
    profile_name = input("Enter profile name")
    user_input.screen_clear()
    profile_dict[profile_name] = {}
    profile_dict[profile_name]["user.name"] = input("\nEnter git username:\t")
    user_input.screen_clear()
    profile_dict[profile_name]["user.email"] = input("\nEnter git Email:\t")
    user_input.screen_clear()
    profile_dict[profile_name]["user.ssh"] = prompt('Enter git ssh key: ', completer=WordCompleter(ssh_keys))
    #profile_dict[profile_name]["user.ssh"] = input("\nEnter git ssh key:\t")
    user_input.screen_clear()
    print(profile_dict)
    with open(config_file, "w+") as file:
        yaml.dump(profile_dict, file)
        file.close()


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

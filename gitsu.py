from os import system, makedirs, listdir
from os.path import expanduser, dirname, exists
import yaml
import user_input
from parsesshconfig import parseSSHConfig
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory


def select(config_file):
    profileList, _ = readConfig(config_file)
    profile_name = user_input.get_choice("Select git account", profileList)
    applyProfile(config_file, profile_name)


def applyProfile(config_file, profile_name):
    _, profile_dict = readConfig(config_file)
    gitUser = profile_dict[profile_name]['user.name']
    gitEmail = profile_dict[profile_name]['user.email']
    ssh_key = profile_dict[profile_name]["user.ssh"]
    try:
        system(f"git config --global user.name \"{gitUser}\"")
        system(
            f"git config --global user.email \"{gitEmail}\""
        )
        if ssh_key:
            parseSSHConfig(ssh_key)
        user_input.screen_clear()
        print(f"👍 Profile {profile_name} has been applied. ")
        print(40 * "-")
        print(f"Git:\n\t{gitUser}\n\t{gitEmail}\nssh:\n\t{ssh_key}")
    except Exception as e:
        print("😞 Error in setting Git config values", e)


def create(config_file):
    session = PromptSession()
    ssh_keys = listdir(expanduser("~/.ssh/"))
    _, profile_dict = readConfig(config_file)
    user_input.screen_clear()
    profile_name = session.prompt('Enter Profile name: ', auto_suggest=AutoSuggestFromHistory())
    profile_dict[profile_name] = {}
    profile_dict[profile_name]["user.name"] = session.prompt('    Enter git username: ',
                                                             auto_suggest=AutoSuggestFromHistory())
    profile_dict[profile_name]["user.email"] = session.prompt('    Enter git email: ',
                                                              auto_suggest=AutoSuggestFromHistory())
    profile_dict[profile_name]["user.ssh"] = prompt('    Enter git ssh key: ', completer=WordCompleter(ssh_keys))
    try:
        writeConfig(config_file, profile_dict)
        toApply = input(f"Profile {profile_name} created. Do you want to apply y/[n]:")
        if "n" in toApply.lower() or not toApply:
            print(f"😈Profile {profile_name} is created, but not applied ")
        if "y" in toApply.lower():
            applyProfile(config_file, profile_name)
    except Exception as e:
        print("😞 Error in updating the config and key", e)


def Delete(config_file):
    profile_list, profile_dict = readConfig(config_file)
    profile_name = user_input.get_choice("Profile to Delete", profile_list)
    del profile_dict[profile_name]
    try:
        writeConfig(config_file, profile_dict)
        print(f"🗑️ Profile {profile_name} has been deleted from config file")
    except Exception as e:
        print("😞 Error in Deleting profile form config file", e)


def writeConfig(config_file, profile_dict):
    with open(config_file, "w+") as file:
        yaml.dump(profile_dict, file)
        file.close()


def readConfig(config_file):
    profileList = []
    profile_dict = {}
    if exists(config_file):
        with open(config_file) as file:
            profile_dict = yaml.load(file, Loader=yaml.FullLoader)
            file.close()
    try:
        for key in profile_dict:
            profileList.append(key)
    except TypeError as e:
        profile_dict = {}
    return profileList, profile_dict


if __name__ == "__main__":
    system("clear")
    config_file = expanduser("~/.config/gitsu-py/config.yml")
    makedirs(dirname(config_file), exist_ok=True)
    choices = ["Select", "Create", "Update", "Delete"]
    crud = user_input.get_choice("User Choice", choices)
    print(crud)
    if crud == "Select":
        select(config_file)
    if crud == "Create":
        create(config_file)
    if crud == "Delete":
        Delete(config_file)

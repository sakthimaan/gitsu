import os
import yaml
import user_input
from parsesshconfig import parseSSHConfig


def select(configfile):
    user_list = {}
    gitsu_list = []
    os.system("clear")
    os.makedirs(os.path.dirname(configfile), exist_ok=True)
    if os.path.exists(configfile):
        with open(configfile) as file:
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
        ssh_key = user_list[result]["ssh.key"]
        if ssh_key:
            parseSSHConfig(ssh_key)
    except Exception as e:
        print("Error in setting Git config values", e)

def create(config_file):
    user_input.screen_clear()
    profile_dict = {}
    profile_name = input("Enter profile name")
    user_input.screen_clear()
    profile_dict[profile_name] ={}
    profile_dict[profile_name]["user.name"] = input("\nEnter git username:\t")
    user_input.screen_clear()
    profile_dict[profile_name]["user.email"] = input("\nEnter git Email:\t")
    user_input.screen_clear()
    profile_dict[profile_name]["user.ssh"] = input("\nEnter git ssh key:\t")
    user_input.screen_clear()
    print(profile_dict)
    # with open(config_file) as file:
    #     profile_list = yaml.full_load(file)
    #     file.close()

if __name__ == "__main__":
    os.system("clear")
    config_file = os.path.expanduser("~/.config/gitsu-py/gitsu.yml")
    choices = ["Select", "Create", "Update", "Delete"]
    crud = user_input.get_choice("User Choice", choices)
    print(crud)
    if crud == "Select":
         select(config_file)
    if crud == "Create":
        create(config_file)

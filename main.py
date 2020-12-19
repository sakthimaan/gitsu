import os
import yaml
import user_input
import sshconf
from  



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
    result = user_input.get_choice(gitsu_list)
    try:
        os.system(f"git config --global user.name \"{user_list[result]['user.name']}\"")
        os.system(
            f"git config --global user.email \"{user_list[result]['user.email']}\""
        )
        ssh_key = user_list[result]["ssh.key"]
        print(ssh_key)
        if ssh_key:
            conf = sshconf.read_ssh_config(os.path.expanduser(f"~/.ssh/{ssh_key}"))
            print(conf.config())

    except Exception as e:
        print("Error in setting Git config values", e)


if __name__ == "__main__":
    os.system("clear")
    config_file = os.path.expanduser("~/.config/gitsu-py/gitsu.yml")
    choices = ["Select", "Create", "Update", "Delete"]
    crud = user_input.get_choice(choices)
    if crud == "Select":
        select(config_file)

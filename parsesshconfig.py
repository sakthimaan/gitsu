import os
import re

def parseSSHConfig(ssh_key_file_name):
    ssh_config_file = os.path.expanduser("~/.ssh/config")
    git_ssh_config = f'\
Host github.com\n\
    User git\n\
    Hostname github.com\n\
    IdentityFile {os.path.expanduser(f"~/.ssh/{ssh_key_file_name}")}\n'
    line_count = 1
    start_line = 0
    end_line = 0
    git_content = []
    if not os.path.exists(ssh_config_file):
        print("~/.ssh/config file not found. Please create a profile to continue")
        exit(0)
    with open(file=ssh_config_file, mode="r") as file:
        content = file.readlines()
        file.close()
        for line in content:
            if "Host " in line or line_count == len(content):
                if start_line != 0:
                    end_line = line_count - 1
                if re.match(r"^Host[\s]+github.com$", line):
                    start_line = line_count
            line_count += 1

    if start_line == 0 or end_line == 0:
        print("github.com host not found in ~/.ssh/config file.\n\
               Please create a profile to continue.")
        exit(0)
    for line in git_ssh_config.splitlines():
        git_content.append(line + "\n")
    del content[start_line - 1: end_line]
    content[start_line - 1: start_line - 1] = git_content
    for line in content:
        print(line, end="")
    with open(ssh_config_file, 'w+') as file:
        for line in content:
            file.write(line)
        file.close()

import os
import re
from paramiko import SSHConfig

ssh_config_file = os.path.expanduser("~/.ssh/config")
line_count = 1
start_line = 0
end_line = 0
git_content = []
with open(file=ssh_config_file, mode="r") as file:
    content = file.readlines()
    for line in content:
        if "Host " in line:
            if start_line != 0:
                end_line = line_count - 1
            if re.match(r"^Host[\s]+github.com$", line):
                start_line = line_count
        line_count += 1
    for i in range(start_line - 1, end_line):
        # print(content[i], end="")
        git_content.append(content[i])

del content[start_line - 1 : end_line]
content[start_line - 1 : start_line - 1] = git_content

for line in git_content:
    if line:
        print(line, end="")
print(">>>>>>>>>>>>>>>>>>>>>>>>")

for line in content:
    print(line, end="")

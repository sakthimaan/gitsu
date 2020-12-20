# gitsu
Git user management written in python, powered by prompt_toolkit.


This script will store config in ~/.config/gitsu-py/config.yml and update the `~/.gitconfig` and `~/.ssh/config` file based on the config file.

<p align="center">
  <img src="https://raw.githubusercontent.com/sakthimaan/gitsu/main/examples/demo.svg">
</p>

*Example config file:*

```yaml
personal:
  user.name: personal.name
  user.email: personal.account@gmail.com
  user.ssh: id_ed25519_personal
official:
  user.name: official.name
  user.email: official.account@mycompany.com
  user.ssh: id_ed25519_official
```

Installation steps:
```bash
git clone git@github.com:sakthimaan/gitsu.git
cd gitsu
pip3 install -r requirements.txt
./gitsu
```

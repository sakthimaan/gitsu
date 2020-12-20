# gitsu
Git user management written in python. 
This script will store config in ~/.config/gitsu-py/config.yml and update the `~/.gitconfig` and `~/.ssh/config` file based on the config file.


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

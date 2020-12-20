from bullet import Bullet
from os import name
from os import system


def get_choice(prompt, choices):
    screen_clear()
    cli = Bullet(
        prompt=f"\n{prompt}: ",
        choices=choices,
        indent=0,
        align=5,
        margin=2,
        shift=0,
        bullet="🡆",
        pad_right=5,
        return_index=False
    )

    return cli.launch()


# The screen clear function
def screen_clear():
    if name == 'posix':
        _ = system('clear')
    else:
        _ = system('cls')

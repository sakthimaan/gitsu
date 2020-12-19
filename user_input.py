from bullet import Bullet
from bullet import colors


def get_choice(choices):
    cli = Bullet(
        prompt="\nPlease choose a fruit: ",
        choices=choices,
        indent=0,
        align=5,
        margin=2,
        bullet="➤",
        bullet_color=colors.bright(colors.foreground["cyan"]),
        word_color=colors.bright(colors.foreground["yellow"]),
        word_on_switch=colors.bright(colors.foreground["yellow"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["black"],
        pad_right=5,
    )
    return cli.launch()


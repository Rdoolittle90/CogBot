from colorama import Fore, Style
from os import getenv

color_map = {
    "DEBUG": {
        "color": Fore.BLUE,
        "int": 4
        },
    "TASK": {
        "color": Fore.LIGHTGREEN_EX,
        "int": 3
        },
    "INFO": {
        "color": Fore.GREEN,
        "int": 3
        },
    "COMMAND": {
        "color": Fore.GREEN,
        "int": 3
        },
    "CONN":  {
        "color": Fore.MAGENTA,
        "int": 3
        },
    "GUILD":  {
        "color": Fore.CYAN,
        "int": 3
        },
    "COG":  {
        "color": Fore.CYAN,
        "int": 2
        },
    "FAIL": {
        "color": Fore.YELLOW,
        "int": 2
        },
    "WARNING": {
        "color": Fore.YELLOW + Style.BRIGHT,
        "int": 2
        },
    "ERROR":  {
        "color": Fore.RED,
        "int": 1
        },
    "CRITICAL":  {
        "color": Fore.RED + Style.BRIGHT,
        "int": 0
        },
    }

def colorized_print(print_type: str, message: str) -> None:
    """
    Helper function to colorize log output based on level.
    """
    debug_level = int(getenv("APP_LOGGING_LEVEL"))
    if color_map[print_type]["int"] <= debug_level:
        format = f'{color_map[print_type]["color"]}[{print_type}] {message}{Style.RESET_ALL}'
        print(format)
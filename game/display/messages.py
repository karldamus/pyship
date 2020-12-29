# Pyship ©2020 Karl Damus, All Rights Reserved
# messages.py

from rich import print
from rich.console import Console

console = Console()

def error_message(message):
    console.print("\n  " + str(message), style="bold red")

def confirmation_message(message):
    console.print("\n  " + str(message), style="bold green")
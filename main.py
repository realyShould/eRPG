from colorama import Fore, Back, Style
import colorama, os, random
import lists_and_functions as f

colorama.init()


print(f'{Fore.YELLOW}\t\t█▀▀█ █▀▀█ █▀▀█\n\t\t█▄▄▀ █░░█ █░░▄▄\n\t\t▀░▀▀ █▀▀▀ █▄▄█')

f.userCommand(f.player, f.wolf, f.bear)
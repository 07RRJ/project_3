from os import system
from msvcrt import getwch       
from colors import bcolors
from random import randint
from sys import exit
import functions

system('cls')       # clear the screen

def game_banner():      # header
    print(" " * 7, "=" * 27)
    print(" " * 7, "===", bcolors.RED + "ROCK", bcolors.BLUE + "PAPER", bcolors.GREEN + "SCISSORS", bcolors.DEFAULT + "===")
    print(" " * 7, "=" * 27, "\n")

def game_instructions():        # shows poossible key imputs (menu)
    system("cls")
    game_banner()
    print(f"Choose one of the options below:\n{bcolors.RED}* r/1 - rock\n{bcolors.BLUE}* p/2 - paper\n{bcolors.GREEN}* s/3 - scissors\n{bcolors.DEFAULT}* z/0 - restart\n* q - quit\n")

def set_score():        # game variables in a function (makes it possible to reset in a neat way)
    global stats
    stats = {
        "wins": 0,
        "losses": 0,
        "draws": 0,
        "rounds": 0,
        "result": "no_matches_fought"
}

set_score()     # on game start reset the score

input_options = ["r", "p", "s", "q", "z", "1", "2", "3"]        # usable things

game_instructions()
while True:     # main loop
    print(f"What do you chose? {bcolors.RED}\"R\"ock {bcolors.BLUE}\"P\"aper {bcolors.GREEN}\"S\"cissors{bcolors.DEFAULT}?")
    your_choice = getwch().lower()
    system("cls")
    game_banner()

    if your_choice in input_options:        # checks for valid input
        if your_choice == "q":      # if you press q, quit with an msg
            system("cls")
            exit("you quit")

        elif your_choice == "z":            # restart
            game_instructions()
            set_score()

        else:
            if your_choice == "r" or your_choice == "1":        # changes your input to the correct display 🪨📄✂️ to understand better
                your_display = "🪨"
                your_display_name = f"{bcolors.RED}rock{bcolors.DEFAULT}"
            elif your_choice == "p" or your_choice == "2":
                your_display = "📄"
                your_display_name = f"{bcolors.BLUE}paper{bcolors.DEFAULT}"
            elif your_choice == "s" or your_choice == "3":
                your_display = "✂️"
                your_display_name = f"{bcolors.GREEN}scissors{bcolors.DEFAULT}"

            ai_choice = randint(1, 3) # ai_choice to understandable value 1 = rock, 2 = paper, 3 = scissors
            if ai_choice == 1:
                ai_display = "🪨"
                ai_display_name = f"{bcolors.RED}rock{bcolors.DEFAULT}"
            elif ai_choice == 2:
                ai_display = "📄"
                ai_display_name = f"{bcolors.BLUE}paper{bcolors.DEFAULT}"
            elif ai_choice == 3:
                ai_display = "✂️"
                ai_display_name = f"{bcolors.GREEN}scissors{bcolors.DEFAULT}"

            print(f"{your_display}  vs {ai_display}")       # display emoji vs
            print(f"{your_display_name} vs {ai_display_name}")      # text representation of vs for better understanding

            functions.draw_win_lose(stats, your_display, ai_display)        # sends to "functions.py" to see the result

            stats["rounds"] += 1
            # v print the result
            print(f"{stats['result']}\n\n{bcolors.GREEN}wins{bcolors.DEFAULT} {stats['wins']}, {bcolors.RED}losses{bcolors.DEFAULT} {stats['losses']}, {bcolors.YELLOW}draws{bcolors.DEFAULT} {stats['draws']}, rounds {stats['rounds']}\n")
    else:
        game_instructions()     # if your input isnt in "input_options" display valid inputs aka the menu
        print(f"{bcolors.GREEN}wins{bcolors.DEFAULT} {stats['wins']}, {bcolors.RED}losses{bcolors.DEFAULT} {stats['losses']}, {bcolors.YELLOW}draws{bcolors.DEFAULT} {stats['draws']}, rounds {stats['rounds']}\n")
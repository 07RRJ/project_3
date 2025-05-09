from colors import bcolors

def draw_win_lose(stats, your_display, ai_display):         # takes input from "index.py" to check results
    if your_display == ai_display:          # draw
        stats["draws"] += 1
        stats["result"] = bcolors.YELLOW+"DRAW"+bcolors.DEFAULT
    
    elif your_display == "🪨" and ai_display == "✂️":           # when you won
        stats["wins"] += 1
        stats["result"] = bcolors.GREEN+"you WON"+bcolors.DEFAULT

    elif your_display == "📄" and ai_display == "🪨":           # when you won
        stats["wins"] += 1
        stats["result"] = bcolors.GREEN+"you WON"+bcolors.DEFAULT

    elif your_display == "✂️" and ai_display == "📄":           # when you won
        stats["wins"] += 1
        stats["result"] = bcolors.GREEN+"you WON"+bcolors.DEFAULT

    else:           # when you lose
        stats["losses"] += 1
        stats["result"] = bcolors.RED+"you LOSE"+bcolors.DEFAULT

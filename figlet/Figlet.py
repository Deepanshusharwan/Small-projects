from pyfiglet import Figlet
import random
import sys

def main():
    figlet = Figlet()
    font_list = figlet.getFonts()

    if len(sys.argv) == 1:
        text = input("Input: ")
        figlet.setFont(font = random.choice(font_list))
        print('Output:')
        print(figlet.renderText(text))

    elif sys.argv[1] == '-f' or sys.argv[1] == "--font":
        text = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        print("Output:")
        print(figlet.renderText(text))

    else:
        sys.exit('error')

main()

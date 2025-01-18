import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    font_list = figlet.getFonts()

    if len(sys.argv) == 1:
        text = input("Input: ")
        font_used = random.choice(font_list)
        figlet.setFont(font = font_used)
        print('Output:')
        print(figlet.renderText(text))

    elif sys.argv[1] == '-f' or sys.argv[1] == "--font":
        text = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        print("Output:")
        print(figlet.renderText(text))

    else:
        sys.exit('error')

if __name__ == "__main__":
    main()

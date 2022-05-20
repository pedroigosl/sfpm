from termcolor import colored
import requests
import time


def main():
    url = "https://www.google.com"
    timeout = 5
    LINE_CLEAR = '\x1b[2K' # <-- ANSI sequence

    toggle = True
    start = time.time()
    while(True):
        print(end=LINE_CLEAR) # <-- clear the line where cursor is located
        try:
            end = time.time()
            if not toggle:
                start = time.time()
            request = requests.get(url, timeout=timeout)
            print(colored(f"connected - {end - start}", "green"),end = "\r")
            toggle = True
        except (requests.ConnectionError,requests.Timeout) as exception:
            print(colored("not connected", "red"),end = "\r")
            toggle = False
            
if __name__ == '__main__':
    main()
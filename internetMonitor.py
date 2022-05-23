from termcolor import colored
import cv2
import requests
import time
import datetime


def startMonitor(img_show=False, timeout=5, url="https://www.google.com"):
    LINE_CLEAR = '\x1b[2K'  # <-- ANSI sequence

    if img_show:
        img1 = cv2.imread("img_connected.png", 1)
        img1 = cv2. resize(img1, (540, 540))
        img2 = cv2.imread("img_disconnected.png", 1)
        img2 = cv2. resize(img2, (540, 540))

    toggle = True
    start = time.time()
    while(True):
        print(end=LINE_CLEAR)  # <-- clear the line where cursor is located
        try:
            request = requests.get(url, timeout=timeout)

            end = time.time()
            if not toggle:
                start = time.time()
            toggle = True

            diff = datetime.timedelta(seconds=(end-start))
            print(colored(f"connected - {str(diff)}", "green"), end="\r")

            if img_show:
                cv2.imshow('status', img1)
                cv2.setWindowTitle('status', str(diff))
        except (requests.ConnectionError, requests.Timeout) as exception:
            print(colored("not connected", "red"), end="\r")
            toggle = False

            if img_show:
                cv2.imshow('status', img2)
                cv2.setWindowTitle('status', 'DISCONNECTED!!')

        if cv2.waitKey(1) == 27:
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    startMonitor(img_show=True)

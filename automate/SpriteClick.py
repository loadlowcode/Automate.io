import pyautogui
import time
import json

import DOM

d = DOM


def spriteClick(images):
    for action in images:
        # Use Json file to destruct this
        k = action["type"]
        v = action["value"]
        time.sleep(1.5)

        if k == "click":
            x, y = pyautogui.locateCenterOnScreen(v, confidence=0.8)
            pyautogui.click(x / 2, y / 2)  # divide by 2 for Mac screen resolution
        elif k == "write":
            exec(v)


def main():
    url = "https://noodlemagazine.com/new-video"
    browse = "safari"
    d.launch(browse, url)

    spriteClick(json.load(open("./sprite/NoodleMag/nodmag.json")))


main()

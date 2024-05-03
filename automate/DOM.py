import pyautogui
import time


def launch(browser, url):
    time.sleep(3)
    pyautogui.hotkey('command', 'space', interval=0.3)
    pyautogui.typewrite(browser)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('command', 'T', interval=0.3)

    # Open URL
    pyautogui.hotkey('command', 'l')
    pyautogui.typewrite(url)
    pyautogui.press('enter')


def script(scripts, interval=3):
    # This function types the script into the address bar and presses Enter to execute it
    for script in scripts:
        time.sleep(interval)
        pyautogui.hotkey('command', 'l')
        pyautogui.typewrite('javascript:(()=>{' + script + '})();')
        pyautogui.press('enter')


def main():
    launch('chrome', 'https://noodlemagazine.com/new-video')
    js = [
        "document.querySelector('.s_text').value = 'nina elle';",
        "document.querySelector('.s_btn').click();",
        "document.querySelector('#list_videos > div:nth-child(7) > a > div.i_info > div').click();",
        "document.querySelector('#iplayer').src += '&autoplay=1';",
    ]

    js2 = js[:]
    js2[2] = "document.querySelector('#list_videos > div:nth-child(9) > a > div.i_info > div').click();"

    script(js2)

import pyautogui
from datetime import datetime
import time

screenshot_path = f'screenshots/{datetime.now()}.png'

for x in range(0,100):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(screenshot_path)
    time.sleep(5)
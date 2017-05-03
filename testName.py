import pyautogui
import time
pyautogui.click(300, 400)
pyautogui.hotkey('ctrl', 'f')
time.sleep(.200)
pyautogui.typewrite('email')
time.sleep(.200)
pyautogui.locateOnScreen('mail.png')

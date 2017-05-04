import pyautogui
import time

#clicks on the browser part of the screen

pyautogui.click(300, 400)

#tries to find the "Name" field

pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite('name')

#finds the "Name" field and clicks on 60 horizontal units on the right and 60 vertical units below it; enters name

if pyautogui.locateOnScreen('name.png')!=None:
    namex = pyautogui.locateOnScreen('name.png')[0] + 60
    namey = pyautogui.locateOnScreen('name.png')[1]+ 60
    time.sleep(1)
    pyautogui.click(namex, namey)
    time.sleep(1)
    pyautogui.typewrite('Pratyush Ranjan Tiwari')
    print "Name field filled"
else:
    print "Name field not found"

time.sleep(1)
pyautogui.click(300, 400)
#tries to find the "Email" field
time.sleep(1)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite('email')
time.sleep(1)
#finds the "email" field and clicks on 60 horizontal units on the right and 60 vertical units below it; enters name

if pyautogui.locateOnScreen('email.png')!=None:
    mailx = pyautogui.locateOnScreen('email.png')[0] + 60
    maily = pyautogui.locateOnScreen('email.png')[1]+ 60
    time.sleep(1)
  

    pyautogui.click(mailx, maily)
    time.sleep(1)
    pyautogui.typewrite('pratyushtiwari224@gmail.com')
    print "Email field filled"
else:
    print "Email field not found"

time.sleep(1)
pyautogui.click(300, 400)
#tries to find the "Email" field
time.sleep(1)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite('application id')
time.sleep(1)
#finds the "email" field and clicks on 60 horizontal units on the right and 60 vertical units below it; enters name

if pyautogui.locateOnScreen('aid.png')!=None:
    aidx = pyautogui.locateOnScreen('aid.png')[0] + 60
    aidy = pyautogui.locateOnScreen('aid.png')[1]+ 60
    time.sleep(1)
  

    pyautogui.click(aidx, aidy)
    time.sleep(1)
    pyautogui.typewrite('102016')
    print "Application ID field filled"
else:
    print "Application ID field not found"




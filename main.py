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
    print namex, namey

    pyautogui.click(namex, namey)
    time.sleep(.200)
    pyautogui.typewrite('Pratyush Ranjan Tiwari')
    print "Name field filled"
else:
    print "Name field not found"


pyautogui.click(300, 400)
#tries to find the "Email" field

pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite('email')

#finds the "email" field and clicks on 60 horizontal units on the right and 60 vertical units below it; enters name

if pyautogui.locateOnScreen('mail.png')!=None:
    mailx = pyautogui.locateOnScreen('mail.png')[0] + 60
    maily = pyautogui.locateOnScreen('mail.png')[1]+ 60
    time.sleep(.200)
  

    pyautogui.click(mailx, maily)
    time.sleep(.200)
    pyautogui.typewrite('pratyushtiwari224@gmail.com')
    print "Email field filled"
else:
    print "Email field not found"



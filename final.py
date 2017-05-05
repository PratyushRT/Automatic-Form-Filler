import pyautogui
import time

fieldsFilled=0

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
    fieldsFilled+=1
else:
    print "Name field not found"

time.sleep(1)
pyautogui.click(300, 400)
#tries to find the "Email" field
time.sleep(1)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite('email')
time.sleep(1)
#finds the "email" field and clicks on 60 horizontal units on the right and 60 vertical units below it; enters email

if pyautogui.locateOnScreen('email.png')!=None:
    mailx = pyautogui.locateOnScreen('email.png')[0] + 60
    maily = pyautogui.locateOnScreen('email.png')[1]+ 60
    time.sleep(1)
  

    pyautogui.click(mailx, maily)
    time.sleep(1)
    pyautogui.typewrite('pratyushtiwari224@gmail.com')
    print "Email field filled"
    fieldsFilled+=1
else:
    print "Email field not found"

time.sleep(1)
pyautogui.click(300, 400)
#tries to find the "Application ID" field
time.sleep(1)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite('application id')
time.sleep(1)
#finds the "Application ID" field and clicks on 60 horizontal units on the right and 60 vertical units below it; enters Application ID

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

time.sleep(1)
pyautogui.click(300, 400)
#tries to find the "Essay" field
time.sleep(1)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite("a Master's degree in CS is the correct choice for you?")
time.sleep(1)
#finds the "essay" field and clicks on 60 horizontal units on the right and 80 vertical units below it; 

if pyautogui.locateOnScreen('essay.png')!=None:
    essayx = pyautogui.locateOnScreen('essay.png')[0] + 60
    essayy = pyautogui.locateOnScreen('essay.png')[1]+ 80
    time.sleep(1)
  

    pyautogui.click(essayx, essayy)
    time.sleep(1)
    
    #enters essay by reading it line by line from essay.txt
    
    file=open("essay.txt", "r")
    for line in file:
        pyautogui.typewrite(line)
    print "Essay field filled"
    fieldsFilled+=1
else:
    print "Essay ID field not found"

time.sleep(1)
pyautogui.click(300, 400)
#tries to find the "Undergraduate Degree" field

time.sleep(1)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite('B. Sc.')
time.sleep(1)
#finds the "B. Sc." field and clicks on 10 horizontal units on the right and 10 vertical units below it; to select the check box

if pyautogui.locateOnScreen('degree.png')!=None:
    degreex = pyautogui.locateOnScreen('degree.png')[0] + 10
    degreey = pyautogui.locateOnScreen('degree.png')[1]+ 10
    time.sleep(1)
  

    pyautogui.click(degreex, degreey)
    time.sleep(1)
    
    print "Degree field filled"
    fieldsFilled+=1
else:
    print "Degree field not found"

pyautogui.click(300, 400)

#tries to find the "Undergraduate subject" field

pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite('undergraduate subject')

#finds the "Undergraduate subject" field and clicks on 60 horizontal units on the right and 60 vertical units below it; enters the undergraduate subject

if pyautogui.locateOnScreen('subject.png')!=None:
    subjectx = pyautogui.locateOnScreen('subject.png')[0] + 60
    subjecty = pyautogui.locateOnScreen('subject.png')[1]+ 60
    time.sleep(1)
    pyautogui.click(subjectx, subjecty)
    time.sleep(1)
    pyautogui.typewrite('Computer Science')
    print "Undergraduate Subject field filled"
    fieldsFilled+=1
else:
    print "Undergraduate subject field not found"
    
#identifies empty fields, if none present, clicks on the submit button
if pyautogui.locateOnScreen("emptyField.png")==None:
    pyautogui.click(300, 400)
    time.sleep(2)
    submitx=pyautogui.locateOnScreen("submit.png")[0]+10
    submity=pyautogui.locateOnScreen("submit.png")[1]+10
    pyautogui.click(submitx, submity)
    print "The form has been completed and submitted"
else:
    print str(fieldsFilled)+" fields in the form were field, please fill the rest and submit"


    

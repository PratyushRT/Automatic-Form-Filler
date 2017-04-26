import pyautogui
import time
import sys
#Displays the current coordinates of the Mouse position.
print "To quit, please press CTRL + C"
try:
    while True:
        x, y=pyautogui.position()
        #The method rjust() returns the string right justified
        position= "X: " + str(x).rjust(3) +" "+ "Y: " +str(y).rjust(3)
        
        
    
except KeyboardInterrupt:
    print "Done"

print position


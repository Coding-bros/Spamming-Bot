# Configuration

***NOW BEFORE RUNNING THE SCRIPT WHAT SHOULD BE INSTALLED ON YOUR PC?***

> PYTHON3

>PYAUTOGUI

## HOW TO INSTALL **PYAUTOGUI**

**OPEN YOUR TERMINAL WINDOW**

**TYPE**

> pip3 install pyautogui

## Now For **MacOS** Users

**You Need To Give Permissions**
> USE "pip3 install pyautogui"

> IF ***PERMISSION DENIED*** COMES, **Create a Virtual Env** and download again

> THEN THE PYTHON CODE SHOULD WORK ***PROPERLY***


# HOW DOES THE BOT WORK?

**IT FIRST ASKS YOU WHAT YOU WANT TO SPAM**

**THEN IT ASKS YOU HOW MANY TIMES YOU WANT TO SPAM**

**THEN YOU PRESS ENTER AND THE BOT SHOULD START WORKING**

**HOPE YOU ENJOY MY BOT :)**


# Any Problems
***CONTACT US TO:***
- jaideep1163@gmail.com
- bkp.karthi@gmail.com

# Code
```python
# importing pyautogui and time (no need to install time as it is a default module in python)
import pyautogui
import time

# this input asks us what we want to spam, the numbers before the text are to add color to the text
A = str(input("\033[1;34;;1mWhat Do You want to Spam:"))

# This input asks us how many times we want to spam the text, the numbers before the text are to add the color to the text.
b = int(input("\033[1;30;1mHow many Times Do You Want to Spam:"))

# adding a pause for 1 sec, so that it doesn't spam your terminal
time.sleep(1)

# this loop is to repeat the the code, till it reaches the number of times we added before, in how many times we want to spam
for i in range(b):
    # this line of code writes the text which we want to spam
    pyautogui.typewrite(A)
    # this line of code hits enter in your keyboard
    pyautogui.press("enter")

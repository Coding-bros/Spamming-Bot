import pyautogui
A = str(input("\033[1;34;;1mWhat Do You want to Spam:"))
b = int(input("\033[1;30;1mHow many Times Do You Want to Spam:"))
for i in range(b):
    pyautogui.typewrite(A)
    pyautogui.press("enter")

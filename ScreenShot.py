#  pip intsall pyautogui
import pyautogui
import tkinter as tk
from tkinter import filedialog

root= tk.Tk()
canvas1=tk.Canvas(root,width=300,height=300)
canvas1.pack()

def takeScreenShot():
    myScreenshot=pyautogui.screenshot()
    file_path=filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)
ScreenShotButton = tk.Button(text='Take Screenshot', command=takeScreenShot , bg='black', fg='white', font=10)
canvas1.create_window(150,150,window=ScreenShotButton)
root.mainloop()
from tkinter import mainloop
import pyautogui
import tkinter as tk
from tkinter.filedialog import *

print ("Hssss")
root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

#Se define la función que es llamada al presionar el botón
def takeScreenshot():
    myscreenshot = pyautogui.screenshot()
    savePath=asksaveasfilename()
    myscreenshot.save(savePath+"_CapturaPython.png")

#Se genera una ventana con un boton centrado para tomar captura
myButton = tk.Button(text="Take a Screenshot",command=takeScreenshot, font=10)
canvas1.create_window(150,150, window=myButton)

mainloop()
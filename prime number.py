from doctest import master
import tkinter as tk

def HRZ():
    number =int(blank.get())
    i = 2
    while True:
        if i >= number:
            answer.configure(text="YES")
            break
        if number % i == 0:
            answer.configure(text="NO")
            break
        i += 1 #i=i+1 


window = tk.Tk()
window.title("sorry Kaosuoy Kamlangmark")
window.minsize(width=350, height=400)

title =tk.Label(master= window, text="prime number")
title.pack()

blank =tk.Entry(master= window,width=40)
blank.pack()

button =tk.Button(master=window,width=10,text="ok", command= HRZ)
button.pack()

answer =tk.Label(master=window, text="YES or NO")
answer.pack()

window.mainloop()

import pyshorteners
from tkinter import *

def convertUrl():
    shorterClass = pyshorteners.Shortener()
    longUrl = urlField.get()
    shortUrl = shorterClass.tinyurl.short(longUrl)
    urlField.delete(0, END)
    urlField.insert(0, shortUrl)

gui = Tk()
gui.geometry("400x200")
gui.title("URL Shorter")

appTitle = Label(gui, text="URL Shorter", font=("century 20 bold"))
appTitle.pack(pady=20)

label = Label(gui, text="Enter your URL:", font=("century 10"))
label.pack(anchor="w")

urlField = Entry(gui, font=("century 12"), width=43)
urlField.pack(pady=10)

btn = Button(gui, text=("Convert"), font=("century 15 bold"), command=convertUrl,width=10, height=1, bg="blue", fg="white")
btn.pack()

gui.mainloop()

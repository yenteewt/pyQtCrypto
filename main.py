from tkinter import *

def encrypt():
    plainText = entPlain.get()
    # ToDo encrypt Plain Text
    print(plainText)


tkWindow = Tk()
tkWindow.title("PyCrypto")
tkWindow.geometry("640x480")

entPlain = Entry(master=tkWindow, width=100)
entPlain.place(x=20, y=40)

entDec = Entry(master=tkWindow, width=100)
entDec.place(x=20, y=100)

btnEncrypt = Button(master=tkWindow, text="encrypt", command=encrypt)
btnEncrypt.place(x=20, y=400)

tkWindow.mainloop()

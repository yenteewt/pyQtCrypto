# Import the necessary modules
import tkinter as tk
import base64
from Crypto.Cipher import AES

# Create the Model, which contains the data
class Model:
    def __init__(self, clearText, encryptedText):
        self.clearText = clearText
        self.encryptedtText = encryptedText


# Create the View, which contains the GUI elements
class View(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.entPlain = tk.Entry(master=self, width=100)
        self.entPlain.place(x=20, y=40)

        self.entDec = tk.Entry(master=self, width=100)
        self.entDec.place(x=20, y=100)

        self.label1 = tk.Label(master=self, text="Klartext")
        self.label1.place(x=20, y=15)

        self.label2 = tk.Label(master=self, text="Verschlüsselt")
        self.label2.place(x=20, y=75)

        self.btnEncrypt = tk.Button(master=self, text="encrypt", command=self.encrypt)
        self.btnEncrypt.place(x=20, y=400)

        self.label1.pack()
        self.entPlain.pack()
        self.label2.pack()
        self.entDec.pack()

        self.btnEncrypt.pack()

    def decrypt(self, key, ciphertext, cipher):
        pass

    def encrypt(self):

        inputText= self.entPlain.get()
        model = self.controller.encrypt(inputText)

        nachricht = self.entPlain.get()

        self.entDec.delete(0,100)
        self.entDec.insert(0, str(model.encryptedtText))

# Create the Controller, which contains the logic for the app
class Controller:
    def __init__(self):
        self.key = b'09865rfqghlafgtz78nafg3q'
        self.cipher = AES.new(self.key, AES.MODE_EAX)

    def encrypt(self, input_text):
        # Verschlüssele die Eingabe mit AES
        nonce = self.cipher.nonce
        ciphertext, tag = self.cipher.encrypt_and_digest(input_text.encode())

        # Konvertiere das verschlüsselte Ergebnis in base64, damit es angezeigt werden kann
        encrypted_text_base64 = base64.b64encode(nonce + tag + ciphertext).decode()

        # Erstelle ein neues Model-Objekt mit dem Klartext und dem verschlüsselten Text
        model = Model(input_text, encrypted_text_base64)
        return model


# Create an instance of the Controller
window = tk.Tk()
window.title("PyCryptor")
window.geometry('640x480')

# Erstelle den Controller und die View
controller = Controller()
view = View(window, controller)
view.pack()
window.mainloop()

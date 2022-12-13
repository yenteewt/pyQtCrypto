# Import the necessary modules
import tkinter as tk
from Crypto.Cipher import AES

# Create the Model, which contains the data
class Model:
    def __init__(self):
        self.counter = 0


# Create the View, which contains the GUI elements
class View(tk.Tk):
    def __init__(self, model):
        super().__init__()
        self.model = model

        self.title("PyCrypto")
        self.geometry("640x480")

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


    # Method to update the label with the current value of the counter
    def update_counter_label(self):
        pass
        #self.counter_label["text"] = f"Counter value: {self.model.counter}"

    # Method to increment the counter and update the label
    def encrypt(self):
        nachricht = self.entPlain.get()
        key = b'09865rfqghlafgtz78nafg3q'
        cipher = AES.new(key, AES.MODE_EAX)
        data = str.encode(nachricht)
        ciphertext, messageDigest = cipher.encrypt_and_digest(data)

        self.entDec.delete(0,100)
        self.entDec.insert(0, str(ciphertext))


# Create the Controller, which contains the logic for the app
class Controller:
    def __init__(self):
        # Create an instance of the Model
        self.model = Model()

        # Create an instance of the View
        self.view = View(self.model)

        # Update the counter label with the initial value of the counter
        self.view.update_counter_label()
        self.view.mainloop()


# Create an instance of the Controller
controller = Controller()

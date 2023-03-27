# This is a file that represents the View component in the MVC model
# it will contain the user interface of the project
# we have several windows including:
# Welcome window, encryption/decryption algorithms windows

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
class MainWindow(tk.Frame):
    # create the init method that will create the welcome window and the menu of buttons
    # Methods for creating the encryption decryption windows
    # Methods for displaying the results of encryption/decryption
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg='#344955')
        self.pack(fill=tk.BOTH, expand=True)
        # label for the title
        self.title_label = tk.Label(self, text="Weclome to CryptoGraphia", font=("Arial Bold", 20), bg=parent['bg'])
        self.title_label.pack(pady=20)

        self.introduction = """
        Cryptography is the practice of securing communication from third-party intruders or attackers. \
        It involves transforming data from its original form, called plaintext, into an unreadable form, called ciphertext, so that only authorized parties can understand the message. There are two main categories of cryptography techniques: symmetric-key and public-key cryptography. In symmetric-key cryptography, the same secret key is used to both encrypt and decrypt the message. The most common symmetric-key algorithms include Advanced Encryption Standard (AES), Data Encryption Standard (DES), and Blowfish.
        """
        tk.Label(self, text=self.introduction, font=("calibre", 15), justify="center", bg=parent['bg'], wraplength=500).pack(pady=10)

        self.encBtn = tk.Button(self, text="Secure your Messages", font=("calibre Bold", 17), bg="#f9aa33", fg='black', command=controller.showCalculator)
        self.encBtn.configure(padx=10, pady=10)
        self.encBtn.pack()

class Calculator(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller=controller
        self.pack(expand=True, fill=tk.BOTH)
        self.config(bg='#344955')

        tk.Label(self, text="Enter your text here for Encryption/Decryption", fg="white", bg='#344955', font=("calibri",16)).place(x=20, y=15)
        self.user_text = tk.Text(self, font="Arial 20", bg="#F9AA33", fg='black', bd=0)
        self.user_text.place(x=20, y=50, width=500, height=155)
        


        tk.Label(self, text="Enter secret key for Encryption/Decryption", fg="white", bg='#344955', font=("calibri", 16)).place(x=20, y=225)
        self.key = tk.StringVar()
        self.key_text = tk.Entry(self, textvariable=self.key, font=("arial", 20), show='*', bg="#F9AA33", fg='black', bd=0)
        self.key_text.place(x=20, y=260, width=450, height=65)

        tk.Label(self, text="Choose an Algorithm", fg="white", bg='#344955', font=("calibre", 16)).place(x=20, y=330)  
        algorithms = ['Caesar', 'Viginere', 'Polyalphabetic', 'Transposition', 'Playfair', 'Hill', 'RSA']
        self.combo = ttk.Combobox(self, values=algorithms, font=("calibre", 16))
        self.combo.set(algorithms[0])
        self.combo.place(x=20, y=365)


        tk.Button(self, text="Encrypt", height='2', width=20, bg="#ed3833", fg="white", font=("arial", 15), bd=0, command=controller.encrypt).place(x=20, y=415)
        tk.Button(self, text="Decrypt", height='2', width=20, bg="#00bd56", fg="white", font=("arial", 15), bd=0, command=controller.decrypt).place(x=280, y=415)
        tk.Button(self, text="Reset", height='2', width=44, bg="#1089ff", fg="white", font=("arial", 15), bd=0, command=controller.reset).place(x=20, y=500)






        
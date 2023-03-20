# This is a file that represents the View component in the MVC model
# it will contain the user interface of the project
# we have several windows including:
# Welcome window, encryption/decryption algorithms windows

import tkinter as tk
from PIL import Image, ImageTk
class MainWindow(tk.Frame):
    # create the init method that will create the welcome window and the menu of buttons
    # Methods for creating the encryption decryption windows
    # Methods for displaying the results of encryption/decryption
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.pack(fill=tk.BOTH, expand=True)
        # label for the title
        self.title_label = tk.Label(self, text="Weclome to CryptoGraphia", font=("Arial Bold", 20), bg=parent['bg'])
        self.title_label.pack(pady=20)

        self.introduction = """
        Cryptography is the practice of securing communication from third-party intruders or attackers.
        It involves transforming data from its original form, called plaintext, into an unreadable form, called ciphertext, so that only authorized parties can understand the message.
        There are two main categories of cryptography techniques: symmetric-key and public-key cryptography.
        In symmetric-key cryptography, the same secret key is used to both encrypt and decrypt the message.
        The most common symmetric-key algorithms include Advanced Encryption Standard (AES), Data Encryption Standard (DES), and Blowfish.

        On the other hand, public-key cryptography uses two separate keys: a public key for encryption and a private key for decryption. The most well-known public-key algorithm is the RSA algorithm.
        Other classical encryption techniques include:
        Caesar cipher: a simple substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
        Vigenère cipher: a polyalphabetic substitution cipher that uses a series of interwoven Caesar ciphers based on a keyword.
        Playfair cipher: a polygraphic substitution cipher that encrypts pairs of letters instead of single letters.
        Hill cipher: a block cipher that encrypts blocks of plaintext as matrix multiplication using a key matrix.
        These techniques, while historically important, are no longer widely used due to their vulnerability to modern cryptanalysis methods. However, they are still studied as important milestones in the history of cryptography.
        """
        self.intro_label = tk.Label(self, text=self.introduction, font=("Arial", 15), bg=parent['bg'], wraplength=1000)
        self.intro_label.pack(pady=10)

        self.enc_label = tk.Label(self, text="Here is the list of Classical Encryption Algorithms", font=("Arial", 15), bg=parent['bg'])
        self.enc_label.pack(pady=20)
        self.encBtn = tk.Button(self, text="Algorithms Calculator", font=("Arial Bold", 17), bg="#B8B886", command=controller.showAlgorithmsCalculator)
        self.encBtn.configure(padx=10, pady=10)
        self.encBtn.pack()

class AlgorithmsCalculator(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller=controller
        self.pack(expand=True, fill=tk.BOTH)

        self.cipher_label = tk.Label(self, text="Ciphertext:", font=("Arial Bold", 20))
        self.cipher_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.ciphertext = tk.Text(self, font=("Arial", 15), height=5)
        self.ciphertext.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.cipher_key = tk.Entry(self, font=("Arial", 15))
        self.cipher_key.grid(row=1, column=4, padx=10, pady=10)

        self.plain_label = tk.Label(self, text="Plaintext:", font=("Arial Bold", 20))
        self.plain_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.plaintext = tk.Text(self, font=("Arial", 15), height=5)
        self.plaintext.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
        self.plain_key = tk.Entry(self, font=("Arial", 15))
        self.plain_key.grid(row=3, column=4, padx=10, pady=10)

        self.btnFrame = tk.Frame(self)

        button_attrs = [
            {"text": "Caesar", "row": 1, "column": 0},
            {"text": "Viginere", "row": 1, "column": 1},
            {"text": "Playfair", "row": 1, "column": 2},
            {"text": "Polyalphabetic", "row": 2, "column": 0},
            {"text": "Transposition", "row": 2, "column": 1},
            {"text": "Hill", "row": 2, "column": 2},
            {"text": "RSA", "row": 3, "column": 1},
        ]

        for button_attr in button_attrs:
            button = tk.Button(self.btnFrame, text=button_attr["text"], font=("Arial Bold", 15), bg="#B8B886", width=15, 
            command=lambda text=button_attr["text"]: self.controller.showCipherPlain(text.lower()))
            button.grid(row=button_attr["row"], column=button_attr["column"], padx=10, pady=10, sticky=tk.W+tk.E)
        
        options = ['Encrypt', 'Decrypt']
        self.selected_option = tk.StringVar()
        self.selected_option.set(options[0])
        self.options_menu = tk.OptionMenu(self.btnFrame, self.selected_option, *options)
        self.options_menu.grid(row=2, column=3, padx=10, pady=10, sticky=tk.W+tk.E)
        self.options_menu.config(width=15, font=("Arial Bold", 15), bg="#B8B886")

        self.btnFrame.grid(row=4, column=0, columnspan=3, pady=20, padx=15, sticky=tk.W+tk.E)





        
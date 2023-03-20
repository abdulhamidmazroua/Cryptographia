# The controller component that will contain the Controller class. This class will have the following methods:
# Functions that will process the user input and call the appropriate encryption/decryption functions from the model.
# Functions that will handle the events triggered by the GUI framework, such as button clicks and menu selections.

import tkinter as tk
import view
import model
class Controller:
    pass
    def __init__(self) -> None:

        self.root = tk.Tk()
        self.root.title("Cryptographia")
        self.root.geometry("1024x750")
        
        self.currentWindow = None

        self.showMainWindow()

        self.root.mainloop()

    def showMainWindow(self):
        if self.currentWindow:
            self.currentWindow.destroy()
        self.currentWindow = view.MainWindow(self.root, self)

    def showAlgorithmsCalculator(self):
        if self.currentWindow:
            self.currentWindow.destroy()
        self.currentWindow = view.AlgorithmsCalculator(self.root, self)

    def showCipherPlain(self, algorithm):
        option = self.currentWindow.selected_option.get().lower()

        if option == 'encrypt':
            plain = self.currentWindow.plaintext.get("1.0", tk.END).strip()
            key = self.currentWindow.plain_key.get().lower().strip()
            algorithms_list ={'caesar': model.caesar_encrypt, 'viginere': model.full_vigenere_encrypt, 'playfair': model.playfair_encrypt, 
            'polyalphabetic': model.polyalphabetic_encrypt, 'transposition': model.transposition_encrypt, 'hill': model.hill_encrypt,
            'rsa': model.rsa_encrypt}
            ouptut_cipher = algorithms_list[algorithm](plain, key)
            self.currentWindow.ciphertext.delete("1.0", tk.END)
            self.currentWindow.ciphertext.insert("1.0", ouptut_cipher)

        elif option == 'decrypt':
            cipher = self.currentWindow.ciphertext.get("1.0", tk.END).strip()
            key = self.currentWindow.cipher_key.get().lower().strip()
            algorithms_list ={'caesar': model.caesar_decrypt, 'viginere': model.full_vigenere_decrypt, 'playfair': model.playfair_decrypt, 
            'polyalphabetic': model.polyalphabetic_decrypt, 'transposition': model.transposition_decrypt, 'hill': model.hill_decrypt,
            'rsa': model.rsa_decrypt}
            output_plain = algorithms_list[algorithm](cipher, key)
            self.currentWindow.plaintext.delete("1.0", tk.END)
            self.currentWindow.plaintext.insert("1.0", output_plain)

        

# The controller component that will contain the Controller class. This class will have the following methods:
# Functions that will process the user input and call the appropriate encryption/decryption functions from the model.
# Functions that will handle the events triggered by the GUI framework, such as button clicks and menu selections.

import tkinter as tk
from tkinter import messagebox
import view
import model
class Controller:
    pass
    def __init__(self) -> None:

        self.root = tk.Tk()
        self.root.title("Cryptographia")
        self.root.geometry("550x600")
        self.root.config(bg="#344955")
        
        self.currentWindow = None

        self.showMainWindow()

        self.root.mainloop()

    def showMainWindow(self):
        if self.currentWindow:
            self.currentWindow.destroy()
        self.currentWindow = view.MainWindow(self.root, self)

    def showCalculator(self):
        if self.currentWindow:
            self.currentWindow.destroy()
        self.currentWindow = view.Calculator(self.root, self)

    def display_output(self, output_text, algo_type):
        '''Accepts the cipher/plain and displays the output in a mini window'''
        output = tk.Toplevel(self.currentWindow)
        output.title("Display Message")
        output.geometry('400x200')
        output.configure(bg="#ed3833")
        tk.Label(output, text=f"Your {algo_type} Message:", bg=output['bg'], font=("arial", 20)).place(x=20, y=20)
        cipher_text = tk.Text(output, bg=output['bg'], bd=2, fg='white', font=('calibre', 18))
        cipher_text.place(x=30, y=65, width=350, height=120)
        cipher_text.insert(tk.END, output_text)

    def encrypt(self):
        function_name = {'caesar':model.caesar_encrypt, 'viginere': model.full_vigenere_encrypt,'polyalphabetic': model.polyalphabetic_encrypt,
                         'transposition': model.transposition_encrypt, 'hill': model.hill_encrypt,
                         'playfair': model.playfair_encrypt, 'rsa': model.rsa_encrypt}
        try:
            cipher = function_name[self.currentWindow.combo.get().lower()](self.currentWindow.user_text.get('1.0', tk.END), self.currentWindow.key.get())
            self.display_output(cipher, 'Encrypted')
        except model.KeyNotValid as e:
            messagebox.showerror("Encryption", str(e))

    def decrypt(self):
        function_name = {'caesar':model.caesar_decrypt, 'viginere': model.full_vigenere_decrypt,'polyalphabetic': model.polyalphabetic_decrypt,
                         'transposition': model.transposition_decrypt, 'hill': model.hill_decrypt,
                         'playfair': model.playfair_decrypt, 'rsa': model.rsa_decrypt}
        try:
            plain = function_name[self.currentWindow.combo.get().lower()](self.currentWindow.user_text.get('1.0', tk.END), self.currentWindow.key.get())
            self.display_output(plain, 'Decrypted')
        except model.KeyNotValid as e:
            messagebox.showerror("Decryption", str(e))
    def reset(self):
        self.currentWindow.user_text.delete('1.0', tk.END)
        self.currentWindow.key_text.delete(0, tk.END)
        # print("This text will be reset")
        # print(f"The text is {self.currentWindow.user_text.get('1.0', tk.END)}")
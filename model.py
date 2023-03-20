import random
import numpy as np

# Caesar cipher
def caesar_encrypt(plaintext, shift):
    shift = int(shift)
    result = ""
    for char in plaintext:
        if char.isalpha():
            char = chr((ord(char.upper()) - 65 + shift) % 26 + 65)
        result += char
    return result

def caesar_decrypt(ciphertext, shift):
    shift = int(shift)
    return caesar_encrypt(ciphertext, -shift)


# Full Vigenere cipher
def full_vigenere_encrypt(plaintext, key):
    result = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            char = chr((ord(char.upper()) + shift - 130) % 26 + 65)
            key_index += 1
        result += char
    return result

def full_vigenere_decrypt(ciphertext, key):
    result = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            char = chr((ord(char.upper()) - shift - 130) % 26 + 65)
            key_index += 1
        result += char
    return result


# Playfair cipher
def playfair_generate_key(key):
    key_matrix = []
    for char in key.upper().replace("J", "I"):
        if char not in key_matrix and char.isalpha():
            key_matrix.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in key_matrix:
            key_matrix.append(char)
    return key_matrix

def playfair_encrypt(plaintext, key):
    key_matrix = playfair_generate_key(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    if len(plaintext) % 2 == 1:
        plaintext += "X"
    result = ""
    for i in range(0, len(plaintext), 2):
        a = plaintext[i]
        b = plaintext[i+1]
        a_row, a_col = divmod(key_matrix.index(a), 5)
        b_row, b_col = divmod(key_matrix.index(b), 5)
        if a_row == b_row:
            result += key_matrix[a_row][(a_col+1)%5] + key_matrix[b_row][(b_col+1)%5]
        elif a_col == b_col:
            result += key_matrix[(a_row+1)%5][a_col] + key_matrix[(b_row+1)%5][b_col]
        else:
            result += key_matrix[a_row][b_col] + key_matrix[b_row][a_col]
    return result


# Playfair cipher
def playfair_decrypt(ciphertext, keyword):
    # Generate the key table
    key_table = playfair_generate_key(keyword)

    # Convert the ciphertext to uppercase and remove whitespace
    ciphertext = ciphertext.upper().replace(" ", "")

    # Split the ciphertext into digrams and decrypt each digram
    digrams = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    plaintext = ""
    for digram in digrams:
        row1, col1 = divmod(key_table[digram[0]], 5)
        row2, col2 = divmod(key_table[digram[1]], 5)
        if row1 == row2:
            # Same row, shift columns to the left
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            # Same column, shift rows up
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            # Rectangle, swap columns
            col1, col2 = col2, col1
        plaintext += key_table[row1*5 + col1] + key_table[row2*5 + col2]
    return plaintext


# Polyalphabetic cipher
def polyalphabetic_generate_key(keyword):
    keyword = keyword.upper()
    key = []
    for char in keyword:
        key.append(ord(char) - 65)
    return key

def polyalphabetic_encrypt(plaintext, keyword):
    key = polyalphabetic_generate_key(keyword)
    result = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = key[key_index % len(key)]
            char = chr((ord(char.upper()) + shift - 130) % 26 + 65)
            key_index += 1
        result += char
    return result

def polyalphabetic_decrypt(ciphertext, keyword):
    key = polyalphabetic_generate_key(keyword)
    result = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = key[key_index % len(key)]
            char = chr((ord(char.upper()) - shift - 130) % 26 + 65)
            key_index += 1
        result += char
    return result


# Transposition cipher
def transposition_encrypt(plaintext, key):
    # Add padding to the plaintext if necessary
    padding_length = len(key) - (len(plaintext) % len(key))
    if padding_length < len(key):
        plaintext += " " * padding_length

    # Split the plaintext into rows and transpose
    num_columns = len(key)
    num_rows = (len(plaintext) + num_columns - 1) // num_columns
    rows = [plaintext[i:i+num_columns] for i in range(0, len(plaintext), num_columns)]
    transposed_rows = []
    for i in range(num_columns):
        transposed_rows.append("".join([row[i] for row in rows]))

    # Sort the key and rearrange the transposed rows
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    ciphertext = ""
    for index in sorted_key_indices:
        ciphertext += transposed_rows[index]

    return ciphertext

def transposition_decrypt(ciphertext, key):
    # Split the ciphertext into rows and rearrange
    num_columns = len(key)
    num_rows = (len(ciphertext) + num_columns - 1) // num_columns
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    num_short_columns = len(key) - len(ciphertext) % len(key)
    plaintext = ""
    col = 0
    row = 0
    for index in range(len(ciphertext)):
        row = index % num_rows
        col = sorted_key_indices[index // num_rows]
        if col >= num_columns - num_short_columns:
            row -= 1
        plaintext += ciphertext[row*num_columns + col]

    return plaintext


# Hill cipher
def hill_encrypt(plaintext, key):
    # Convert plaintext to numbers
    plaintext = plaintext.upper()
    plaintext = [ord(char) - 65 for char in plaintext]
    plaintext = np.array(plaintext)

    # Make sure the key is square and invertible
    key = np.array(key)
    det = np.linalg.det(key)
    if det == 0 or np.gcd(int(det), 26) != 1:
        raise ValueError("Invalid key")

    # Pad the plaintext with dummy values if necessary
    if len(plaintext) % key.shape[0] != 0:
        padding = key.shape[0] - len(plaintext) % key.shape[0]
        plaintext = np.concatenate([plaintext, np.zeros(padding, dtype=int)])

    # Reshape the plaintext into a matrix and multiply with the key
    plaintext = plaintext.reshape((-1, key.shape[0]))
    ciphertext = np.dot(plaintext, key) % 26

    # Convert ciphertext back to characters
    ciphertext = "".join([chr(char + 65) for char in ciphertext.flatten()])
    return ciphertext

def hill_decrypt(ciphertext, key):
    # Convert ciphertext to numbers
    ciphertext = ciphertext.upper()
    ciphertext = [ord(char) - 65 for char in ciphertext]
    ciphertext = np.array(ciphertext)

    # Make sure the key is square and invertible
    key = np.array(key)
    det = np.linalg.det(key)
    if det == 0 or np.gcd(int(det), 26) != 1:
        raise ValueError("Invalid key")

    # Invert the key and multiply with the ciphertext
    inv_key = np.linalg.inv(key)
    plaintext = np.dot(ciphertext.reshape((-1, key.shape[0])), inv_key) % 26

    # Convert plaintext back to characters
    plaintext = "".join([chr(char + 65) for char in plaintext.flatten()])
    return plaintext


# RSA cipher
def rsa_encrypt(plaintext, public_key):
    n, e = public_key
    ciphertext = [(ord(char) ** e) % n for char in plaintext]
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    n, d = private_key
    plaintext = [chr((char ** d) % n) for char in ciphertext]
    return "".join(plaintext)

def rsa_generate_key_pair(bit_length=1024):
    # Generate two large primes
    p = rsa_generate_large_prime(bit_length // 2)
    q = rsa_generate_large_prime(bit_length // 2)

    # Calculate n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose a public exponent e
    e = 65537
    while rsa_gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n - 1)

    # Calculate the private exponent d
    d = rsa_modular_inverse(e, phi_n)

    # Return the public and private keys
    return (n, e), (n, d)

def rsa_generate_large_prime(bit_length):
    while True:
        # Generate a random number of the specified bit length
        p = random.getrandbits(bit_length)

        # Set the two highest bits to ensure that p is of the desired bit length
        p |= (1 << bit_length - 1) | 1 << bit_length - 2

        # Test if p is prime
        if rsa_is_prime(p):
            return p

def rsa_is_prime(n, k=10):
    # Check if n is even
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Perform k Miller-Rabin tests
    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def rsa_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rsa_extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = rsa_extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def rsa_modular_inverse(a, n):
    gcd, x, y = rsa_extended_gcd(a, n)
    if gcd != 1:
        return None
    return x % n
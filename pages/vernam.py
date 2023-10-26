import random
import streamlit as st


# Function to generate a random key of specified length
def generate_key(length):
    key = ""
    for i in range(length):
        key += chr(random.randint(65, 90))
    return key


# Function to encrypt plaintext using Vernam Cipher
def vernam_cipher_encrypt(plain_text, key):
    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_text += chr((ord(plain_text[i]) + ord(key[i])) % 26 + 65)
    return cipher_text


# Function to decrypt ciphertext using Vernam Cipher
def vernam_cipher_decrypt(cipher_text, key):
    plain_text = ""
    for i in range(len(cipher_text)):
        plain_text += chr((ord(cipher_text[i]) - ord(key[i])) % 26 + 65)
    return plain_text


def app():
    st.title('Vernam Cipher')
    plain_text = st.text_input("Enter Plain Text: ")
    plain_text = plain_text.upper()
    if plain_text:
        key = generate_key(len(plain_text))
        cipher_text = vernam_cipher_encrypt(plain_text, key)
        decrypted_text = vernam_cipher_decrypt(cipher_text, key)
        col1, col2 = st.columns([1, 1])
        col1.write(f"Generated Key: {key}")
        text = f"Ciphertext: {cipher_text}"
        col1.success(text)
        col2.write(f"Plaintext: {plain_text}")
        text = f"Decrypted Text: {decrypted_text}"
        col2.success(text)




if __name__ == '__main__':
    app()

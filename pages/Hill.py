import numpy as np
import streamlit as st


def encrypt(plaintext, key):
    PT_matrix = [[(ord(ch) - 97) % 26] for ch in plaintext]
    col1, col2 = st.columns([1, 1])
    col1.subheader('Plain Text Matrix')
    col1.markdown(PT_matrix)
    key_matrix = [[(ord(ch) - 97) % 26] for ch in key]
    col2.subheader('Key Matrix')
    col2.markdown(key_matrix)

    CT_matrix = [[0 for i in range(len(PT_matrix[0]))] for j in range(len(key_matrix))]
    for i in range(len(key_matrix)):
        for j in range(len(PT_matrix[0])):
            for k in range(len(key_matrix[0])):
                CT_matrix[i][j] += key_matrix[i][k] * PT_matrix[k][j]

    ciphertext = ''.join(
        [chr((CT_matrix[i][j] % 26) + ord('A')) for i in range(len(CT_matrix)) for j in range(len(CT_matrix[0]))])
    return ciphertext, CT_matrix, key_matrix


def decrypt(ciphertext, key_matrix):
    inversekey = np.linalg.inv(key_matrix)
    PT_matrix = [[0 for i in range(len(ciphertext[0]))] for j in range(len(inversekey))]
    for i in range(len(inversekey)):
        for j in range(len(ciphertext[0])):
            for k in range(len(inversekey[0])):
                PT_matrix[i][j] += inversekey[i][k] * ciphertext[k][j]

    plaintext = ''.join(
        [chr((PT_matrix[i][j] % 26) + ord('A')) for i in range(len(PT_matrix)) for j in range(len(PT_matrix[0]))])
    return ciphertext


def app():
    # print("enter plain text")
    st.title('Hill Cipher')
    PT = st.text_input('Enter Plain Text')
    # print("enter key")
    Key = st.text_input('Enter Key')
    if PT and Key:
        cipher, ciphertext, key_matrix = encrypt(PT, Key)
        text = f"encrypted text: {cipher}"
        st.success(text)


# print("Decrypted or original text:", decrypt(ciphertext, key_matrix))


if __name__ == '__main__':
    app()

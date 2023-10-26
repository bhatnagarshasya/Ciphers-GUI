import streamlit as st

def create_matrix(plaintext, key):
    matrix = [['*'] * 5 for _ in range(5)]
    key = key.replace(" ", "")
    key = ''.join(key)
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    for i in range(len(key)):
        matrix[i // 5][i % 5] = key[i]

    ptr = 0
    newalpha = ''
    for i in alphabet:
        if i not in key:
            newalpha += i

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == '*':
                matrix[i][j] = newalpha[ptr]
                ptr += 1
    return matrix


def encryption(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.lower()

    i = 0
    while i < len(plaintext) - 1:
        if plaintext[i] == plaintext[i + 1]:
            plaintext = plaintext[:i + 1] + 'x' + plaintext[i + 1:]
        i += 1
    if len(plaintext) % 2 != 0:
        plaintext += 'x'

    key = {}
    for i in range(5):
        for j in range(5):
            key[key_matrix[i][j]] = (i, j)

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a, b = key[plaintext[i]], key[plaintext[i + 1]]
        if a[0] == b[0]:
            ciphertext += key_matrix[a[0]][(a[1] + 1) % 5]
            ciphertext += key_matrix[b[0]][(b[1] + 1) % 5]
        elif a[1] == b[1]:
            ciphertext += key_matrix[(a[0] + 1) % 5][a[1]]
            ciphertext += key_matrix[(b[0] + 1) % 5][b[1]]
        else:
            ciphertext += key_matrix[a[0]][b[1]]
            ciphertext += key_matrix[b[0]][a[1]]
    return ciphertext


def app():
    st.title('Playfair Cipher')
    PT = st.text_input("enter plain text:")
    keyword = st.text_input("enter the key:")
    if PT and keyword:
        key_matrix = create_matrix(PT, keyword)
        st.header('Key Matrix')
        st.markdown(key_matrix)
        text = f"the encrypted text is: {encryption(PT, key_matrix)}"
        st.success(text)


if __name__ == '__main__':
    app()

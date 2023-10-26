import streamlit as st


def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    st.subheader('Key Matrix')
    st.markdown(key)
    return "".join(key)


def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = ((ord(string[i]) - 97) +
             (ord(key[i]) - 97)) % 26
        x += 97
        cipher_text.append(chr(x))
    return "".join(cipher_text)


def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i])) % 26
        x += ord('A')

        orig_text.append(chr(x))
    return "".join(orig_text)


def app():
    st.title('Vignere Cipher')
    string = st.text_input("Enter the plain text")
    keyword = st.text_input("Enter key")
    if string and keyword:
        key = generateKey(string, keyword)
        cipher_text = cipherText(string, key)
        col1, col2 = st.columns([1, 1])
        text = f"Ciphertext : {cipher_text}"
        col1.success(text)
        text = f"Original/Decrypted Text : {originalText(cipher_text, key)}"
        col2.success(text)


if __name__ == '__main__':
    app()

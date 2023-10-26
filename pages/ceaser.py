import streamlit as st


def ceaser_(plain_t, key):
    print("enter plain text: ")
    # plain_t = input()
    print("enter key: ")
    # key = int(input())
    cipher_t = ""

    for i in range(len(plain_t)):
        index = plain_t[i]

        if index.isupper():
            print('Current Exec', ord(index), key)
            cipher_t += chr((ord(index) + key - 65) % 26 + 65)

        else:
            cipher_t += chr((ord(index) + key - 97) % 26 + 97)

    print("Encrypted text: ", cipher_t)
    decrypted = ""
    for i in range(len(cipher_t)):
        index = cipher_t[i]

        if index.isupper():
            decrypted += chr((ord(index) - key - 65) % 26 + 65)
        else:
            decrypted += chr((ord(index) - key - 97) % 26 + 97)

    print("Decrypted text: ", decrypted)
    return (decrypted, cipher_t)


def app():
    st.title('Ceaser Cipher')
    st.header('Encryption')
    st.write()
    col1, col2 = st.columns([1, 1])


    PlainText = col1.text_input('Enter Text to be Encrypted')
    Key = col2.number_input('Enter the Key for Encryption')
    Key = int(Key)
    if PlainText and Key:

        (decrypted, encrypted) = ceaser_(PlainText, Key)
        st.caption(f'Encrypted Message is : {encrypted}')
        st.header('Decryption')
        st.caption(f'Decrypted Message is : {decrypted}')


if __name__ == '__main__':
    app()

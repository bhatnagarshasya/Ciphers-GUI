import streamlit as st

def railfence(PT):
    rail = [['\n' for i in range(len(PT))]
            for j in range(2)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(PT)):
        if (row == 0) or (row == 1):
            dir_down = not dir_down
        rail[row][col] = PT[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    st.subheader('Rail Fence')
    for i in rail:
        st.markdown(i)
    result = []
    for i in range(2):
        for j in range(len(PT)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    st.subheader('Result')
    st.markdown(result)
    return "".join(result)


def derailfence(CT):
    rail = [['\n' for i in range(len(CT))]
            for j in range(2)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(CT)):
        if row == 0:
            dir_down = True
        if row == 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(2):
        for j in range(len(CT)):
            if ((rail[i][j] == '*') and
                    (index < len(CT))):
                rail[i][j] = CT[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(CT)):

        if row == 0:
            dir_down = True
        if row == 1:
            dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)


def app():
    st.title('Rail Fence Cipher')
    plaintext = st.text_input("enter the plain text:")
    if plaintext:
        ciphertext = railfence(plaintext)
        col1, col2 = st.columns([1, 1])
        col1.header('Encryption')
        text = f"cipher text: {ciphertext}"
        col1.success(text)
        col2.header('Decryption')
        text = f"decrypted text: {derailfence(ciphertext)}"
        col2.success(text)


if __name__ == '__main__':
    app()

import random
from math import pow
import streamlit as st

a = random.randint(2, 10)


# To fing gcd of two numbers
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# For key generation i.e. large random number
def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
    return key


def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
    return x % c


# For asymetric encryption
def encryption(msg, q, h, g):
    ct = []
    k = gen_key(q)
    s = power(h, k, q)
    p = power(g, k, q)
    for i in range(0, len(msg)):
        ct.append(msg[i])
    st.write("g^k used= ", p)
    st.write("g^ak used= ", s)
    for i in range(0, len(ct)):
        ct[i] = s * ord(ct[i])
    return ct, p


# For decryption
def decryption(ct, p, key, q):
    pt = []
    h = power(p, key, q)
    for i in range(0, len(ct)):
        pt.append(chr(int(ct[i] / h)))
    return pt


def app():
    st.header("ElGamal Encryption")
    msg = st.text_input("Enter message.")
    if msg:
        q = random.randint(pow(10, 20), pow(10, 50))
        g = random.randint(2, q)
        key = gen_key(q)
        h = power(g, key, q)
        st.write("g used=", g)
        st.write("g^a used=", h)
        ct, p = encryption(msg, q, h, g)
        text = f"Original Message={msg}"
        st.success(text)
        st.subheader("Encrypted Message:")
        text = f"{ct}"
        st.success(text)
        pt = decryption(ct, p, key, q)
        d_msg = ''.join(pt)
        st.subheader("Decrypted Message:")
        st.success(d_msg)


if __name__ == '__main__':
    app()

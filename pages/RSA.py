import math
import streamlit as st

def app():
    st.title('RSA')
    # Input Prime Numbers
    # st.write("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")
    p = st.number_input("Enter a prime number for p: ")
    p = int(p)
    q = st.number_input("Enter a prime number for q: ")
    q = int(q)

    # Check if Input's are Prime
    # THIS FUNCTION AND THE CODE IMMEDIATELY BELOW THE FUNCTION CHECKS WHETHER THE INPUTS ARE PRIME OR NOT.


    def prime_check(a):
        if (a == 2):
            return True
        elif ((a < 2) or ((a % 2) == 0)):
            return False
        elif (a > 2):
            for i in range(2, a):
                if not (a % i):
                    return \
                        False
        return True

    if p and q:
        check_p = prime_check(p)
        check_q = prime_check(q)
        #count = 1
        if (((check_p == False) or (check_q == False))):
            st.error('Number should be Prime')
        #   p = st.number_input("Enter a prime number for p : ")
        #   p = int(p)
        #    q = st.number_input("Enter a prime number for q : ")
        #   q = int(q)
        #   check_p = prime_check(p)
        #    check_q = prime_check(q)
        else:
                st.success('Entered Numbers are Prime')

                # RSA Modulus
                # '''CALCULATION OF RSA MODULUS 'n'.'''
                n = p * q
                st.write("RSA Modulus(n) is:", n)

                # Eulers Toitent
                # '''CALCULATION OF EULERS TOITENT 'r'.'''
                r = (p - 1) * (q - 1)
                st.write("Eulers Toitent(r) is:", r)

                # GCD
                # '''CALCULATION OF GCD FOR 'e' CALCULATION.'''


                def egcd(e, r):
                    while (r != 0):
                        e, r = r, e % r
                    return e


                # Euclid's Algorithm
                def eugcd(e, r):
                    for i in range(1, r):
                        while (e != 0):
                            a, b = r // e, r % e
                            # if (b != 0):
                            # st.write("%d = %d*(%d) + %d" % (r, a, e, b))
                            r = e
                            e = b


                # Extended Euclidean Algorithm
                def eea(a, b):
                    if (a % b == 0):
                        return (b, 0, 1)
                    else:
                        gcd, s, t = eea(b, a % b)
                        s = s - ((a // b) * t)
                        # st.write("%d = %d*(%d) + (%d)*(%d)" % (gcd, a, t, s, b))
                        return (gcd, t, s)


                # Multiplicative Inverse
                def mult_inv(e, r):
                    gcd, s, _ = eea(e, r)
                    if (gcd != 1):
                        return None
                    else:
                        # if (s < 0):
                        # st.write("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d." % (s, s, s % r))
                        # elif (s > 0):
                        # st.write("s=%d." % (s))
                        return s % r


                # e Value Calculation
                # '''FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME.'''
                for i in range(1, 1000):
                    if (egcd(i, r) == 1):
                        e = i
                st.write("The value of e is:", e)

                # d, Private and Public Keys
                # '''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''

                eugcd(e, r)

                d = mult_inv(e, r)

                st.write("The value of d is:", d)

                public = (e, n)
                private = (d, n)
                st.write("Private Key is:", private)
                st.write("Public Key is:", public)

                # Encryption
                # '''ENCRYPTION ALGORITHM.'''


                def encrypt(pub_key, n_text):
                    e, n = pub_key
                    x = []
                    m = 0
                    for i in n_text:
                        if (i.isupper()):
                            m = ord(i) - 65
                            c = (m ** e) % n
                            x.append(c)
                        elif (i.islower()):
                            m = ord(i) - 97
                            c = (m ** e) % n
                            x.append(c)
                        elif (i.isspace()):
                            spc = 400
                            x.append(400)
                    return x


                # Decryption
                # '''DECRYPTION ALGORITHM'''


                def decrypt(priv_key, c_text):
                    d, n = priv_key
                    txt = c_text.split(',')
                    x = ''
                    m = 0
                    for i in txt:
                        if (i == '400'):
                            x += ' '
                        else:
                            m = (int(i) ** d) % n
                            m += 65
                            c = chr(m)
                            x += c
                    return x


                # Message
                message = input("What would you like encrypted or decrypted?(Separate numbers with ',' for decryption):")
                st.write("Your message is:", message)

                # Choose Encrypt or Decrypt and st.write
                choose = input("Type '1' for encryption and '2' for decrytion.")
                if (choose == '1'):
                    enc_msg = encrypt(public, message)
                    st.write("Your encrypted message is:", enc_msg)
                elif (choose == '2'):
                    st.write("Your decrypted message is:", decrypt(private, message))
                else:
                    st.write("You entered the wrong option.")



if __name__ == '__main__':
    app()

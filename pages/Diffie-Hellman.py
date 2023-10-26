import streamlit as st

def prime_checker(p):
    # Checks If the number entered is a Prime Number or not
    if p < 1:
        return -1
    elif p > 1:
        if p == 2:
            return 1
        for i in range(2, p):
            if p % i == 0:
                return -1
            return 1


def primitive_check(g, p, L):
    # Checks If The Entered Number Is A Primitive Root Or Not
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return -1
        return 1


def app():
    st.header("Diffie-Hellman")
    l = []
    count = 1

    P = st.number_input(f"Enter a prime number P : ")

    P = int(P)
    if P:
        if prime_checker(P) == -1:
            st.write("Number Is Not Prime, Please Enter Again!")



        G = st.number_input(f"Enter The Primitive Root Of {P} : ")
        if primitive_check(G, P, l) == -1:
            st.write(f"Number Is Not A Primitive Root Of {P}, Please Try Again!")



        # Private Keys
        x1 = st.number_input("Enter The Private Key Of User 1 : ")
        x2 = st.number_input("Enter The Private Key Of User 2 : ")

        if x1 >= P or x2 >= P:
            st.write(f"Private Key Of Both The Users Should Be Less Than {P}!")



        # Calculate Public Keys
        y1, y2 = pow(G, x1) % P, pow(G, x2) % P

        # Generate Secret Keys
        k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P

        st.write(f"\nSecret Key For User 1 Is {k1}\nSecret Key For User 2 Is {k2}\n")

        if k1 == k2:
            st.write("Keys Have Been Exchanged Successfully")
        else:
            st.write("Keys Have Not Been Exchanged Successfully")





if __name__ == '__main__':
    app()

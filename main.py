import streamlit as st

footer = """
<style>
footer:after{
    content:'Copyright ©️ Pratham Sharma 2023';
    display:block;
    padding:5px
    top:3px;
}
</style>
"""


def app():
    st.set_page_config(
        page_title='Cyber Sec',
        page_icon='👾',
    )
    st.markdown(footer, unsafe_allow_html=True)
    st.header("Welcome To The Ciphers Calculator App")
    st.subheader("⬅️ Choose a Cipher from the side menu")


if __name__ == '__main__':
    app()

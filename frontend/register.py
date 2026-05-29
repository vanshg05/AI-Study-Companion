import streamlit as st # type: ignore
import requests # type: ignore

API_URL = "http://127.0.0.1:8000"

st.title(
    "📝 Register"
)

username = st.text_input(
    "Username"
)

email = st.text_input(
    "Email"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Register"):

    response = requests.post(
        f"{API_URL}/register",
        json={
            "username": username,
            "email": email,
            "password": password
        }
    )

    st.write(
        response.json()
    )
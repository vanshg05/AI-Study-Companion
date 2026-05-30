import streamlit as st # type: ignore
import requests # type: ignore

API_URL = "http://127.0.0.1:8000"

st.title(
    "Login"
)

username = st.text_input(
    "Username"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    response = requests.post(
        f"{API_URL}/login",
        json={
            "username": username,
            "password": password
        }
    )

    data = response.json()

    if "access_token" in data:

        st.session_state.token = data[
            "access_token"
        ]

        st.success(
            "Login successful"
        )

        st.switch_page(
            "streamlit_app.py"
        )

    else:

        st.error(
            "Invalid credentials"
        )
import streamlit as st # type: ignore
import requests # type: ignore

API_URL = "http://127.0.0.1:8000"


def show_auth():

    st.title("🔐 AI Study Companion")

    login_tab, register_tab = st.tabs(
        ["Login", "Register"]
    )

    with login_tab:

        username = st.text_input(
            "Username",
            key="login_user"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_pass"
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

                st.session_state.logged_in = True

                st.session_state.username = (
                    username
                )

                st.success(
                    "Login Successful"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid Credentials"
                )

    with register_tab:

        username = st.text_input(
            "Username",
            key="reg_user"
        )

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="reg_pass"
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

            st.write(response.json())
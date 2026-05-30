import streamlit as st # type: ignore


def show_sidebar():

    with st.sidebar:

        st.title(
            "📚 AI Study Companion"
        )

        st.success(
            "🟢 Logged In"
        )

        st.markdown("---")

        st.write(
            "Powered by Llama 3.2"
        )

        st.markdown("---")

        if st.button("Logout"):

            st.session_state.clear()

            st.rerun()
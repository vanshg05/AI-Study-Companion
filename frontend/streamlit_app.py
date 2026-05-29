import streamlit as st # type: ignore

# if "token" not in st.session_state:

#     st.warning(
#         "Please login first"
#     )

#     st.stop()

if st.sidebar.button("Logout"):

    del st.session_state["token"]

    st.rerun()
    
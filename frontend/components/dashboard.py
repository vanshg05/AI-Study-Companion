import streamlit as st # type: ignore


def show_dashboard():

    st.header("🏠 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Questions",
        st.session_state.questions_count
    )

    col2.metric(
        "Flashcards",
        st.session_state.flashcard_count
    )

    col3.metric(
        "Code Reviews",
        st.session_state.code_reviews
    )

    col4.metric(
        "Quiz Attempts",
        st.session_state.quiz_attempts
    )
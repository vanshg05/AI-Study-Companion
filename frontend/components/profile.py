import streamlit as st # type: ignore


def show_profile():

    st.header("👤 Profile")

    st.metric(
        "Questions",
        st.session_state.questions_count
    )

    st.metric(
        "Flashcards",
        st.session_state.flashcard_count
    )

    st.metric(
        "Code Reviews",
        st.session_state.code_reviews
    )

    st.metric(
        "Quiz Attempts",
        st.session_state.quiz_attempts
    )

    if st.session_state.quiz_score:

        st.metric(
            "Latest Quiz Score",
            st.session_state.quiz_score
        )
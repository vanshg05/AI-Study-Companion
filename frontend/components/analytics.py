import streamlit as st # type: ignore
import pandas as pd # type: ignore
import plotly.express as px # type: ignore


def show_analytics():

    st.header("📊 Analytics")

    data = pd.DataFrame(
        {
            "Activity":[
                "Questions",
                "Flashcards",
                "Code Reviews",
                "Quiz Attempts"
            ],
            "Count":[
                st.session_state.questions_count,
                st.session_state.flashcard_count,
                st.session_state.code_reviews,
                st.session_state.quiz_attempts
            ]
        }
    )

    fig = px.bar(
        data,
        x="Activity",
        y="Count"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
import streamlit as st # type: ignore
import pandas as pd # type: ignore
import plotly.express as px # type: ignore

from backend.database.db import (
    SessionLocal
)

from backend.services.analytics_service import (
    get_user_stats
)


def show_analytics():

    st.header("📊 Analytics")

    db = SessionLocal()

    stats = get_user_stats(
        db,
        st.session_state.username
    )

    db.close()

    data = pd.DataFrame(
        {
            "Activity":[
                "Questions",
                "Flashcards",
                "Summaries",
                "Quizzes",
                "Code Reviews"
            ],
            "Count":[
                stats["QUESTION_ASKED"],
                stats["FLASHCARD"],
                stats["SUMMARY"],
                stats["QUIZ"],
                stats["CODE_REVIEW"]
            ]
        }
    )

    fig = px.bar(
        data,
        x="Activity",
        y="Count",
        title="User Activity Analytics"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
import streamlit as st # type: ignore

from backend.database.db import (
    SessionLocal
)

from backend.database.models import (
    Activity
)


def show_history():

    st.header(
        "📜 Activity History"
    )

    db = SessionLocal()

    activities = db.query(
        Activity
    ).filter(
        Activity.username ==
        st.session_state.username
    ).all()

    db.close()

    if len(activities) == 0:

        st.info(
            "No activity yet."
        )

        return

    for activity in reversed(
        activities
    ):

        st.write(
            f"{activity.created_at} — {activity.activity_type}"
        )
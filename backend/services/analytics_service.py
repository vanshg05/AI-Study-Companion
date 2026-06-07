from backend.database.models import (
    Activity
)


def get_user_stats(
    db,
    username
):

    activities = db.query(
        Activity
    ).filter(
        Activity.username == username
    ).all()

    stats = {
        "QUESTION_ASKED": 0,
        "FLASHCARD": 0,
        "SUMMARY": 0,
        "QUIZ": 0,
        "CODE_REVIEW": 0
    }

    for activity in activities:

        if activity.activity_type in stats:

            stats[
                activity.activity_type
            ] += 1

    return stats
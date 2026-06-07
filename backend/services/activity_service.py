from backend.database.models import Activity


def log_activity(
    db,
    username,
    activity_type
):

    activity = Activity(
        username=username,
        activity_type=activity_type
    )

    db.add(activity)

    db.commit()
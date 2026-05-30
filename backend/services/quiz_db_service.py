from backend.database.models import QuizAttempt

def save_quiz_result(
    db,
    username,
    score,
    total_questions
):

    attempt = QuizAttempt(
        username=username,
        score=score,
        total_questions=total_questions
    )

    db.add(attempt)

    db.commit()
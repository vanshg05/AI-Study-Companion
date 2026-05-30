import streamlit as st # type: ignore


def show_quiz():

    st.header(
        "📝 Interactive Quiz"
    )

    if "quiz_questions" not in st.session_state:

        st.info(
            "Generate a quiz first."
        )

        return

    if len(st.session_state.quiz_questions) == 0:

        st.info(
            "Generate a quiz first."
        )

        return

    answers = {}

    total_questions = len(
        st.session_state.quiz_questions
    )

    for idx, question in enumerate(
        st.session_state.quiz_questions
    ):

        st.subheader(
            f"Question {idx + 1}"
        )

        st.write(
            question["question"]
        )

        selected = st.radio(
            "Choose Answer",
            question["options"],
            index=None,
            key=f"question_{idx}"
        )

        answers[idx] = selected

        st.markdown("---")

    if st.button(
        "Submit Quiz"
    ):

        unanswered = []

        score = 0

        for idx in range(total_questions):

            if st.session_state.get(
                f"question_{idx}"
            ) is None:

                unanswered.append(idx + 1)

        if unanswered:

            st.error(
                f"Please answer all questions. Missing: {unanswered}"
            )

            return

        for idx, question in enumerate(
            st.session_state.quiz_questions
        ):

            answer_index = question.get(
                "answer",
                0
            )

            options = question.get(
                "options",
                []
            )

            if answer_index >= len(options):

                st.warning(
                    f"Skipping invalid question {idx+1}"
                )

                continue

            correct_option = options[
                answer_index
            ]

            if answers[idx] == correct_option:

                score += 1

        st.session_state.quiz_score = score

        st.session_state.quiz_attempts += 1

        st.success(
            f"Your Score: {score}/{total_questions}"
        )

        st.metric(
            "Percentage",
            f"{(score/total_questions)*100:.2f}%"
        )

        st.balloons()

        with st.expander(
            "View Correct Answers"
        ):

            for idx, question in enumerate(
                st.session_state.quiz_questions
            ):

                st.write(
                    f"Q{idx+1}: {question['question']}"
                )

                st.success(
                    f"Correct Answer: {question['options'][question['answer']]}"
                )
import streamlit as st # type: ignore
import os

from backend.pdf_processor import extract_text
from backend.vector_store import store_document
from backend.rag_engine import answer_question
from backend.services.flashcard_generator import (
    generate_flashcards
)
from backend.services.summary_generator import (
    generate_summary
)
from backend.services.quiz_service import (
    generate_quiz
)


def show_study_assistant(project_root):

    st.header(
        "Study Assistant"
    )

    uploaded_files = st.file_uploader(
        "Upload PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        for uploaded_file in uploaded_files:

            upload_folder = os.path.join(
                project_root,
                "uploads"
            )

            os.makedirs(
                upload_folder,
                exist_ok=True
            )

            save_path = os.path.join(
                upload_folder,
                uploaded_file.name
            )

            with open(save_path, "wb") as f:

                f.write(
                    uploaded_file.getbuffer()
                )

            text = extract_text(
                save_path
            )

            store_document(text)

            st.session_state.document_text += (
                "\n" + text
            )

        st.success(
            "Documents Processed"
        )

    question = st.text_input(
        "Ask a Question"
    )

    if st.button("Ask"):

        answer = answer_question(
            question
        )

        st.session_state.questions_count += 1

        st.session_state.chat_history.append(
            {
                "question": question,
                "answer": answer
            }
        )

    for chat in reversed(
        st.session_state.chat_history
    ):

        with st.chat_message("user"):
            st.write(chat["question"])

        with st.chat_message("assistant"):
            st.write(chat["answer"])

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("Generate Flashcards"):

            flashcards = generate_flashcards(
                st.session_state.document_text
            )

            st.session_state.flashcard_count += 1

            st.write(flashcards)

    with col2:

        if st.button("Generate Summary"):

            summary = generate_summary(
                st.session_state.document_text
            )

            st.write(summary)

    with col3:

        if st.button("Generate Quiz"):

            if st.session_state.document_text:

                quiz_questions = generate_quiz(
                    st.session_state.document_text
                )

                if len(quiz_questions) > 0:

                    st.session_state.quiz_questions = (
                        quiz_questions
                    )

                    # Clear old quiz answers
                    for key in list(st.session_state.keys()):

                        if key.startswith("question_"):

                            del st.session_state[key]

                    st.success(
                        f"Quiz Generated Successfully ({len(quiz_questions)} Questions)"
                    )

                    st.info(
                        "Open the Quiz tab to attempt the quiz."
                    )

                else:

                    st.error(
                        "Failed to generate quiz."
                    )

            else:

                st.warning(
                    "Upload a PDF first."
                )
import streamlit as st # type: ignore
import requests # type: ignore
import os
import sys
import pandas as pd # type: ignore
import plotly.express as px # type: ignore

# ==========================
# PATH SETUP
# ==========================

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)

from backend.pdf_processor import extract_text
from backend.vector_store import store_document
from backend.rag_engine import answer_question
from backend.flashcard_generator import generate_flashcards
from backend.quiz_generator import generate_quiz
from backend.summary_generator import generate_summary
from backend.code_assistant import (
    explain_code,
    detect_bugs,
    optimize_code
)

# ==========================
# CONFIG
# ==========================

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Study Companion",
    layout="wide"
)

# ==========================
# SESSION STATE
# ==========================

if "token" not in st.session_state:
    st.session_state.token = None

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "questions_count" not in st.session_state:
    st.session_state.questions_count = 0

if "flashcard_count" not in st.session_state:
    st.session_state.flashcard_count = 0

if "code_reviews" not in st.session_state:
    st.session_state.code_reviews = 0

# ==========================
# LOGIN SCREEN
# ==========================

if not st.session_state.logged_in:

    st.title("🔐 AI Study Companion")

    auth_tab1, auth_tab2 = st.tabs(
        ["Login", "Register"]
    )

    # LOGIN
    with auth_tab1:

        username = st.text_input(
            "Username",
            key="login_user"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_pass"
        )

        if st.button("Login"):

            response = requests.post(
                f"{API_URL}/login",
                json={
                    "username": username,
                    "password": password
                }
            )

            data = response.json()

            if "access_token" in data:

                st.session_state.token = data[
                    "access_token"
                ]

                st.session_state.logged_in = True

                st.success(
                    "Login Successful"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid Credentials"
                )

    # REGISTER
    with auth_tab2:

        reg_user = st.text_input(
            "Username",
            key="reg_user"
        )

        reg_email = st.text_input(
            "Email"
        )

        reg_pass = st.text_input(
            "Password",
            type="password",
            key="reg_pass"
        )

        if st.button("Register"):

            response = requests.post(
                f"{API_URL}/register",
                json={
                    "username": reg_user,
                    "email": reg_email,
                    "password": reg_pass
                }
            )

            st.write(
                response.json()
            )

    st.stop()

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.title(
        "📚 AI Study Companion"
    )

    st.success(
        "🟢 Logged In"
    )

    st.markdown("---")

    st.write(
        "Powered by Llama 3.2"
    )

    st.markdown("---")

    if st.button("Logout"):

        st.session_state.clear()

        st.rerun()

# ==========================
# MAIN TABS
# ==========================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📖 Study Assistant",
        "💻 Code Assistant",
        "📊 Analytics",
        "👤 Profile"
    ]
)

# ===================================================
# STUDY ASSISTANT
# ===================================================

with tab1:

    st.header(
        "Study Assistant"
    )

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

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

        st.session_state.document_text = text

        store_document(text)

        st.success(
            "PDF Processed Successfully"
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

            st.write(
                chat["question"]
            )

        with st.chat_message("assistant"):

            st.write(
                chat["answer"]
            )

    if st.button(
        "Generate Flashcards"
    ):

        flashcards = generate_flashcards(
            st.session_state.document_text
        )

        st.session_state.flashcard_count += 1

        st.subheader(
            "Flashcards"
        )

        st.write(flashcards)

    # Quiz Generator
    if st.button("Generate Quiz"):

        quiz = generate_quiz(text)

        st.subheader("Quiz")

        st.write(quiz)

    # Summary Generator
    if st.button("Generate Summary"):

        summary = generate_summary(text)

        st.subheader("Summary")

        st.write(summary)

# ===================================================
# CODE ASSISTANT
# ===================================================

with tab2:

    st.header(
        "Code Assistant"
    )

    uploaded_code = st.file_uploader(
        "Upload Code",
        type=[
            "py",
            "java",
            "cpp"
        ]
    )

    if uploaded_code:

        code = uploaded_code.read().decode(
            "utf-8",
            errors="ignore"
        )

        st.code(code)

        action = st.selectbox(
            "Select Analysis",
            [
                "Explain Code",
                "Detect Bugs",
                "Optimize Code"
            ]
        )

        if st.button(
            "Analyze Code"
        ):

            if action == "Explain Code":

                result = explain_code(
                    code
                )

            elif action == "Detect Bugs":

                result = detect_bugs(
                    code
                )

            else:

                result = optimize_code(
                    code
                )

            st.session_state.code_reviews += 1

            st.write(result)

# ===================================================
# ANALYTICS
# ===================================================

with tab3:

    st.header(
        "Analytics Dashboard"
    )

    data = pd.DataFrame(
        {
            "Activity":[
                "Questions",
                "Flashcards",
                "Code Reviews"
            ],
            "Count":[
                st.session_state.questions_count,
                st.session_state.flashcard_count,
                st.session_state.code_reviews
            ]
        }
    )

    fig = px.bar(
        data,
        x="Activity",
        y="Count",
        title="Usage Statistics"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ===================================================
# PROFILE
# ===================================================

with tab4:

    st.header(
        "Profile"
    )

    st.metric(
        "Questions Asked",
        st.session_state.questions_count
    )

    st.metric(
        "Flashcards Generated",
        st.session_state.flashcard_count
    )

    st.metric(
        "Code Reviews",
        st.session_state.code_reviews
    )

    st.success(
        "Account Active"
    )
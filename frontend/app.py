import streamlit as st # type: ignore
import os
import sys

# ==========================
# PATH SETUP
# ==========================

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ==========================
# IMPORT COMPONENTS
# ==========================

from frontend.components.auth import show_auth
from frontend.components.sidebar import show_sidebar
from frontend.components.dashboard import show_dashboard
from frontend.components.study_assistant import (
    show_study_assistant
)
from frontend.components.code_assistant import (
    show_code_assistant
)
from frontend.components.quiz import (
    show_quiz
)
from frontend.components.analytics import (
    show_analytics
)
from frontend.components.profile import (
    show_profile
)
from frontend.components.history import (
    show_history
)

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="AI Study Companion",
    page_icon="📚",
    layout="wide"
)

# ==========================
# SESSION STATE INIT
# ==========================

defaults = {
    "token": None,
    "logged_in": False,
    "chat_history": [],
    "document_text": "",
    "questions_count": 0,
    "flashcard_count": 0,
    "code_reviews": 0,
    "quiz_generated": "",
    "quiz_score": None,
    "quiz_attempts": 0
}

for key, value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value

if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = []

if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}

# ==========================
# AUTHENTICATION
# ==========================

if not st.session_state.logged_in:

    show_auth()

    st.stop()

if "username" not in st.session_state:
    st.session_state.username = ""

# ==========================
# SIDEBAR
# ==========================

show_sidebar()

# ==========================
# HEADER
# ==========================

st.title(
    "📚 AI Study Companion & Code Review Platform"
)

st.caption(
    "Powered by FastAPI • SQLite • ChromaDB • Ollama • Llama 3.2"
)

# ==========================
# TABS
# ==========================

tab0, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "🏠 Dashboard",
        "📖 Study Assistant",
        "💻 Code Assistant",
        "📝 Quiz",
        "📊 Analytics",
        "👤 Profile",
        "📜 History"
    ]
)

# ==========================
# DASHBOARD
# ==========================

with tab0:

    show_dashboard()

# ==========================
# STUDY ASSISTANT
# ==========================

with tab1:

    show_study_assistant(
        PROJECT_ROOT
    )

# ==========================
# CODE ASSISTANT
# ==========================

with tab2:

    show_code_assistant()

# ==========================
# QUIZ
# ==========================

with tab3:

    show_quiz()

# ==========================
# ANALYTICS
# ==========================

with tab4:

    show_analytics()

# ==========================
# PROFILE
# ==========================

with tab5:

    show_profile()

# ==========================
# HISTORY
# ==========================

with tab6:

    show_history()
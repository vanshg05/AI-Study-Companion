import streamlit as st # type: ignore

from backend.code_assistant import (
    explain_code,
    detect_bugs,
    optimize_code,
    analyze_complexity
)


def show_code_assistant():

    st.header("💻 Code Assistant")

    uploaded_code = st.file_uploader(
        "Upload Code",
        type=["py", "java", "cpp"]
    )

    if uploaded_code:

        code = uploaded_code.read().decode(
            "utf-8",
            errors="ignore"
        )

        st.code(code)

        action = st.selectbox(
            "Analysis Type",
            [
                "Explain Code",
                "Detect Bugs",
                "Optimize Code",
                "Complexity Analysis"
            ]
        )

        if st.button("Analyze"):

            if action == "Explain Code":

                result = explain_code(code)

            elif action == "Detect Bugs":

                result = detect_bugs(code)

            elif action == "Optimize Code":

                result = optimize_code(code)

            else:

                result = analyze_complexity(
                    code
                )

            st.session_state.code_reviews += 1

            st.write(result)
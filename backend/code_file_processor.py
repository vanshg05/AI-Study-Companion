def read_code_file(uploaded_file):

    return uploaded_file.read().decode(
        "utf-8",
        errors="ignore"
    )
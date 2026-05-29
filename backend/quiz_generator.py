from backend.llama_helper import ask_llama

def generate_quiz(context):

    prompt = f"""
    Generate 10 multiple choice questions.

    Include:
    - Question
    - 4 options
    - Correct answer

    Context:
    {context[:5000]}
    """

    return ask_llama(prompt)
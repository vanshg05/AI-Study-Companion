from backend.llama_helper import ask_llama

def generate_summary(text):

    prompt = f"""
    Summarize the following document.

    Focus on:
    - Main topics
    - Important concepts
    - Key takeaways

    Document:
    {text[:5000]}
    """

    return ask_llama(prompt)
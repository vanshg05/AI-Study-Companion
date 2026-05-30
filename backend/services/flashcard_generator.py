from backend.llama_helper import ask_llama

def generate_flashcards(context):

    prompt = f"""
Create study flashcards from the provided content.

Format:

Flashcard 1
Q: ...
A: ...

Flashcard 2
Q: ...
A: ...

Generate 10 flashcards.

Content:
{context[:6000]}
"""

    return ask_llama(prompt)
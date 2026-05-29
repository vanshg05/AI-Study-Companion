from backend.llama_helper import ask_llama
from backend.vector_store import retrieve_context

def answer_question(question):

    context = retrieve_context(question)

    prompt = f"""
You are a study assistant.

Use ONLY the provided context.

If the answer is not present,
say:

"I could not find that information in the uploaded document."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    return ask_llama(prompt)
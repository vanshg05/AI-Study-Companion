from backend.llama_helper import ask_llama
import json


def generate_quiz(document_text):

    prompt = f"""
Generate EXACTLY 10 MCQs.

Return ONLY a JSON array.

Example:

[
  {{
    "question":"What is HTML?",
    "options":[
      "Markup Language",
      "Database",
      "Operating System",
      "Compiler"
    ],
    "answer":0
  }},
  {{
    "question":"What is CSS?",
    "options":[
      "Style Sheet",
      "Database",
      "Language",
      "Browser"
    ],
    "answer":0
  }}
]

Document:

{document_text[:4000]}
"""

    response = ask_llama(prompt)

    print(response)

    try:

        start = response.find("[")

        end = response.rfind("]") + 1

        json_text = response[start:end]

        cleaned_questions = []

        quiz_data = json.loads(json_text)

        for q in quiz_data:

            if (
                "question" in q
                and "options" in q
                and "answer" in q
            ):

                if len(q["options"]) == 4:

                    if 0 <= q["answer"] <= 3:

                        cleaned_questions.append(q)

        return cleaned_questions

    except Exception as e:

        print(e)

        return []
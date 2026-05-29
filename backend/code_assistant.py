from backend.llama_helper import ask_llama


def explain_code(code):

    prompt = f"""
Explain this code in detail.

Include:
1. Purpose
2. How it works
3. Important functions
4. Inputs and outputs

Code:
{code}
"""

    return ask_llama(prompt)


def detect_bugs(code):

    prompt = f"""
Find bugs in this code.

Include:
1. Logical bugs
2. Runtime issues
3. Edge cases
4. Suggested fixes

Code:
{code}
"""

    return ask_llama(prompt)


def optimize_code(code):

    prompt = f"""
Optimize this code.

Include:
1. Performance improvements
2. Cleaner code
3. Better practices

Code:
{code}
"""

    return ask_llama(prompt)
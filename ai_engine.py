import ollama

def analyze_code(code, vulnerability):

    print("Calling DeepSeek...")

    prompt = f"""
You are a cybersecurity expert.

Code:

{code}

Detected vulnerability:

{vulnerability}

Explain:

1. Why this is dangerous.
2. Severity.
3. How to fix it.
4. Give secure code example.

Keep answer concise.
"""

    response = ollama.chat(

        model="deepseek-coder",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("DeepSeek replied!")

    return response["message"]["content"]
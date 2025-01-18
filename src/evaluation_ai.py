import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def evaluate_interview_answer(answer):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Evaluează răspunsul unui candidat la un interviu de medicină."},
            {"role": "user", "content": answer}
        ]
    )
    return response["choices"][0]["message"]["content"]

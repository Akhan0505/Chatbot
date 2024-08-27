from groq import Groq



# Initialize the Groq client
client = Groq(api_key="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")
completion = client.chat.completions.create(
    model="gemma2-9b-it",
    messages=[
        {
            "role": "user",
            "content": "Hi tell me about new AI tools"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
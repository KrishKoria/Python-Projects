import openai

openai.api_key = "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"


def chat_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=1,
    )

    message = response.choices[0].text.strip()
    return message


user_prompt = input("Enter Your Prompt :- ")
bot_response = chat_with_chatgpt(prompt=user_prompt)
print(bot_response)

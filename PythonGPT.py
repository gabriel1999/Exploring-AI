import openai

openai.api_key = "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"

messages = []
messages.append({"role": "system", "content": "Basic GPT."})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
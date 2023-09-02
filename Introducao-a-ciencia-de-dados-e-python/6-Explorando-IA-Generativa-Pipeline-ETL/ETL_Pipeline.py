import openai

api_key = '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'
openai.api_key = api_key

def chat_with_gpt(prompt, conversation=[]):
    conversation.append({"role": "system", "content": "Você é um assistente de bate-papo."})
    conversation.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    reply = response['choices'][0]['message']['content']
    return reply, conversation

conversation = []

print("Bem-vindo ao ChatGPT! Digite 'sair' para encerrar a conversa.")

while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        break

    reply, conversation = chat_with_gpt(user_input, conversation)
    print("ChatGPT:", reply)





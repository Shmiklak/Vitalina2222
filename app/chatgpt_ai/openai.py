from dotenv import load_dotenv
import asyncio
from openai import AsyncOpenAI
import os

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv('OPENAI_TOKEN'),
    # base_url=os.getenv('OPENAI_URL')
)

with open('vitalina.txt', encoding = 'utf-8', mode = 'r') as file:
    vitalina = file.read()


vitalina_history = []

async def chatgpt_response(prompt):
    print("Начинаю генерировать ответ...")


    if len(vitalina_history) == 10:
        vitalina_history.pop(0)

    vitalina_history.append({
        "role": "user",
        "content": prompt,
        "name": "users"
    })

    messages_to_send = [{"role": "system","content": vitalina,"name": "System"}] + vitalina_history

    response = await client.chat.completions.create(
        messages=messages_to_send,
        model="gpt-3.5-turbo",
        max_tokens=150,
        temperature=0.4
    )

    print(response)

    vitalina_history.append({
        "role": "assistant",
        "content": response.choices[0].message.content,
        "name": "Vitalina2222"
    })

    return response.choices[0].message.content + "<:pepeBusiness:1036987708456845391>"
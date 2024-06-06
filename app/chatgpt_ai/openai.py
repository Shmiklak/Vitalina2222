from dotenv import load_dotenv
from openai import AsyncOpenAI
import os

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv('OPENAI_TOKEN'),
    # base_url=os.getenv('OPENAI_URL')
)

with open('vitalina.txt', encoding = 'utf-8', mode = 'r') as file:
    vitalina = file.read()

with open('vitalina_en.txt', encoding = 'utf-8', mode = 'r') as file:
    vitalina_en = file.read()

vitalina_history = []

async def chatgpt_response(prompt, force_english=False):
    
    global vitalina_history

    if (prompt == "MARVOLLO_HISTORY"):
        return vitalina_history
    
    if (prompt == "MARVOLLO_RESET"):
        vitalina_history = []
        return vitalina_history

    print("Начинаю генерировать ответ...")


    if len(vitalina_history) == 10:
        vitalina_history.pop(0)

    vitalina_history.append({
        "role": "user",
        "content": prompt,
        "name": "users"
    })

    if force_english:
        messages_to_send = [{"role": "system","content": vitalina_en,"name": "System"}] + vitalina_history
    else:
        messages_to_send = [{"role": "system","content": vitalina,"name": "System"}] + vitalina_history

    response = await client.chat.completions.create(
        messages=messages_to_send,
        model="gpt-3.5-turbo",
        max_tokens=300,
        temperature=0.4
    )

    print(response)

    vitalina_history.append({
        "role": "assistant",
        "content": response.choices[0].message.content,
        "name": "Vitalina2222"
    })

    return response.choices[0].message.content + "<:pepeBusiness:1036987708456845391>"
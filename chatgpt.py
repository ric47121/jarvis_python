# https://www.youtube.com/watch?v=b8COygWdvmw&ab_channel=MoureDevbyBraisMoure
# https://github.com/openai/openai-python
# https://platform.openai.com/docs/api-reference/authentication

# pip install openai

import openai
import config

openai.api_key = config.api_key

# contaxto
messages = [{"role":"system", "content": "eres un asistente de viajes"}]

content = input('de que quieres hablar?')
messages.append({"role":"user", "content": content})

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                             messages=messages)

# guardo respuesta
messages.append({"role":"assistant", "content": response})

print(response.choices[0].message.conetnt)



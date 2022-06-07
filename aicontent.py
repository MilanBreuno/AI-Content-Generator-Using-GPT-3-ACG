import os
from urllib import response 
import openai
import config 
openai.api_key = config.OPENAI_API_KEY

def aicontent(query):
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt="Generate a detailed product description for:{}".format(query),
        temperature=0.8,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    
    if 'choices' in response:
        if len(response['choices']) >0:
             answer = response['choices'][0]['text']
        else:
            answer = 'Ugh oh ! i accept i fail !'
    return answer

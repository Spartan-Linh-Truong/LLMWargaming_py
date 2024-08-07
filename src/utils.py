import openai
import os
from datetime import date
from openai import OpenAI
from omegaconf import OmegaConf

class ChatSetup:
    def __init__(self, secret_key, model, use_dummygpt):
        self.secret_key = secret_key
        self.model = model
        self.use_dummygpt = use_dummygpt
        self.client = OpenAI(
            # This is the default and can be omitted
            api_key=secret_key,
        )
    def chat(self, chat_hist, prompt):
        chat_hist.append({"role": "user", "content": prompt})
        if self.use_dummygpt:
            message = OmegaConf.create({"role": "ROLE", "content": "CONTENT"})
        else:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=chat_hist
            )
            message = response.choices[0].message
        chat_hist.append({"role": message.role, "content": message.content})

def readfile(dir, filename):
    with open(os.path.join(dir, filename), 'r') as f:
        s = f.read()
    return s

def create_file_ending(dir):
    tod = str(date.today())
    file_ind = len([e for e in os.listdir(dir) if tod in e])
    return f"{tod}_{file_ind}"

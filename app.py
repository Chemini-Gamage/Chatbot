from openai import OpenAI
# since you work with env variables
import os
from dotenv import load_dotenv
# to use the env variables
load_dotenv()
# print(os.environ["OPENAI_API_KEY"])
OPENAI_API_KEY =os.environ["OPENAI_API_KEY"]
#object creation
client=OpenAI()
#client is used to give a question and to generate the ans
client.chat.completions.create(
    model ="gpt-3.5-turbo", 
    max_tokens =50,
    n=1,
    temperature=0,
    #cn assign roles here
    messages =[
        {"role":"user", "content":"Hello"}
    ]
)
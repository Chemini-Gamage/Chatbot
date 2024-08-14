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
#to take the user input
#while to iterate
while True:

    question =input("User:")

    if question != "bye":
     response =client.chat.completions.create(
        model ="gpt-3.5-turbo", 
    #to tell the number of tokens which cn be recieved is 50 tokens here
        max_tokens =50,
    #number of responses received is "n"
        n=1,
    #temperature to measure the randomeness of the response
        temperature=0.3,
    #cn assign roles here
        messages =[
        {"role":"user", "content":question}
    ]
)
#cn have multiple responses
    for choice in response.choices:
         print(f"AI: {choice.message.content}")

               
    else:
      print("AI :Bye")
      break             
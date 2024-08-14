from openai import OpenAI
# since you work with env variables
import os
from dotenv import load_dotenv
# to use the env variables
load_dotenv()
print(os.environ["OPENAI_API_KEY"])
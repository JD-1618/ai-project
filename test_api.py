import os 
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model=os.getenv("MODEL_NAME"),
    messages=[{"role":"user", "content":"Say 'JD's MEDAI is live!' in 5 words."}])
print(response.choices[0].message.content)

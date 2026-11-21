import os
from dotenv import load_dotenv
#1. Load variables from the .env file into memory
load_dotenv()
#2. Read each variable using os.getenv()
app_name = os.getenv("APP_NAME")
model_name = os.getenv("MODEL_NAME")
temperature = float(os.getenv("TEMPERATURE"))
debug = os.getenv("DEBUG") == "True"
print(f"App:{app_name} | model: {model_name}")
print(f"Temperature:{temperature} | Debug mode:{debug}")


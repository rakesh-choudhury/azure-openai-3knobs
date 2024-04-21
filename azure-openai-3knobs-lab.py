import os
from openai import AzureOpenAI
from datetime import datetime

# TODO: CONFIGURE ENVIRONMENT for PYTHON:
# 1. create empty folder, cd into it
# 2. create and activate isolated python environment:
#       python3 -m venv .
#       source bin/activate
# 3. install needed Azure OpenAI packages:
#       pip3 install openai
# 4. copy this file into that folder - hello-ai.py
# 5. run the app:
#       python3 hello-ai.py
# 6. then diagnose and solve the problem of the AI is not responding as instructed
#       see below for the challenge details (search for string "KNOB")
# DO NOT DO THIS IN REAL CODE! Keys do not belong in source code.
# this is a certified TERRIBLE IDEA (tm) - but makes mini-workshop possible
# key will be rolled (invalidated) right after this mini-workshop


# KNOB 0: MODEL CHOICE (we do not have ability to alter the model in this lab)
deployment = "xxxxxxxxxxxxxxxxxxx" # get your deployment environment from azure
client = AzureOpenAI(
   api_key="xxxxxxxxxxxxxxxxxxxx", # get the azure-openai api key
   api_version="2024-02-01",
   azure_endpoint = "xxxxxxxxxxxxxxxxxx" #get the azure end point assigned to you
)
import datetime
print("\n----------------- DEBUG INFO -----------------")
doy = datetime.datetime.now().strftime("%B %d")
year = datetime.datetime.now().year
today = datetime.datetime.now().strftime("%A, %B %d, %Y")
# get January or February or whatever month we are in today
month = datetime.datetime.now().strftime("%B")
print(f"Today is {today} @ {datetime.datetime.now().strftime('%I:%M:%S %p')}")
print("----------------------------------------------")

years_back = 25
# range = f"within the past {years_back} years"
range = f"since the year {year-years_back}"

# KNOB 1: PROMPT ENGINEERING - does the AI respond accurately to this prompt? How to fix?
prompt = (
    f"Today is {today}. \n"
    f"Summarize an interesting and upbeat historical event "
    # f"that took place in the current month. \n"
    f"that took place in the current month {range}. \n"
    # f"that took place in the month of {month}. \n"
    # f"that took place in the month of {month} {range}. \n"
    f"Be sure to include the specific historical date. \n"
)

#### KNOB 2: TOKEN COUNT # PLEASE DON'T MAKE LARGER THAN 500 (but see what happens at 25)
max_tokens = 100

if (max_tokens > 500):
    print(f"WARNING: max_tokens is set to {max_tokens}. Please don't make this larger than 500.")
    max_tokens = 500

print(f"PROMPT: \n\n{prompt}")

#### KNOB 3: TEMPERATURE (0.0 to 1.0) - how creative should the AI be? 1.0 is most creative. 0.0 is most factual.
temperature = 0.1  # Set your desired temperature here
response = client.completions.create(model=deployment, prompt=prompt, max_tokens=max_tokens, temperature=temperature)

print(f"\nRESPONSE: {response.choices[0].text}")
print(f"----------------- DEBUG INFO -----------------")
print(f"Tokens used: {response.usage.completion_tokens}/{max_tokens}")
print(f"----------------------------------------------");
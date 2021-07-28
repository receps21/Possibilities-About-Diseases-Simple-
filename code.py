import os
import openai
import json
import sys

openai.api_key = '<API-KEY>'
start_sequence = "\nPossibilities about Diseases"
restart_sequence = "Symptoms:"
Symptoms = "I have neckpain and tinnitus" #@param {type:"string"}
prompt = "I am a specialist who diagnosis the disease, please tell me your pain."+"""
Symptoms: I have blood on my feces.
Possibilities about Diseases: Colon cancer, Hemorrhoid, Large intestine polyps, Rectual cancer, Irritable bowel syndrome, Anal fissure.
Symptoms: I have numbness in my fingers.
Possibilities about Diseases: Carpal tunnel syndrome, Cervical spondylosis, Cubital tunnel syndrome, degenerative disc disease, Peripheral neuropathy, Rheumatoid arthritis.
Symptoms:"""+Symptoms+'\n'
response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  temperature=0.3,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.05,
  presence_penalty=0.06,
  stop=["\n"]
)
## print(response)
jsonType = json.loads(response.last_response.body)
print(jsonType['choices'][0]['text'])

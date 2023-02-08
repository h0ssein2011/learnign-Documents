import openai

with open('./API_Key.txt','r') as f:
    API_KEY = f.read()

with open('./question.txt','r') as f:
    question = f.read()

API_KEY = API_KEY
openai.api_key = API_KEY

# create a completion
completion = openai.Completion.create(engine="text-davinci-003", prompt=question)

# print the completion
print(completion.choices[0].text)
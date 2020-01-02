from sys import argv

script,user_name = argv

prompt = ">"

print("Hi {user_name} I am the {script} script")
print("I would like ask you a few questions:")
print(f"Do you like me {user_name}")

likes =input(prompt)

print(f"where do you live {user_name}")

lives=input(prompt)

print("what kind of computer do you have?")
computers=input(prompt)

print(f"""
Alright so you said {likes} about me
you live in {lives}.Not sure about this
and you have a {computers} computer
""")

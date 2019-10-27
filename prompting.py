from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name} I'm the {script} script")
print(f"I am going to ask you some questions")

print(f"Do you like me?")
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print(f"What computer do you have?")
computer = input(prompt)

print(f""" 
Alrightm so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice
""")

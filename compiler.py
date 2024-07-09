from setup import run_jia 
import os

while True:
    user_input = input("Jia> ")
    if user_input.lower() == "jia":
        print("Welcome to Jia! Type 'exit' to quit.\n")
        run_jia()
    elif list(user_input.split(" "))[0].lower() == "run" and len(list(user_input.split(" "))) == 2:
        print(list(user_input.split(" ")))


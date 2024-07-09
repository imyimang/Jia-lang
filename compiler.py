from setup import run_jia 
import os

while True:
    user_input = input("Jia> ")
    if user_input.lower() == "jia":
        print("Welcome to Jia! Type 'exit' to quit.\n")
        run_jia()

    elif list(user_input.split(" "))[0].lower() == "run" and len(list(user_input.split(" "))) == 2:
        inputs = list(user_input.split(" "))
        if os.path.exists(inputs[1]) and os.path.isfile(inputs[1]):
            root, extension = os.path.splitext(inputs[1])
            if extension == ".jia" or extension == ".txt":
                with open(inputs[1], "r", encoding='utf-8') as f:
                    content = f.read()
                run_jia(content)
            else:
                print("Error: Unknown file type(Only supports .txt and .jia)")    
        else:
            print("Error: Invalid file name")





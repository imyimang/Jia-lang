from repl import run_jia 
import os,re,sys

def edit_file(file_name):
    try:
        with open(file_name, "r+", encoding='utf-8') as f:
            print(f"Editing {file_name}, Press Ctrl+C to exit...\n")
            print(f.read(), end="")
            f.seek(0, 2)
            input_lines = []
            while True:
                line = sys.stdin.readline().rstrip('\n')
                if line == '':continue
                input_lines.append(line)
                
    except KeyboardInterrupt:
        with open(file_name, "r+", encoding='utf-8') as f:
            f.seek(0, 2) 
            for line in input_lines:
                f.write("\n" + line)
        print(f"\n\n...End editing {file_name}")


print("Welcome to Jia! Enter 'exit' to exit...")
while True:
    user_input = input("Jia> ")
    if user_input.lower() == "jia":
        print("Welcome to Jia REPL! Type 'exit' to quit.\n")
        run_jia("")
    
    elif user_input.lower() == "exit":
        print("Leaving Jia... hope to see you again")
        break

    elif list(user_input.split(" "))[0].lower() == "run" and len(list(user_input.split(" "))) == 2:
        inputs = list(user_input.split(" "))
        if (os.path.exists(inputs[1]) and os.path.isfile(inputs[1])):
            root, extension = os.path.splitext(inputs[1])
            if extension == ".jia" or extension == ".txt":
                with open(inputs[1], "r", encoding='utf-8') as f:
                    content = f.read()
                run_jia(content)
            else:
                print("Error: Unknown file type(Only supports .txt and .jia)")

        elif re.match(r"^[^.]*$", inputs[1]):
            if (os.path.exists(f"{inputs[1]}.jia") and os.path.isfile(f"{inputs[1]}.jia")):
                with open(f"{inputs[1]}.jia", "r", encoding='utf-8') as f:
                    content = f.read()
                run_jia(content)
            elif (os.path.exists(f"{inputs[1]}.txt") and os.path.isfile(f"{inputs[1]}.txt")):
                with open(f"{inputs[1]}.txt", "r", encoding='utf-8') as f:
                    content = f.read()
                run_jia(content)
        else:
            print("Error: Invalid file name")


    elif list(user_input.split(" "))[0].lower() == "edit" and len(list(user_input.split(" "))) == 2:
        inputs = list(user_input.split(" "))
        if re.match(r"[^\.]+\.(jia|txt)", inputs[1]):
            root, extension = os.path.splitext(inputs[1])
            edit_file(inputs[1])

        elif re.match(r"^[^.]*$", inputs[1]):
            edit_file(f"{inputs[1]}.jia")
        
        else:
            print("Error: Invalid file name")

    elif user_input.lower() == "help":
        print("jia                   open jia REPL")       
        print("run <file name>       run a .jia or .txt file") 
        print("edit <file name>      append a .jia or .txt file")

    else:
        print("Error: Invalid command")


    






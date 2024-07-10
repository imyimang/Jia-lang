from repl import run_jia 
import os,re,sys


def append_file(file_name):
    input_lines = []
    try:
        with open(file_name, "a+", encoding='utf-8') as f:
            print(f"Appending {file_name}, Press Ctrl+C to exit...\n")
            f.seek(0)
            print(f.read(), end="")
            while True:
                line = sys.stdin.readline().rstrip('\n')
                input_lines.append(line)
    except KeyboardInterrupt:
        with open(file_name, "a+", encoding='utf-8') as f:
            for line in input_lines:
                f.write(line + "\n")
        print(f"\n\n...End appending {file_name}")
    
def translate_file(file_name):
    print(f"Start translating Jia code to {file_name}(only supports ASCII 0~127), Press Ctrl+Z to exit:")
    user_input = sys.stdin.read()

    with open(file_name, "w", encoding='utf-8') as f:
        for char in user_input:
            ascii_value = ord(char)
            if ascii_value > 127:
                ascii_value = 63 
            code = "申" * ascii_value 
            f.write(code)
            f.write("由右\n") 
    print(f"...Conversion completed and saved to {file_name}")


print("Welcome to Jia! Enter 'exit' to exit...")
while True:
    user_input = input("Jia> ")
    if user_input.lower() == "jia":
        print("Welcome to Jia REPL! Type 'exit' to quit.\n")
        run_jia("")
    
    elif user_input.lower() == "exit":
        print("Leaving Jia... hope to see you again")
        break

    elif user_input.lower() == "help":
        print("jia                      open jia REPL")       
        print("run <file name>          run a .jia or .txt file") 
        print("append <file name>       append a .jia or .txt file")
        print("translate <file name>    translate user input to Jia code")    

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


    elif list(user_input.split(" "))[0].lower() == "append" and len(list(user_input.split(" "))) == 2:
        inputs = list(user_input.split(" "))
        if re.match(r"[^\.]+\.(jia|txt)", inputs[1]):
            append_file(inputs[1])

        elif re.match(r"^[^.]*$", inputs[1]):
            append_file(f"{inputs[1]}.jia")
        
        else:
            print("Error: Invalid file name")

    elif list(user_input.split())[0].lower() == "translate":
        if len(list(user_input.split(" "))) == 2:
            inputs = list(user_input.split(" "))
            if re.match(r"[^\.]+\.(jia|txt)", inputs[1]):
                if (os.path.exists(inputs[1]) and os.path.isfile(inputs[1])):
                    yes_or_no =input(f"Are you sure you want to overwrite '{inputs[1]}'? (Y/N): ").lower()

                    while yes_or_no != "y" and yes_or_no != "n":
                        yes_or_no = input(f"Are you sure you want to overwrite the file '{inputs[1]}'? (Y/N): ").lower()

                    if yes_or_no == "y":
                        translate_file(inputs[1])
                    else:
                        print("...Operation cancelled, file not overwritten")
                else:
                    translate_file(inputs[1])

            elif re.match(r"^[^.]*$", inputs[1]):
                if (os.path.exists(inputs[1] + ".jia") and os.path.isfile(inputs[1] + ".jia")):
                    yes_or_no =input(f"Are you sure you want to overwrite '{inputs[1]}.jia'? (Y/N): ").lower()

                    while yes_or_no != "y" and yes_or_no != "n":
                        yes_or_no = input(f"Are you sure you want to overwrite the file '{inputs[1]}.jia'? (Y/N): ").lower()

                    if yes_or_no == "y":
                        translate_file(inputs[1] + ".jia")
                    else:
                        print("...Operation cancelled, file not overwritten")

                elif (os.path.exists(inputs[1] + ".txt") and os.path.isfile(inputs[1] + ".txt")):
                    yes_or_no =input(f"Are you sure you want to overwrite '{inputs[1]}.txt'? (Y/N): ").lower()

                    while yes_or_no != "y" and yes_or_no != "n":
                        yes_or_no = input(f"Are you sure you want to overwrite the file '{inputs[1]}.txt'? (Y/N): ").lower()

                    if yes_or_no == "y":
                        translate_file(inputs[1] + ".txt")
                    else:
                        print("...Operation cancelled, file not overwritten")

                else:
                    translate_file(inputs[1] + ".jia")
            
            else:
                print("Error: Invalid file name")

        elif len(list(user_input.split())) == 1:
            file_name = "new_file"
            x = 1
            while (os.path.exists(file_name + ".jia") and os.path.isfile(file_name + ".jia")):
                file_name = "new_file"
                file_name = f"{file_name}{x}"
                x+=1
            translate_file(f"{file_name}.jia")


        else:
            print("Error: Invalid command")

    else:
        print("Error: Invalid command")


    






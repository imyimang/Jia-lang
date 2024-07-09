def simplebrain(code):
    tape = [0] * 30000
    pointer = 0
    i = 0
    loop_stack = []
    max_used_pointer = 0  

    def find_matching_bracket(start, direction):
        count = 0
        i = start
        while True:
            i += direction
            if i < 0 or i >= len(code):
                raise ValueError("Unmatched brackets")
            if code[i] == '[':
                count += 1
            elif code[i] == ']':
                if count == 0:
                    return i
                count -= 1

    output = []

    while i < len(code):
        command = code[i]
        if command == '右':
            pointer = (pointer + 1) % 30000
            max_used_pointer = max(max_used_pointer, pointer)
        elif command == '左':
            pointer = (pointer - 1) % 30000
        elif command == '申':
            tape[pointer] = (tape[pointer] + 1) % 256
            max_used_pointer = max(max_used_pointer, pointer)
        elif command == '田':
            tape[pointer] = (tape[pointer] - 1) % 256
            max_used_pointer = max(max_used_pointer, pointer)
        elif command == '由':
            output.append(chr(tape[pointer]))
        elif command == '甲':
            tape[pointer] = ord(input("Input a character: ")[0])
            max_used_pointer = max(max_used_pointer, pointer)
        elif command == '始':
            if tape[pointer] == 0:
                i = find_matching_bracket(i, 1)
            else:
                loop_stack.append(i)
        elif command == '終':
            if tape[pointer] != 0:
                i = loop_stack[-1]
            else:
                loop_stack.pop()
        i += 1


    tape_output = tape[:max_used_pointer+1] 
    while tape_output and tape_output[-1] == 0:
        tape_output.pop() 

    return ''.join(output), tape_output

def run_jia():
    while True:
        user_input = input(">>> ")
        if user_input.lower() == "exit":break
        result, final_tape = simplebrain(user_input)
        print("=============================================")
        print(result)
        print("=============================================")
        print("Jia's tape:")
        print(final_tape)



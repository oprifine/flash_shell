def bf():
    tape = [0] * 30000
    pointer = 0
    output = []

    stack = []
    loop_start = {}

    code = input("Enter BF code: ")
    
    i = 0
    while i < len(code):
        command = code[i]

        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            tape[pointer] += 1
        elif command == '-':
            tape[pointer] -= 1
        elif command == '.':
            output.append(chr(tape[pointer]))
        elif command == ',':
            # Input not implemented in this example
            pass
        elif command == '[':
            stack.append(i)
        elif command == ']':
            if tape[pointer] == 0:
                stack.pop()
            else:
                if i not in loop_start:
                    loop_start[i] = stack.pop()
                else:
                    i = loop_start[i] - 1

        i += 1

    return ''.join(output)

cmd = input("Enter brainf*ck code: ")

if cmd == "exit":
    for i in range (1):
        break
    else:
        pass
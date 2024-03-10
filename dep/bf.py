import pybrainfuck

def run_brainfuck(code):
    # Create a Brainfuck interpreter
    interpreter = pybrainfuck.Interpreter()

    # Run the provided Brainfuck code
    interpreter.execute(code)

    # Get the output of the Brainfuck program
    output = interpreter.output()

    return output

# Get user input for Brainfuck code
code = input("Enter Brainfuck code: ")

# Check if the input is 'exit' to terminate the loop
if code == "exit":
    # Perform any cleanup or exit actions if needed
    pass
else:
    # Execute the Brainfuck code and print the output
    result = run_brainfuck(code)
    print("Output:", result)
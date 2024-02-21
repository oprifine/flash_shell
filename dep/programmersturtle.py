import turtle

t = turtle.Turtle()

def forward(distance):
    turtle.forward(distance)

def backward(distance):
    turtle.backward(distance)

def left(angle):
    turtle.left(angle)

def right(angle):
    turtle.right(angle)

def main():
    print("Welcome to Programmer's Turtle!")
    print("Type commands like 't.forward(90)' or 't.left(45)'.")
    print("To exit, type 'exit'.")

    while True:
        command = input(">>> ")

        if command.lower() == 'exit':
            print("Exiting Programmer's Turtle. Goodbye!")
            break

        try:
            # Execute the user command within the turtle namespace
            exec(command, globals(), locals())
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

print("Dais simple calculator")
print("----------------------------------")

def addition():
    num1 = float(input("Enter the First Number "))
    num2 = float(input("Enter the second number "))

    result = num1 + num2
    return result

def subtraction():
    num1 = float(input("Enter the first Number "))
    num2 = float(input("Enter the second number "))

    result = num1 - num2
    return result

def multiplication():
    num1 = float(input("Enter the first Number "))
    num2 = float(input("Enter the second number "))

    result = num1 * num2
    return result

def division():
    num1 = float(input("Enter the first Number "))
    num2 = float(input("Enter the second number "))

    if num2 == 0:
        print("Division by zero is not allowed")

    result = num1 / num2
    return result

def calculator():
    quit = False #boolean value
    while not quit:
        print("Select an option")
        print("Press 'a' to add")
        print("Press 'm' to multiply")
        print("Press 's' to subract")
        print("Press 'd' to divide")
        print("Press 'q' to quit")

        choice = input("Enter your choice ")

        if choice == 'q':
            quit = True
            break

        if choice == 'a':
            answer = addition()
            print("Result of addition is", answer)
        elif choice == 'm':
            answer = multiplication()
            print("Result of multiplicatio  is ", answer)
        elif choice == 'd':
            answer = division()
            print("The quotient is: ", answer)
        elif choice == 's':
            answer = subtraction()
            print("The difference is: ", answer)
        else:
            print("You entered an invalid choice")


if __name__ == "__main__":
    calculator()
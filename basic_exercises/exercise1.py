#Calculate the multiplication and sum of two numbers

def sum():
    number1 = int(input("Enter the First number: "))
    number2 = int(input("Enter the Second number: "))

    result = number1 + number2
    print("The result is ", result)

def multiply():
    number1 = int(input("Enter the First number: "))
    number2 = int(input("Enter the Second number: "))

    result = number1 * number2
    print("The result is ", result)

print("Sum and Multiplication Program")
print("------------------------------------------")

if __name__ == "__main__":
    print("Do you want to sum or multiply")
    print("press '*' for multiply and '+' for sum")

    choice = input("Enter your choice ")

    if choice == '*':
        multiply()
    else:
        sum()

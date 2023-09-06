#Check palindrome number

#writing a program to check if a given number is a palindrome number
#NB: A palindrome number is a number that is the same after reverse.

def palindrome_checker():
    number = input("Enter number to check ")

    #reversing
    string = str(number)
    reverse = string[::-1]
    print(reverse)

    #reverse_no = int(reverse)

    if (number == reverse):
        print("Original number", number)
        print("Yes the number is a palindrome")
    else:
        print("Original number", number)
        print("No, the number is not a palindrome")

if __name__ == "__main__":
    palindrome_checker()

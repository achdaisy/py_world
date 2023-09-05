#print characters from a string that are present at an even index number
#write a program to accept a string from the user and display charcaters that are present at an even index number

def accept_string():
    string = input("Enter the string: ")

    print("Original string is ", string)
    print("Printing only even index chars")
    
    index = 0
    while index < len(string):
        print(string[index])
        index += 2

if __name__ == "__main__":
    accept_string()
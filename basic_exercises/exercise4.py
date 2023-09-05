#Remove the first n charaters from a string

#Program to remove characters from a string starting from zero upto n and return the n string

def remove_n_chars():
    string = input("Enter the string ")
    n = int(input("Enter 'n': "))
    strlen = len(string)

    if n > strlen:
        print("n value should be less than the string length")
        return (-1)
    
    result = string[n - 1:]  #main logic #using n-1 because of indexing, and indexes are usually less than 1
    
    print(result)

if __name__ == "__main__":
    remove_n_chars()

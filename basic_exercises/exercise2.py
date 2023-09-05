###prints the sum of the current and the previous number

#program to iterate the first ten numbers, and in each iteration, print the sum of the current and the previous number
print("Printing current and previous number sum in range (10)")
def loop():
    sum = 0
    previous_no = 0


    for i in range (10):
        sum = i + previous_no
        print ("Current Number", i , "Previous Number", previous_no , "Sum: ",sum)

        previous_no = i

if __name__ == "__main__":
    loop()

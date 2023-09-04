print("Countdown Timer")
print("----------------------------------")

import time

def countdown(user_input):
    while user_input >= 0:
        mins, secs = divmod(user_input, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end = "\r") #end = "\r" overwrites the previous timer displayed in the terminal and creates effect of timer updating in place
        time.sleep(1) #to pause for a second
        user_input -= 1
    print("Countdown done!!")    


if __name__ == "__main__":
    user_input = int(input("Enter the number of seconds "))
    countdown(user_input)
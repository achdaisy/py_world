import random
list_of_attempts = []

def show_score():
    if not list_of_attempts:
        print("There is currently no high score")
    
    else:
        print("The current high score is", {min(list_of_attempts)})


def start_game():
    random_no = random.randint(1, 10)
    print("Number guessing game")
    print("------------------------------")
    print("Hello player, welcome to the number guessing game!")
    player_name = input("Enter your name ")

    while True:
        print("\n New game")
        attempts = 0
        wanna_play = input("hey, do you want to play the game? (Enter Yes/No) ")

        if wanna_play.lower() != "yes":
            break

        
        while wanna_play.lower() == "yes":
            try:
                guess = int(input("Pick a number between 1 and 10: "))
                if guess < 1 or guess > 10:
                    raise ValueError("Please enter a number within the given range")

                attempts += 1
                list_of_attempts.append(attempts)

                if guess == random_no:
                    print("Congratulations you got it right!!")
                    print("It took you ",attempts, "attempts to get it")
                    wanna_play = input("Would you like to play again (Enter yes/no) ")
                    if wanna_play.lower() == "no":
                        print("Bye")
                        break
                    else:
                        attempts = 0
                        random_no = random.randint(1, 10)
                        show_score()
                        continue
                else:
                    if guess > random_no:
                        print("The number is higher, try a lower one" )
                    elif guess < random_no:
                        print("The guess is low, try  a higher number")
                

            except ValueError as err:
                    print("Oh no, thats not a valid value")
                    print(err)

if __name__ == '__main__':
    start_game()


print("Welcome to my Quiz game")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay, let's play")

userName = input("What's your name? ")
print("Hi " +userName+ ", Thank you for joining quiz game")
score = 0

print("Question one: What does CPU stand for? (5 marks) ")
answer = input()

if answer == "central processing unit":
    print("Correct")
    score += 5
else:
    print("Incorrect")

print("Hi " +userName+ " your total score is " +str(score) )
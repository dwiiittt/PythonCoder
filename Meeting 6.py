score = 0

def check_guess(answer):
    global score
    still_guessing = True
    attempt = 0

    while still_guessing and attempt < 3:
        guess = input("Guess: ")
        
        if guess.lower() == answer.lower():
            print("Correct answer!")
            score += 1
            still_guessing = False
        else:
            if attempt < 2:
                print("Wrong answer! Try again.")
            attempt += 1
            
    if attempt == 3 and still_guessing:
        print("The correct answer was " + answer)

# --- Game Starts Here ---

print("Guess the Country!")

print("By Size, what is the largest country in the world?")
check_guess("Russia")

print("Which country has a unicorn as its national animal?")
check_guess("Scotland")

print("In which country would you find the currency Baht?")
check_guess("Thailand")

print("Your final score is: " + str(score))
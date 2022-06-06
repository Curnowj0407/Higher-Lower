# HL component 5 - no duplicates

# To Do
# set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

# HL component 5 - prevent duplicates guesses

SECRET = 7
GUESSES_ALLOWED = 5

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >=1:

    guess = int(input("Guess:"))

    # guess that guess is not a duplicate
    if guess in already_guessed:
        print("you already guess that number! please try again,"
              "you *still* have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < SECRET:
            print("too low , try a higher number. guesses left:")

        elif guess > SECRET:
            print("too high, try a lower number. guess left:")

        else:
            if guess < SECRET:
                print("too low!")
            elif guess > SECRET:
                print("too high")


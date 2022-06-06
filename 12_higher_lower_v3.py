import math
# HL component 1 - get (and check) user input

# to do
# check a lowest is an integer (any integer)
# check that higest is more than lowest (lower bound only)
# check that rounds is more than 1 (upper bound only)
# check that guess is between lowest and higher (
# lower and upper bound)

# Function go here

def choice_checker(question, valid_list, error):
    valid = False
    while not valid:
        # Ask user for choice (and put lowercase)
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


def show_help():
    print("""

    how to play...

    choose a low number and a high number then guess between your low number and high number etc

    """)



def int_check(question, low=None, high=None, exit_code = None):

    situation = ""
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is not None :
        situation = "low only"

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)
            # check to see if response is the exit code and return it
            if response == exit_code:
                return response

            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue


# Main Routine

yes_no_list = ["yes", "no"]

# Ask user if they have played before.
show_instruction = choice_checker("D0 you want to see instruction?",yes_no_list, "please answer yes or no")

if show_instruction == "yes":
    show_help()

# Number checking function goes here

# checks that response is an integer
low_num = int_check("Low Number: ")
print("You chose a low number of ", low_num)

# checks that response is an integer more than the low number
high_num = int_check("High Number: ", low_num)
print("You chose a high number of ", high_num)

var_range = high_num - low_num + 1
max_raw = math.log2(var_range)
max_upped = math.ceil(max_raw)
max_guesses = max_upped + 1
print("max guess: {}".format(max_guesses))




guess = int_check("Guess: ", low_num, high_num, "xxx")
print("You guessed {}".format(guess))

# end of game statements

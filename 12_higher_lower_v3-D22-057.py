# HL component 1 - get (and check) user input

def yes_no():
    response = input(yes_no)
    if response == "y" or response =="yes":
        return response

    if response == "n" or response == "no":
        

        return response


def instruction():
    print("please choose between high and lower")

# Number checking function goes here



def int_check(question, low=None, high=None, exit_code = None):

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


# checks that response is an integer
low_num = int_check("Low Number: ")
print("You chose a low number of ", low_num)

# checks that response is an integer more than the low number
high_num = int_check("High Number: ", low_num)
print("You chose a high number of ", high_num)



guess = int_check("Guess: ", low_num, high_num, "xxx")
print("You guessed {}".format(guess))

# end of game statements

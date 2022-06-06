# Fuction used to check input is vaild
def choice_checker (question):
    error = "please between higher or lower ( or xxx to quit)"
    valid = False
    while not valid:
        # Ask user for choice (and put choice in lowercase)
        response = input(question)
        response = "i" or response == "infinite"


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


# Main routine goes here

rounds_played = 0
mode = "regular"

# Ask user for # of rounds, <enter> for infinite mode
rounds = int_check("How many rounds <enter> for infinite: ", 1, exit_code = "")

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        mode = "infinite"
        rounds = 5

    if mode == "infinite":

        headings = "continue mode: round {}".format(rounds_played + 1)
        rounds += 1
    else:
        headings = "round {} of {}".format(rounds_played + 1, rounds)

    print(headings)
    choose = input("Type <enter>" )
    rounds_played += 1

    if choose == "xxx" or rounds_played >= rounds:
        break
    # rest of loop / game
    print("you choose {}".format(choose))


print("thank you for playing")

import random


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

# Number checking function goes here

# checks that response is an integer
low_num = int_check("Low Number: ")
print("You chose a low number of ", low_num)

# checks that response is an integer more than the low number
high_num = int_check("High Number: ", low_num)
print("You chose a high number of ", high_num)

for item in range(0, 5):
    secret_number = random.randint(low_num, high_num)
    print(secret_number)
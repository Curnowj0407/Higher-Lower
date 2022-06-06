# HL component 11 - maximum guesses calculator

import math

for item in range(0,4):

    low = int(input("Low: "))
    high = int(input("High: "))

    var_range = high - low + 1
    max_raw = math.log2(var_range)
    max_upped =math.ceil(max_raw)
    max_guesses = max_upped + 1
    print("max guess: {}".format(max_guesses))

    print()
#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Dec. 11, 2021
# This program allows a user to input a number and then view the corresponding
# month to that number.

import colorama
import random
import time
from colorama import Fore, Back, Style


# Cases that assign each number to a month
def month_num(user_num_int):
    cases = {
        1: lambda: print(Fore.CYAN +
                         "{} is the month of January".format(user_num_int)),
        2: lambda: print(Fore.RED +
                         "{} is the month of February".format(user_num_int)),
        3: lambda: print(Fore.BLUE +
                         "{} is the month of March".format(user_num_int)),
        4: lambda: print(Fore.YELLOW +
                         "{} is the month of April".format(user_num_int)),
        5: lambda: print(Fore.GREEN +
                         "{} is the month of May".format(user_num_int)),
        6: lambda: print(Fore.WHITE +
                         "{} is the month of June".format(user_num_int)),
        7: lambda: print(Fore.MAGENTA +
                         "{} is the month of July".format(user_num_int)),
        8: lambda: print(Fore.CYAN +
                         "{} is the month of August".format(user_num_int)),
        9: lambda: print(Fore.RED +
                         "{} is the month of September".format(user_num_int)),
        10: lambda: print(Fore.GREEN +
                          "{} is the month of October".format(user_num_int)),
        11: lambda: print(Fore.YELLOW +
                          "{} is the month of November".format(user_num_int)),
        12: lambda: print(Fore.MAGENTA +
                          "{} is the month of December".format(user_num_int)),
    }
    cases.get(user_num_int, lambda: print("Didn't match a case"))()


def main():

    # Get user input and print intro text
    print(Fore.WHITE + "What month is your number?")
    time.sleep(1)
    print(Fore.BLUE + " ")
    user_num = input("Enter a number between 1 and 12: ")

    # Make sure user doesn't input words
    try:

        user_num_int = int(user_num)
        # Print specific case
        month_num(user_num_int)
    except Exception:
        print("'{}' is not a number".format(user_num))
    print(" ")


if __name__ == "__main__":
    main()

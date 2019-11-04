#!/usr/bin/env python3

# Created by: Trinity Armstrong
# created on: November 2019
# This is the guess the number program


import random


def main():
    # This function runs the guess the number program with a break

    # Variables
    correct_number = random.randint(1, 9)

    # Process & output
    while True:
        # Input
        user_guess = input("Guess a number between 0 and 9 (integer): ")
        print("")

        try:
            user_guess = int(user_guess)
            if user_guess == correct_number:
                print("You are correct!!!")
                break
            else:
                print("Sorry, try again :)")
        except Exception:
            print("That is not an integer.")


if __name__ == "__main__":
    main()

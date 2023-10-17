#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Oct 16, 2023
# This program asks the user for the length of
# a side of an octagon in whatever units they want.
# It then calculates and displays
# the area and perimeter of the octagon.

import math


def main():
    # get the units the user wants to use from the user
    print("This program will calculate the area and perimeter of a octagon")
    print("with your length in whatever unit you want.")
    user_unit = str(input("Enter the units type you want: "))

    # get the length of octagon from the user
    length_of_side = float(input("Enter the length of the side you want: "))

    # Check if the length is negative
    if length_of_side < 0:
        print("")
        print("Please enter a positive length.")
        return  # This will exit the function, so it doesn't calculate or print anything else.

    # calculates the area
    area = 2 * (1 + math.sqrt(2)) * length_of_side**2

    # calculates the perimeter
    perimeter = 8 * length_of_side

    # display the area
    print("")
    print("The area of your octagon is = {:.2f}{}".format(area, user_unit))

    # display the perimeter
    print("")
    print("The perimeter of your octagon is = {:.2f}{}".format(perimeter, user_unit))


if __name__ == "__main__":
    main()

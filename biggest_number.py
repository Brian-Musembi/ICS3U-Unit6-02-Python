#!/usr/bin/env python3

# Created by Brian Musembi
# Created on June 2021
# This program prints 10 random integers and finds the average

import random


def max_value(random_list):
    # This function finds the largest number

    max_num = random_list[0]

    for loop_counter in range(0, len(random_list)):
        if max_num >= random_list[loop_counter]:
            continue
        elif max_num < random_list[loop_counter]:
            max_num = random_list[loop_counter]

    return max_num


def main():
    # This function prints 10 random integers and output

    print("This program prints 10 random integers between 1 and 100 and"
          " finds the largest among them.")
    print("")

    random_list = []

    print("Displayed below are 10 random integers between 1 and 100:")

    # process
    for loop_counter in range(0, 10):
        # random number
        random_number = random.randint(1, 100)
        random_list.append(random_number)
        print(random_number)

    # call function
    largest_num = max_value(random_list)

    print("")
    print("The largest integer among these is: {0}".format(largest_num))


if __name__ == "__main__":
    main()

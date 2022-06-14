#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: May 2022
# This program finds the class' average


def average_of_list(list_of_marks):
    # this function claculates the average
    total = 0

    for value in list_of_marks:
        total += value
    average = total / len(list_of_marks)

    return average


def main():
    # this function checks the input and places it in a list

    list_of_marks = []

    # input & process
    print("Please enter 1 mark at a time. Enter -1 to end.")
    print("")
    while True:
        mark_as_string = input("What is your mark(as a %): ")
        try:
            mark = int(mark_as_string)
            if mark == -1:
                break
            elif mark <= 0:
                print("invalid input. Try again.")
            else:
                list_of_marks.append(mark)
        except Exception:
            print("invalid input. Try again.")
    print("")

    answer = average_of_list(list_of_marks)
    print("The average is {}%".format(answer))


if __name__ == "__main__":
    main()

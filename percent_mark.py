#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program tells user the month afte typing the number


def mark(mark_level):
    # This function determines the student percentage
    percentage = None

    if mark_level == "4+":
        percentage = 97
    elif mark_level == "4":
        percentage = 90
    elif mark_level == "4-":
        percentage = 85
    elif mark_level == "3+":
        percentage = 78
    elif mark_level == "3":
        percentage = 74
    elif mark_level == "3-":
        percentage = 71
    elif mark_level == "2+":
        percentage = 68
    elif mark_level == "2":
        percentage = 64
    elif mark_level == "2-":
        percentage = 61
    elif mark_level == "1+":
        percentage = 58
    elif mark_level == "1":
        percentage = 55
    elif mark_level == "1-":
        percentage = 51
    elif mark_level == "0+":
        percentage = 45
    elif mark_level == "0":
        percentage = 35
    elif mark_level == "0-":
        percentage = 18
    elif mark_level == "NE":
        percentage = 0
    else:
        percentage = -1

    return percentage


def main():
    # This function takes input from the user
    level = input("Enter level of grade: ")
    print("")
    mark(level)
    final_mark = mark(level)
    print(final_mark)
    print("")
    if final_mark == -1:
        print("Invalid Input")


if __name__ == '__main__':
    main()

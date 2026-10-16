"""----------------------------------------------------------------
Name:       Morgan McPeek
Assignment: Lab - Baby Shark
Course:     CS 1430, Section X, Fall 2026
Purpose:    This program is designed to be practice for Python
            functions

Input: None

Output: The sound Baby Shark, with three verses:
        Baby Shark,
        doo-doo-doo-do-do-do-do *3
        Baby Shark!
        Mommy Shark,
        doo-doo-doo-do-do-do-do *3
        Mommy Shark!
        Daddy Shark,
        doo-doo-doo-do-do-do-do *3
        Daddy Shark!
----------------------------------------------------------------"""

##############
# CONSTANTS
##############
REPEAT = 3

def verse(age):
    print(age, "Shark,")
    print("doo-doo-doo-do-do-do-do")
def main():
    for _ in range(REPEAT):
        if _ == 0:
            age = "Baby"
            verse(age)
            verse(age)
            verse(age)
            print(age, "Shark!")
        elif n == 1:
            age = "Mommy"
            verse(age)
            verse(age)
            verse(age)
            print(age, "Shark!")
        elif n == 2:
            age = "Daddy"
            verse(age)
            verse(age)
            verse(age)
            print(age, "Shark!")

if __name__ == "__main__":
    main()

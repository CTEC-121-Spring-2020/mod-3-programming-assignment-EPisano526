# Module 3
#   Programming Assignment 4
#     Prob-3.py

# <YOUR NAME>


def letterGrade(score):
    if score == 5:
        grade = "A"

    elif score == 4:
        grade = "B"

    elif score == 3:
        grade = "C"

    elif score == 2:
        grade = "D"

    elif score == 1:
        grade = "F"

    elif score == 0:
        grade = "F"

    return grade


def unitTest():
    # your test code here
    print(letterGrade(5))
    print(letterGrade(4))
    print(letterGrade(3))
    print(letterGrade(2))
    print(letterGrade(1))
    print(letterGrade(0))


if __name__ == "__main__":
    unitTest()

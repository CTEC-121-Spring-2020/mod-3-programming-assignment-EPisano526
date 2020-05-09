# Module 3
#   Programming Assignment 4
#     Prob-5.py

# Esther Pisano


def main():

    try:
        x = eval(2)
        print("x:", x)
    except TypeError:
        print("eval() arg 1 must be a string, bytes or code object")
    except Exception:
        print("Caught an exception in the try block starting at line 10")


main()

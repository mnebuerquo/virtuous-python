#!/usr/bin/env python3
import silly

def square(x):
    """
    return the square of the argument
    >>> square(4)
    16
    """
    return x * x


def life():
    """
    this function tells you the meaning of life
    >>> life()
    42
    """
    return 42


def expectedToFail(x):
    """
    this function does something mathy
    the test is expected to fail
    >>> expectedToFail(2)
    77
    """
    return x * (x + 7)


def main():
    print("hello world")
    print(square(life()))
    print(silly.paragraph())


if __name__ == "__main__":
    main()

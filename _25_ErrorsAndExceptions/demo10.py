# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 错误和异常
用户自定义异常
    创建一个新的异常类来拥有自己的异常。异常类继承自Exception类，可以直接继承，或者间接继承

    当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，
    然后基于这个基础类为不同的错误情况创建不同的子类

    大多数的异常的名字都以"Error"结尾，就跟标准的异常命名一样。
'''


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, by_next, message):
        self.previous = previous
        self.next = by_next
        self.message = message


if __name__ == "__main__":
    try:
        print(10 / 0)
    except TransitionError as e:
        print(e.previous, e.next, e.message)

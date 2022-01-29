# -*- coding: UTF-8 -*-
# author: chenyongjun


class Student(object):
    """学生类型Student"""

    _level = None

    def __init__(self, name, grade, score):
        """
        1.the __init__() constructor initializes the class
        2.self：represents the instance of the created class itself
        :param name: student name
        :param score: student score
        """
        self.__name = name
        self.__grade = grade
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_grade(self):
        return self.__grade

    def get_level(self):
        if self.__score >= 90:
            self._level = "A"
            return self._level
        elif self.__score >= 80:
            self._level = "B"
            return self._level
        elif self.__score >= 60:
            self._level = "C"
            return self._level
        else:
            self._level = "D"
            return self._level

    def display(self):
        print("The {0:s} score is: {1:.2f}".format(self.__name, self.__score))

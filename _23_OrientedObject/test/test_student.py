# -*- coding: UTF-8 -*-
# author: chenyongjun
from _23_OrientedObject.objects.Students import Student
import unittest


class StudentTest(unittest.TestCase):
    """description the Test Class"""

    def setUp(self):
        """install the WebDriver"""
        self.student = Student("Jack", 3, 88.90)

    # @unittest.skip("skipping")
    def test_student(self):
        """description the test method"""
        self.student.display()
        self.student._level = "D"
        print(self.student._level)
        print(self.student.get_level())

    def tearDown(self):
        """tearDown the WebDriver"""
        del self.student


if __name__ == "__main__":
    unittest.main()

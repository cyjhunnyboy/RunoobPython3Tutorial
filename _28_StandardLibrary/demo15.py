# -*- coding: UTF-8 -*-
# author: chenyongjun
import unittest
from _25_StandardLibrary.demo14 import average

"""
unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集
"""


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)


if __name__ == "__main__":
    # Calling from the command line invokes all tests
    unittest.main()

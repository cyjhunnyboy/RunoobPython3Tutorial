# -*- coding: UTF-8 -*-
# author: chenyongjun


class Complex:

    def __init__(self, real_part, imaginary_part):
        self.realPart = real_part
        self.imaginaryPart = imaginary_part

    def print_complex(self):
        print("realPart = {0:.1f}, imaginaryPart = {1:.2f}".format(self.realPart, self.imaginaryPart))


if __name__ == "__main__":
    x = Complex(3.0, -4.5)
    x.print_complex()

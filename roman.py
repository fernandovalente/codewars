"""
Create a function taking a positive integer as its parameter and returning a 
string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting 
with the left most digit and skipping any digit with a value of zero. 
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 
2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman 
symbol in descending order: MDCLXVI.
"""

import unittest


def return_roman_numeral(n: int) -> str:
    if not type(n) == int or n < 1:
        return 'The number must be positive integer.'

    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
  
    # Converting to roman
    thousands = m[n // 1000]
    hundreds = c[(n % 1000) // 100]
    tens = x[(n % 100) // 10]
    ones = i[n % 10]
  
    return f'{thousands + hundreds + tens + ones}'.replace(' ', '')
  

class RomanNumeralsTest(unittest.TestCase):

    def test_case_negative_integer(self):
        self.assertEqual(
            return_roman_numeral(-1),
            'The number must be positive integer.'
        )

    def test_case_zero(self):
        self.assertEqual(
            return_roman_numeral(0),
            'The number must be positive integer.'
        )

    def test_case_not_int(self):
        self.assertEqual(
            return_roman_numeral('a'),
            'The number must be positive integer.'
        )

    def test_case_I(self):
        self.assertEqual(return_roman_numeral(1), 'I')

    def test_case_V(self):
        self.assertEqual(return_roman_numeral(5), 'V')

    def test_case_IV(self):
        self.assertEqual(return_roman_numeral(4), 'IV')

    def test_case_CMLXXXIV(self):
        self.assertEqual(return_roman_numeral(984), 'CMLXXXIV')

    def test_case_MDCCCLXXXIX(self):
        self.assertEqual(return_roman_numeral(1889), 'MDCCCLXXXIX')
    
    def test_case_MCMLXXXIX(self):
        self.assertEqual(return_roman_numeral(1989), 'MCMLXXXIX')


if __name__ == '__main__':
    unittest.main()

'''
An isogram is a word that has no repeating letters, consecutive or
non-consecutive. Implement a function that determines whether a string that
contains only letters is an isogram. Assume the empty string is an isogram.
Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
'''

import unittest


def is_isogram(string):
    return len(string) == len(set(string.lower()))


class IsIsogramTest(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(is_isogram('Dermatoglyphics'), True)
    
    def test_case_2(self):
        self.assertEqual(is_isogram('isogram'), True)
    
    def test_case_3(self):
        self.assertEqual(is_isogram('aba'), False)

    def test_case_4(self):
        self.assertEqual(is_isogram('moOse'), False)

    def test_case_5(self):
        self.assertEqual(is_isogram(''), True)


if __name__ == '__main__':
    unittest.main()
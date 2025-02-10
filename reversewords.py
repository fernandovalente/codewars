'''
Complete the function that accepts a string parameter, and reverses each word
in the string. All spaces in the string should be retained.

Examples:
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

import unittest


def reverse_words(words):
    return ' '.join([w[::-1] for w in words.split(' ')])


class ReverseWordsTest(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(
            reverse_words('Lorem ipsum dolor sit amet'),
            'meroL muspi rolod tis tema'
        )

    def test_case_2(self):
        self.assertEqual(
            reverse_words('This is an example!'),
            'sihT si na !elpmaxe'
        )

    def test_case_3(self):
        self.assertEqual(reverse_words('double  spaces'), 'elbuod  secaps')


if __name__ == '__main__':
    unittest.main()
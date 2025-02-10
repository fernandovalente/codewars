"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets, with values
between 0 and 255, inclusive.

Examples of valid inputs:
1.2.3.4
123.45.67.89

Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

Notes:
 - Leading zeros (e.g. 01.02.03.04) are considered invalid
 - Inputs are guaranteed to be a single string
"""

import socket, unittest


# Using Socket
def is_valid_ip_socket(addr):
    try:
        socket.inet_pton(socket.AF_INET, addr)
        return True
    except socket.error:
        return False


# Handly way
def is_valid_ip(addr):
    splited_ip = addr.split(".")
    
    if not len(splited_ip) == 4:
        return False
    
    for i in splited_ip:
        if not str(i).isdigit():
            return False
        
        if len(i) > 1 and i[0] == "0":
            return False

        if not 0 <= int(i) <= 255:
            return False

    return True


class IsValid(unittest.TestCase):

    # Using Socket
    def test_case1(self):
        self.assertEqual(is_valid_ip_socket("0.0.0.0"), True)

    def test_case2(self):
        self.assertEqual(is_valid_ip_socket("01.02.03.04"), False)

    def test_case3(self):
        self.assertEqual(is_valid_ip_socket("1.2.3"), False)

    def test_case3(self):
        self.assertEqual(is_valid_ip_socket("1"), False)

    def test_case4(self):
        self.assertEqual(is_valid_ip_socket("1.2.3.4.5"), False)

    def test_case4(self):
        self.assertEqual(is_valid_ip_socket("123.456.78.90"), False)

    def test_case4(self):
        self.assertEqual(is_valid_ip_socket("123.045.067.089"), False)

    def test_case5(self):
        self.assertEqual(is_valid_ip_socket("192.168.0.1"), True)

    def test_case6(self):
        self.assertEqual(is_valid_ip_socket("1.2.3.4"), True)

    def test_case7(self):
        self.assertEqual(is_valid_ip_socket("123.45.67.89"), True)

    def test_case8(self):
        self.assertEqual(is_valid_ip_socket("qwer.asdf.67.89"), False)
    
    # Handly way
    def test_case9(self):
        self.assertEqual(is_valid_ip("01.02.03.04"), False)

    def test_case10(self):
        self.assertEqual(is_valid_ip("1.2.3"), False)

    def test_case11(self):
        self.assertEqual(is_valid_ip("1"), False)

    def test_case12(self):
        self.assertEqual(is_valid_ip("1.2.3.4.5"), False)

    def test_case13(self):
        self.assertEqual(is_valid_ip("123.456.78.90"), False)

    def test_case14(self):
        self.assertEqual(is_valid_ip("123.045.067.089"), False)

    def test_case15(self):
        self.assertEqual(is_valid_ip("192.168.0.1"), True)

    def test_case16(self):
        self.assertEqual(is_valid_ip("1.2.3.4"), True)

    def test_case17(self):
        self.assertEqual(is_valid_ip("123.45.67.89"), True)

    def test_case18(self):
        self.assertEqual(is_valid_ip("qwer.asdf.67.89"), False)

    def test_case19(self):
        self.assertEqual(is_valid_ip("0.0.0.0"), True)


if __name__=="__main__":
    unittest.main()

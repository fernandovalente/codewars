"""
Fizz Buzz is a popular coding challenge often used in coding interviews as a
basic test of a candidate's programming skills. The task is to write a program
that prints the numbers from 1 to 100. But for multiples of 3, it should print
"Fizz" instead of the number, and for the multiples of 5, it should print "Buzz".
For numbers which are multiples of both 3 and 5, it should print "FizzBuzz".
"""

for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

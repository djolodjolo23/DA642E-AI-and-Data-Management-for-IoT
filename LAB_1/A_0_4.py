# A.0.4. Is it a prime number? (function) Mandatory - 1pt
# A prime number is an integer greater than 1 that is only divisible by one and itself. Write a function that
# determines whether or not its parameter is prime, returning True if it is, and False otherwise. Write a main
# program that reads an integer from the user and displays a message indicating whether or not it is prime.

import math

def main():
    print(is_it_prime(10))


def is_it_prime(num):
    if num > 1:
        # optimised way of checkin, after square root the divisors repeat in reverse order
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    main()
# A.0.5. What is the next prime? (loop) Mandatory - 1pts

# In this exercise, you will create a function named "nextPrime" that finds and returns  the first prime number
# larger than some integer, n. The value of n will be passed to the function as its only parameter. Include a main
# program that reads an integer from the user and displays the first prime number larger than the entered value.
# Import and use your solution to Exercise A.03 while completing this exercise.

from A_0_4 import is_it_prime


def main():
    print(f"The next prime number is: {next_prime(get_input())}.")


def next_prime(n):
    n += 1
    while not (is_it_prime(n)):
        n += 1
    return n


def get_input():
    while True:
        user_input = input("Provide n: ").strip().lower()
        if user_input == "quit":
            return None
        try:
            num = int(user_input)
            if num < 0:
                print("Please enter a non-negative number.")
                continue
            return num
        except ValueError:
            print("Invalid input! Please enter a valid number or type 'quit' to exit.")



if __name__ == '__main__':
    main()
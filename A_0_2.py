# A.0.2: Dog Years! (conditionals) Mandatory - 1pt
#  It is commonly said that one human year is equivalent to 7 dog years. However, this simple conversion fails to
#  recognize that dogs reach adulthood in approximately two years. As a result, some people believe that it is better
#  to count each of the first two human years as 10.5 dog years, and then count each additional human year
#  as 4 dog years.

# Write a program that implements the conversion from human years to dog years described in the previous paragraph.
# Ensure that your program works correctly for conversions of less than two human years and for conversions of two or
# more human years. Your program should display an appropriate error message if the user enters a negative number.


def main():
    years = get_input()
    if years is None:
        print("Goodbye!")
        return
    print_dog_years(convert_to_dog_years(years))


def get_input():
    while True:
        user_input = input("How many years to convert? :) ").strip().lower()
        if user_input == "quit":
            return None
        try:
            years = int(user_input)
            if years < 0:
                print("Please enter a non-negative number.")
                continue
            return years
        except ValueError:
            print("Invalid input! Please enter a valid number or type 'quit' to exit.")


def print_dog_years(dog_years):
    print(f"The number you provided corresponds to {dog_years} dog years.")


def convert_to_dog_years(years):
    dog_years = 0;
    for i in range(1, years + 1):
        if i <= 2:
            dog_years += 10.5
        else:
            dog_years += 4
    return dog_years


if __name__ == "__main__":
    main()

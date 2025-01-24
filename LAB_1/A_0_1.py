# A.0.1: Cinnamon buns (formatting output) Mandatory - 1pt
# A bakery sells fresh Swedish lovely Kanelbulle for 35 SEK each. Day-old Kanelbulle is discounted by 60 percent.
# A customer enters to buy only old kanelbulle from the store. Write a program that begins by reading the number of
# day-old Kanelbulle being purchased from the user. Then your program should display the regular price for them, the
# discount because they are day-old, and the total price. All of the values should be displayed using two decimal
# places, and the decimal points in all of the numbers should be aligned when reasonable values are entered by the user.

kanelbulle_price = 35.00
kanelbulle_discounted_price = kanelbulle_price * 0.6

def main():
    print_prices(get_input())


def print_prices(user_input):
    regular_price = user_input * kanelbulle_price
    discounted_price = user_input * kanelbulle_discounted_price
    discount = regular_price - discounted_price

    print(f"Regular price for {user_input} Kanelbulle's is: {regular_price:.2f} SEK")
    print(f"Discount for day-old Kanelbulle's is: {discount:.2f} SEK")
    print(f"Total price for {user_input} day-old Kanelbulle's is: {discounted_price:.2f} SEK")
    


def get_input():
    while True:
        user_input = input("How many KanelBulle's you want to buy? :) ").strip().lower()
        if user_input == "quit":
            return None
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number or type 'quit' to exit.")


if __name__ == "__main__":
    main()




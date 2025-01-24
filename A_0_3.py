# A.0.3: Coin Flip - 3 same flips (loop) Mandatory - 1pts

# Create a program that uses Python’s random number generator to simulate flipping a coin several times. The simulated
# coin should be fair, meaning that the probability of heads is equal to the probability of tails.

#Each time the program is run, your program should flip simulated coins until either 3 consecutive heads or 3
# consecutive tails occur. Display an H each time the outcome is heads, and a T each time the outcome is tails, with
# all of the outcomes shown on the same line. Then display the number of flips needed to reach 3 consecutive flips
# with the same outcome.

import random

arr = ['head', 'tail']


def main():
    for i in range(5):
        flip()


def flip():
    head_count = 0
    tail_count = 0
    total_flips = 0
    while head_count < 3 and tail_count < 3:
        random_flip = random.choice(arr)
        if random_flip == arr[0]:
            print('H', end=" ")
            head_count += 1
            tail_count = 0
        else:
            print('T', end=" ")
            tail_count += 1
            head_count = 0
        total_flips += 1
    print(f" ({total_flips} flips)")


if __name__ == "__main__":
    main()
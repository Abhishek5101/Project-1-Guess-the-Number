import random

count = 1

def start_game(count):
    computer = random.randint(1,10)
    while True:
        try:
            answer = int(input("Please enter your guess\n "))
            if answer < 1 or answer > 10:
                count += 1
                print("please only input values from 1 to 5\n")
                continue
            if answer < computer:
                count += 1
                print("\U0001F9D0 It's higher than that\n ")
                continue
            elif answer > computer:
                count += 1
                print("\U0001F9D0 It's Lower than that\n")
                continue
            print("\U0001F44F Congrats!You got it in {} tries".format(count))
            break

        except ValueError:
            count += 1
            print("Please input only Valid Input: Integers from 1-10")


if __name__ == '__main__':
    start_game(count)


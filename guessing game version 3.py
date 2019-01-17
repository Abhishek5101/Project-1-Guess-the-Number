import random

count=0

def start_game(count):
    lowscore=999
    print("Guess a number between 1-10 that I have in mind?")
    computer = random.randint(1, 10)
    while True:
        try:
            answer = int(input("Please enter your guess\n"))
            count += 1
            if answer < 1 or answer > 10:
                raise ValueError()
            if answer == computer:
                print("\U0001F44F Congrats You got it. It took you {} attempts".format(count))
                if count < lowscore:
                    lowscore = count
            elif answer < computer:
                print("\U0001F9D0 It's higher than that\n")
                continue
            elif answer > computer:
                print("\U0001F9D0 It's lower than that\n")
                continue
            playagain = input("would you like to play again? [y/n]\n")
            if playagain.lower() == "y":
                count = 0
                computer = random.randint(1,10)
                print("beat the score of {} to do the best".format(lowscore))
                continue
            elif playagain.lower() == "n":
                print(" \U0001F600 Thank You for playing this silly little game with us\n")
                break
            else:
                continue
        except ValueError:
            count += 1
            print("please enter valid input. Only integers from 1-10")


if __name__ == '__main__':
    start_game(count)


import random
count=0
def start_game(count):
    try:
        answer=int(input("Please guess a Number between 1-100\n"))
        count+=1
        computer=random.randint(1,100)
        while answer != computer:
            if answer < 1 or answer > 100:
                count+=1
                print("Your guess should be in the range of 1-100 only!")
                answer=int(input("enter a number\n"))
                continue
            elif answer < computer:
                print("It's higher than that\n")
                count+=1
                answer=int(input("enter a number\n"))
                continue
            elif answer > computer:
                print("It's Lower than that\n")
                count+=1
                answer=int(input("enter a number\n"))
                continue
    except ValueError:
        print("Error:please input integers only")
        count+=1

    else:
        print("Got it\n")
        print("You got in {} tries\n".format(count))

    playagain=input("Would you like to play again?[y/n] \n")
    if playagain.lower() == "y" :
        start_game(count)
    else:
        print("\tThanks for playing the game")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game(count)

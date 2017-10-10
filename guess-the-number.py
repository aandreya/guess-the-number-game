import random

print "Let's play a game!\n\nWe hid a number and we want you to guess it.\nYou have 5 chances to get it right.\nPRIZE: the fun!\n\n" \
      "Now let's guess a number between 1 and 30!\n\n "

def main():
    another_game = "y"
    while another_game.lower() == "y":
        hidden_number = random.randint(1, 30)
        for guess in range(1,6):
            try:
                bingo = int(raw_input("Your guess is: "))
                if bingo == hidden_number:
                    print "W O W ! You guessed it!"
                    break
                elif bingo > hidden_number:
                    print "Must be lower number"
                elif bingo < hidden_number:
                    print "Must be higher number"
            except ValueError:
                print "Your choice is not a number."
        print "\n\n G A M E   O V E R"
        another_game = raw_input("Wanna play again?    Y / N  :")

if __name__ == "__main__":
    main()

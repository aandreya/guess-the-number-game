hidden_number = 17

print "Let's play a game!"
print "We hid a number and we want you to guess it."
print "You have 5 chances to guess the hidden number."
print "PRIZE: the fun!"
print " "
print " "
print "Now let's guess a number between 1 and 30! "
print " "
print " "

i = 0
guess = 0

while True:
    try:
        guess = int(raw_input("Your guess is: "))

        if guess > 30:
            print "Number must be between 1 an 30."
            print " "
        elif guess == hidden_number:
            print "W O W ! You guessed it!"
            print " "
            break
        elif guess > hidden_number:
            print "Try lower number"
            print " "
        elif guess < hidden_number:
            print "Try higher number"
            print " "
    except ValueError:
        print "Your choice is not a number.";

    i = i + 1
    if i >= 5:
            print " "
            print "G A M E   O V E R !"
            print " "
            break
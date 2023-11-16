import random  #import the random module

generatedNum = random.randint(1,100)  #the random number is generated for the user to guess

userGuess=0  #start userGuess at 0, so that loop can start and is not equal to generated num
guessCount = 0  #define count for amount of times user guessed
maxGuesses = 7 #constant for max amount of guesses

print("You have 7 attempts to guess correctly, good luck!")  #tell the user how many attempts they have to guess num

while userGuess != generatedNum:  #while loop for when the user did not guess the correct num
    print("Guess a number between 1 and 100: ")  #ask the user to pick a num

    while True:  #loop for try/except to ensure the user enters an int
        try:
            userGuess = int(input())  #input for user to pick a num, converted to int
            break
        except:  #display an error if the user enters something other than an int
            print("ERROR: Input must be an integer between 1 and 100. Try again!")

    guessCount += 1  #add one guess to the amount of guesses for the user

    if  guessCount != maxGuesses:  #if user does not hit max attempts

        if userGuess == generatedNum:  #break this nested statement if the user guesses correctly
            print("You guessed the correct number in "+str(guessCount)+" attempts. Great job!")  #print amount of guesses, convert to string
            break
        elif ((userGuess > generatedNum) and (userGuess < 101)):  #if user guesses too high, tell user too high and reset loop
            print("Try Again! You guessed too high.")
            continue
        elif ((userGuess < generatedNum) and (userGuess > 0)):  #if user guesses too low, tell user too low and reset loop
            print("Try Again! You guessed too low.")
            continue
        else:
            print("ERROR: Input must be an integer between 1 and 100. Try again!")  #print an error if the number is not between 1 and 100
            guessCount -= 1  #subtract 1 from the guess count because this is an error
            continue

    elif userGuess == generatedNum:  #if user guesses the correct number break loop
        print("You guessed the correct number in "+str(guessCount)+" attempts. Great job!")  #print amount of guesses, convert to string
        break


    else:  #user reached max attempts prior to guessing correctly break loop
        print("You have reached the max amount of attempts of 7. Start over!")
        break

print("Thanks for playing!")  #thank user for attempt
SecretWord = "Python "
guess = ""
guessCount = 0
guessLimit = 3
outOfGusses = False
while guess != SecretWord and not outOfGusses :
    if guessCount < guessLimit:
        guess = input("Enter Your Guess: ")
        guessCount = guessCount + 1
    else:
        outOfGusses = True
if outOfGusses:
    print("YOU LOSE, Out of Gusses!!")
else:
    print("YOU WIN !!")
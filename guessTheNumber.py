import random
print('Hello. What is your name?')
name = input()
print('Hello ' + name + ', I am thinking of a nubmer between 1 and 20.')
secretNubmer = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNubmer:
        print("your guess is too low.")
    elif guess > secretNubmer:
        print("your guess is too high.")
    else:
        break

if guess == secretNubmer:
    print("Good job" + name + "! you guessed my nubmer in " + str(guessesTaken) + " guesses")
else:
    print("Nope. The number i was thinking of was" + str(secretNubmer))

print('You took' + str(guessesTaken) + ' guesses.')
import random 

def number_guessing():

    number = random.randint(1,100)

    attempts = 0

    print("Welcom to the the Number Guessing game")

    print("I am thinking of a number between 1 and 100")

    while True:
        guess = int(input("Take a Guess: "))
        attempts +=1 

        if guess < number:
            print("Too low")

        elif guess > number:

            print("Too high")
          
        else:

            print(f"Congratulations! You have guessed the number {number} in {attempts} attempts.")

            break

    return



number_guessing()



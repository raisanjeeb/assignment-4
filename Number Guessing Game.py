def your_function():
    secret = 7  
    while True:
        guess = int(input("Guess the number: "))

        if guess == -1:   
            print("Exiting game...")
            break
        elif guess < -1:   
            print("Number too small. Try again.")
            continue
        elif guess == secret:  
            print(guess, "Correct!!")
            break
        else:
            print("Wrong guess, try again.")

def main():
    your_function()

main()

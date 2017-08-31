#with help from Jen, classmates and stack overflow
import random
#get random library to generate numbers
min_number = 0 #set the range min and max
max_number = 100


##to update/ user sets range/ count total guesses/ move cursor to end of line

def main(): #create the main program
    #comuter generate a random secret number
    secret_number = random.randint(min_number, max_number)
    print("Welcome to Fun! With Numbers! See if you can guess the secret number...")#intro for user
    print()#blank line
    play_game = input("Would you like to play? press 'Y' to play, 'Q' to exit: ")#user input

    if play_game.lower() =="y": #remove case sensitive from user response
        user_number = int(input("please enter a number between 0-100, inclusive: "))#get user input,
        print("Ok, you selected " + str(user_number)) #convert int to string to allow comparision to computer number
        compare_numbers(user_number, secret_number)# call the function to compare user guess

    else:
        print("Thanks, goodbye!")#let user know they have exited
        exit()

#function for number comparison
def compare_numbers(user_number, secret_number):
    print(secret_number) #for texting, comment during actual play
    #provide hints to user after each guess
    while user_number != secret_number: #when the numbers dont match...
        if user_number < secret_number: # if guess is lexx than somputer
            print("Sorry, you guessed to low.")
            user_number = int(input("Try again."))#get new input
            print("Ok, your new guess is " +str(user_number))#convert int to str for comparing
        elif user_number > secret_number: # if guess is too high..
            print("Nope, your guessed too high.")
            user_number = int(input("Try again."))# new user input
            print("Ok, your new guess is " + str(user_number)) #convert input to str for comparing

        if user_number == secret_number: # if both numbers are the same
            print("Success!! It's a match!")
            play_again = input(" Want to go again? Hit 'Y' for yes, or 'Q' to exit: " )
            print()#blank space
            print()
            if play_again.lower() == "y":
                return main()# if user says yes, call the main function to play again


main()
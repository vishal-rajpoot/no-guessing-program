n=23       # HERE NO. IS DECLARED WHICH SHOULD BE GUESS BY USER TO WIN
no_of_guesses = 1    # HERE NO. OF GUESSES INITIALIZED BY 1
print("\nWELCOME TO NO. GUESSING GAME!!! \t Devloped   by    VISHAL RAJPUT \n ")
print("\nNo. of guesses is limited to only 5 times\n")

while (no_of_guesses<=5):     # WE TOOK WHILE LOOP HERE TO ENTER INTO IT AND WE DECLARED LIMITED NO. OF GUESSES WHICH IS 5 HERE
    guess_no = int(input("Guess your no.: "))  # HERE "CONTROL" WILL TAKE INPUT FROM THE USER.
    if guess_no > n: 
        print("OHHH!!!  Your guess is high. Try again.     hurry up!!!\n")
    elif guess_no < n:
        print("OHHH!!!  Your guess is low. Try again.      hurry up!!! \n")
    else:
        print("CONGRATS!!! YOU WON\n")
        print(no_of_guesses," Guesses you took to finish\n")
        break
    print(5-no_of_guesses,"no of guesses left\n")  # HERE WE SUBTRACT NO. OF GUESSES WITH 5 (BECAUSE "5" IS DECLARED ABOVE TO LIMIT THE NO. OF GUESSES) 
    no_of_guesses = no_of_guesses + 1   # HERE WE INCREMENT NO. OF GUESSES BY 1 

if (no_of_guesses>5):    # IF NO. OF GUESSES ARE EXCEEDEED THEIR LIMIT THEN "CONTROL" WILL PRINT THE NEXT STATEMENT WHICH IS GAME OVER
    print("GAME OVER !!! YOU LOST")

#! /usr/bin/python33


round = 0           # integer round initiated to 0
while True:        # sets up an infinite loop condition
    print('Challenge Question!\n')
    round = round + 1     # increase the round counter
    print('what is your favorite color?')
    answer = input("Your color--> ")    # string ans collected from user
    if answer == 'Blue': # logic to check if user gave correct answer
        print('Correct!')
        break             # break statement escapes the while loop
    elif answer  == 'Red':  
        print('Sorry, the answer was corn.')
        break             # break statement escapes the while loop
    elif answer == 'Yellow':
        print('Sorry, the answer was Syrup.')
        break             # break statement escape
    elif answer == 'Green':
        print('Sorry, the answer was pancake.')
        break             # break statement escape
    elif answer == 'Orange':
        print('Sorry, the answer was hamburger.')
        break             # break statement escape
    elif round == 3:    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was hamburger.')
        break        
    elif answer == 'q'or 'Q':    # logic to ensure round has not yet reached 3
        print('Bye Chicken!')
        break
    else:# if answer was wrong, and round is not yet equal to 3
        print('Sorry. Try again!')

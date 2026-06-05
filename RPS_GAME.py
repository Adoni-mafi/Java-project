#rock, paper and scissors game 
'''how this game work :
#Ask the user to make a chioce 
#if choice is not valid:
#     print an error
# let the computer to make a choice
#     print choices (emojis)
# then we determine the winner 
#Ask the user if they want to continue 
# if not :
#   Terminate the programe 
'''
import random
choices = ('r','p','s')
while True:
    user_input = input('ROCK, PAPER OR SECISSER (r,p,s): ').lower()
    if user_input not in  choices :
        print("Invalid Enter") 
        continue
 
    computer_choice = random.choice(choices).lower()
    print("Computer is : " ,computer_choice)
    print("I Choose : ", user_input)
    if user_input == computer_choice:
       print ("Let's Try Another Game")
    elif (user_input == 'r' and computer_choice =='s')or \
      (user_input == 's' and computer_choice =='p') or \
      (user_input == 'p' and computer_choice =='r') :
         print ('You Win!!')
    else:
        print('You Loss!!')
    should_continue = input('continue? (y/n): ').lower()
    if should_continue =='n':
        break


    

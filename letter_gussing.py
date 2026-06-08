import random
user_letters = {1:'hello', 2: 'this', 3:'be' , 4:'game'}
# 1=='hello'
# 2=='this'
# 3=='be' 
# 4=='game'

# paragraph = "Hello guy, This is Letter gussing game you have to be guss repeatly to win the game.enjoy the game!"

paragraph = ('__1__','guy','__2__','is','letter',
             'gussing','game','you','have','to','__3__',
             'guss','repeatly','to','win','the','game',
             'enjoy','the','__4__')
print('This is the text that you fill:       \n  ', paragraph)
print("1=>'hello'\n2='this'\n3='be'\n4='game'")
while True:

    try:
        user_input = int(input('Enter number that you have to fix it (1,2,3,4): '))
    except ValueError:
        print("Invalid Enter")
        break

    letters=random.choice(list(user_letters.values()))

    print("computer choose!:   ",letters)
    if letters==user_input:
        print ("You win")
    else:

        print('You lose!')
    print("The correct version of the text is: \n", "Hello guy, This is Letter gussing game you have to be guss repeatly to win the game.enjoy the game!")

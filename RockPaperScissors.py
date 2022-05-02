import random
user_action = input('Enter a choice of rock, paper, or scissors: ')
possible_action = ['rock', 'paper', 'scissors']
computer_action = random.choice(possible_action)
print('You chose ' + user_action + '. Computer chose ' + computer_action + '.')

if user_action.lower() ==computer_action:
    print('Both players selected ' + user_action + '. It is a tie.')
elif user_action.lower() == 'rock':
    if computer_action == 'scissors':
        print('Rock smashes scissors. You win.')
    else:
        print('Paper covers rock. You lose.')

elif user_action.lower() == 'scissors':
    if computer_action == 'paper':
        print('Scissors cuts the papers. You win')
    else:
        print('Rock smashes scissors. You lose')

elif user_action.lower() == 'paper':
    if computer_action == 'rock':
        print('Paper covers the rock. You win')
    else:
        print('Scissors cut paper. You lose')



calenderbutton = Button(root, text= "Calender", fg="green", command=open(openpyxl=exam1 range "B2:B21"))
calenderbutton.place (x=200, y=400)

buildingsbutton = Button(root, text="buildings", fg="green",command=open(openpyxl=exam1 range "A2:A8") )
buildingsbutton.place (x=400,y=400)

facultybutton = Button(root, text="Faculty", fg="green",command=open(openpyxl=exam1 range "C2:C13))
facultybutton.place(x=600,y=400)

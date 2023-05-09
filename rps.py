from random import randrange

def rps():
    human_choice='start'
    options=['Rock', 'Paper', 'Scissors', 'Bad Entry'] #maps numbers to game components
    human_choice_alter={'rock':0,'r':0, 'paper':1, 'p':1, 's':2, 'scissors':2, 'scissor':2} # and vice versa for user input

    while True:
    #Take user input
        human_choice=input('Choose rock, paper, scissors, or I quit (to end game):')

        #Standardize the user input
        human_choice=human_choice.lower()
        try:
            human_choice=human_choice_alter[human_choice]
        except:
            if human_choice=='i quit':
                break
            else:
                human_choice=3
        
        #generates a computer
        computer_choice=randrange(0,3)
        print(f"The computer chose {options[computer_choice]}")

        #Determines a winner
        if (human_choice==1 and computer_choice==0) or (human_choice==2 and computer_choice==1) or (human_choice==0 and computer_choice==2):
            print(f"{options[human_choice]} beats {options[computer_choice]}, you win")
        elif (human_choice==computer_choice):
            print(f"{options[human_choice]} draws with {options[computer_choice]}, you draw")
        else:
            print(f"{options[human_choice]} loses to {options[computer_choice]}, you lose")

rps()
#Import random for random numbers.
import random

def RockPaperScissorsLizardSpock():
    #Set up key dictionary.
    #Fill key with every computer choice and then for each computer
    #make another dictionary that will give answers for each user choice.
    key = {}
    key['rock.'] = {'r' : 'It is a draw.', 'p' : 'You win!', 'sc' : 'You lose.', 'l' : 'You win!', 'sp' : 'You lose.'}
    key['paper.'] = {'r' : 'You lose.', 'p' : 'It is a draw.', 'sc' : 'You win!', 'l' : 'You win!', 'sp' : 'You lose.'}
    key['scissors.'] = {'r' : 'You win!', 'p' : 'You lose.', 'sc' : 'It is a draw.', 'l' : 'You lose.', 'sp' : 'You win!'}
    key['lizard.'] = {'r' : 'You win!', 'p' : 'You lose.', 'sc' : 'You win!', 'l' : 'It is a draw.', 'sp' : 'You lose.'}
    key['spock.'] = {'r' : 'You lose.', 'p' : 'You win!', 'sc' : 'You lose.', 'l' : 'You win!', 'sp' : 'It is a draw.'}

    #Set win and lose to 0.
    win = 0
    lose = 0

    #List used for the computer choices, which are random.
    compChoiceList = ['rock.','paper.','scissors.','lizard.','spock.']

    #User choice dictionary that will allow for better printing.
    userChoice = {'r' : 'rock.', 'p' : 'paper.', 'sc' : 'scissors.', 'l' : 'lizard.', 'sp' : 'spock.'}

    #While true loop will continue to run until it a break.
    while True:

        #Make a random choice from 0 to 4 for the computer.
        compChoice = compChoiceList[(int)(random.uniform(0,4))]

        #Get the user input.
        userInput = input('Enter your choice (r)ock, (p)aper, (sc)issors, (l)izard, (sp)ock:')

        #Print the computer choice, your choice and who one,
        #using the dictionary key to look it up.
        print('The computer chose',compChoice,)
        print('You chose',userChoice[userInput])
        print(key[compChoice][userInput], '\n')

        #Check to see if user won, lost or if the game is over.
        #if the game ends, break the while loop.
        if (key[compChoice][userInput] == 'You win!'):
            win = win + 1
        if (key[compChoice][userInput] == 'You lose.'):
            lose = lose + 1
        if (win == 5):
            print('You are a winner! Way to go!!')
            break
        if (lose == 5):
            print('You are a loser. I am sorry.')
            break

        #Print the current standings after each round, which will
        #work even for draws.
        print('The current standings are: You', win, 'Computer', lose, '\n')

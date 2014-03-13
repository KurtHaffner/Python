import random

def RockPaperScissorsLizardSpock():
    key = {}
    key['rock'] = {'r' : 'It is a draw.', 'p' : 'You win!', 'sc' : 'You lose.', 'l' : 'You win!', 'sp' : 'You lose.'}
    key['paper'] = {'r' : 'You lose.', 'p' : 'It is a draw.', 'sc' : 'You win!', 'l' : 'You win!', 'sp' : 'You lose.'}
    key['scissors'] = {'r' : 'You win!', 'p' : 'You lose.', 'sc' : 'It is a draw.', 'l' : 'You lose.', 'sp' : 'You win!'}
    key['lizard'] = {'r' : 'You win!', 'p' : 'You lose.', 'sc' : 'You win!', 'l' : 'It is a draw.', 'sp' : 'You lose.'}
    key['spock'] = {'r' : 'You lose.', 'p' : 'You win!', 'sc' : 'You lose.', 'l' : 'You win!', 'sp' : 'It is a draw.'}

    win = 0
    lose = 0

    compChoiceList = ['rock','paper','scissors','lizard','spock']

    while True:
        compChoice = compChoiceList[(int)(random.uniform(0,4))]
        userInput = input('Enter your choice (r)ock, (p)aper, (sc)issors, (l)izard, (sp)ock:')
        
        print(key[compChoice][userInput], 'The computer chose', compChoice, '.\n')
        
        if (key[compChoice][userInput] == 'You win!'):
            win = win + 1
            print('The current standings are: You', win, 'Computer', lose, '\n')
        if (key[compChoice][userInput] == 'You lose.'):
            lose = lose + 1
            print('The current standings are: You', win, 'Computer', lose, '\n')
        if (win == 5):
            print('You are a winner! Way to go!!')
            break
        if (lose == 5):
            print('You are a loser. I am sorry.')
            break

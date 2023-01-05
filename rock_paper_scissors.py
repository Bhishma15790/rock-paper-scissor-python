import random


def play():
    user = input("what are you picking ! 'r' for rock, 'p' for paper, 's' for scissors \n ")
    computer = random.choice(" 'r', 's', 'p' ")

    if user == computer:
        return 'it is tie'
    
    if is_win(user, computer):
        return 'you won'
    else:
        return 'you lose'
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True 
    

print (play())
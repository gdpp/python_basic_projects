import random

# Return str
def game():
    user = input("'r' for ROCK, 'p' for PAPER, 's' for SCISSORS")
    ia = random.choice(['r', 'p', 's'])
    
    if user == ia:
        return "It's a Tie!!!"

    if is_win(user, ia):
        return "You won!"
    
    return "You lost!"    

# Return bool
def is_win(player, opponent):
    win = False
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        win = True
    
    return win

result = game()

print(result)
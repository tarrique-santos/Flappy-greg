# functions.py
import os

# Carrega o recorde
def load_highscore():
    if os.path.exists('highscore.txt'):
        with open('highscore.txt', 'r') as file:
            return int(file.read())
    return 0

# Salva o recorde
def save_highscore(score):
    with open('highscore.txt', 'w') as file:
        file.write(str(score))

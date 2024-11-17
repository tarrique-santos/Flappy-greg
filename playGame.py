# playGame.py
import pygame
from settings import screen_width, screen_height
from functions import load_highscore
from game_logic import game

# Inicializa o pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Grifo")

# Carrega o recorde
highscore = load_highscore()

# Inicia o jogo
game(screen)

# Finaliza o pygame
pygame.quit()
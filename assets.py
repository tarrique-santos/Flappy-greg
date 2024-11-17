# assets.py
import pygame
from settings import bird_width, bird_height

# Carrega a imagem do grifo e do fundo
bird_img = pygame.image.load('img/skins/grifo.png')
bird_img = pygame.transform.scale(bird_img, (bird_width, bird_height))
bg_img = pygame.image.load('img/backgrounds/paisagem_alternativa2.jpg')

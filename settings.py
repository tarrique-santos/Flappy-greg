# settings.py
import pygame

# Dimensões da tela
screen_width = 600
screen_height = 600

# Cores definidas em RGB
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Variáveis do pássaro
bird_x = 50
bird_y = screen_height // 2
bird_width = 35
bird_height = 35
gravity = 0.8
jump_strength = -10

# Variáveis dos pilares
pipe_width = 50
pipe_velocity = -5

# Velocidade do fundo
bg_velocity = 1  # Movimento lento para a direita

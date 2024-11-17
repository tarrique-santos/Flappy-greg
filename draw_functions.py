# draw_functions.py
import pygame
from settings import screen_width, screen_height, bird_x, pipe_width, white, black, bg_velocity
from assets import bird_img, bg_img

# Função para desenhar o grifo na tela
def draw_bird(screen, bird_y):
    screen.blit(bird_img, (bird_x, bird_y))

# Função para desenhar os pilares
def draw_pillars(screen, pipe_x, pipe_height):
    pillar_width = pipe_width
    broken_gap = 150

    pillar_color = (169, 169, 169)
    border_color = (105, 105, 105)

    # Desenha o pilar primeiro
    pygame.draw.rect(screen, pillar_color, [pipe_x, 0, pillar_width, pipe_height])
    pygame.draw.rect(screen, pillar_color, [pipe_x, pipe_height + broken_gap + 20, pillar_width, screen_height - pipe_height - broken_gap - 20])
    # Desenha as bordas depois para ficarem na frente
    pygame.draw.rect(screen, border_color, [pipe_x - 5, pipe_height - 20, pillar_width + 10, 20])
    pygame.draw.rect(screen, border_color, [pipe_x - 5, pipe_height + broken_gap, pillar_width + 10, 20])

# Função para exibir o fundo em loop com movimento
def draw_background(screen, bg_x):
    bg_x -= bg_velocity - 0.5  # Move o fundo para a direita

    # Desenha o fundo em loop
    rel_x = bg_x % bg_img.get_width()
    screen.blit(bg_img, (rel_x - bg_img.get_width(), 0))
    if rel_x < screen_width:
        screen.blit(bg_img, (rel_x, 0))
    return bg_x

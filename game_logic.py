# game_logic.py
import pygame
from music import play_random_music
from settings import screen_width, screen_height, white, black, green, red
from functions import save_highscore

def game_over_screen(screen, score, highscore):
    # Configuração da tela de Game Over
    font = pygame.font.Font(None, 48)
    screen.fill(white)

    # Exibe o texto "Game Over"
    text = font.render("Game Over", True, red)
    screen.blit(text, [screen_width // 2 - text.get_width() // 2, screen_height // 4])

    # Define as dimensões e posições dos botões
    button_width = 150
    button_height = 50
    button_x = screen_width // 2 - button_width // 2

    # Botão de reiniciar
    restart_button = pygame.Rect(button_x, screen_height // 2, button_width, button_height)
    pygame.draw.rect(screen, green, restart_button)
    font = pygame.font.Font(None, 36)
    restart_text = font.render("Restart", True, black)
    screen.blit(restart_text, [restart_button.x + button_width // 4, restart_button.y + 10])

    # Botão de sair
    quit_button = pygame.Rect(button_x, screen_height // 2 + 70, button_width, button_height)
    pygame.draw.rect(screen, green, quit_button)
    quit_text = font.render("Quit Game", True, black)
    screen.blit(quit_text, [quit_button.x + button_width // 6, quit_button.y + 10])

    # Exibe a pontuação e o recorde
    score_text = font.render(f"Score: {score}", True, black)
    highscore_text = font.render(f"Highscore: {highscore}", True, black)
    screen.blit(score_text, [screen_width // 2 - score_text.get_width() // 2, screen_height // 4 + 50])
    screen.blit(highscore_text, [screen_width // 2 - highscore_text.get_width() // 2, screen_height // 4 + 80])

    pygame.display.flip()

    # Loop de espera para escolher uma opção
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if restart_button.collidepoint(mouse_pos):
                    waiting = False
                    game(screen)  # Reinicia o jogo chamando a função `game`
                if quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()
import random
from settings import (bird_x, bird_y, bird_width, bird_height, gravity, jump_strength, pipe_width,
                      pipe_velocity, screen_height, screen_width, black)
from draw_functions import draw_background, draw_bird, draw_pillars
from functions import save_highscore, load_highscore

def game(screen):
    play_random_music()

    # Inicializa as variáveis do jogo
    bird_y = screen_height // 2
    bird_velocity = 0
    pipe_x = screen_width
    pipe_height = random.randint(150, 400)
    score = 0
    highscore = load_highscore()
    clock = pygame.time.Clock()
    running = True
    bg_x = 0  # Posição inicial do fundo

    while running:
        # Verifica os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = jump_strength  # Pulo do pássaro

        # Atualiza a posição e a velocidade do pássaro
        bird_velocity += gravity
        bird_y += bird_velocity

        # Atualiza a posição dos pilares
        pipe_x += pipe_velocity
        if pipe_x < -pipe_width:
            pipe_x = screen_width
            pipe_height = random.randint(150, 400)
            score += 1
            if score > highscore:
                highscore = score
                save_highscore(highscore)

        # Verifica colisão com as bordas ou os pilares
        if (bird_y < 0 or bird_y > screen_height - bird_height or
                (pipe_x < bird_x + bird_width and pipe_x + pipe_width > bird_x and
                 (bird_y < pipe_height or bird_y + bird_height > pipe_height + 150))):
            running = False

        # Desenha o fundo, o pássaro e os pilares
        bg_x = draw_background(screen, bg_x)  # Fundo com movimento
        draw_bird(screen, bird_y)
        draw_pillars(screen, pipe_x, pipe_height)

        # Exibe a pontuação e o recorde na tela
        font = pygame.font.Font(None, 36)
        score_text = font.render("Pontos: " + str(score), True, black)
        highscore_text = font.render("Recorde: " + str(highscore), True, black)
        screen.blit(score_text, [10, 10])
        screen.blit(highscore_text, [10, 40])

        pygame.display.flip()
        clock.tick(30)

    # Chama a tela de Game Over
    game_over_screen(screen, score, highscore)

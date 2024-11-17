import pygame
import random
import os

# Inicializa o pygame
pygame.init()

# Dimensões da tela
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Título do jogo
pygame.display.set_caption("Flappy Grifo")

# Cores definidas em RGB
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Variáveis do jogo
bird_x = 50
bird_y = screen_height // 2
bird_width = 35
bird_height = 35
bird_velocity = 0
gravity = 0.8
jump_strength = -10

pipe_width = 60
pipe_height = random.randint(150, 400)
pipe_x = screen_width
pipe_velocity = -5
score = 0

# Velocidade do fundo
bg_velocity = 1  # Movimento lento para a direita
bg_x = 0  # Posição inicial do fundo

# Carrega a imagem do grifo e do fundo
bird_img = pygame.image.load('img/skins/grifo.png')
bird_img = pygame.transform.scale(bird_img, (bird_width, bird_height))
bg_img = pygame.image.load('img/backgrounds/paisagem_alternativa2.jpg')

# Carrega o recorde
def load_highscore():
    if os.path.exists('highscore.txt'):
        with open('highscore.txt', 'r') as file:
            return int(file.read())
    return 0

def save_highscore(score):
    with open('highscore.txt', 'w') as file:
        file.write(str(score))

highscore = load_highscore()

# Função para desenhar o grifo na tela
def draw_bird(bird_y):
    screen.blit(bird_img, (bird_x, bird_y))

# Função para desenhar os pilares
def draw_pillars(pipe_x, pipe_height):
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

    create_broken_effect(pipe_x, pipe_height, broken_gap, pillar_width)

    for i in range(5):
        line_x = pipe_x + (i * pillar_width // 5)
        pygame.draw.line(screen, black, (line_x, 0), (line_x, pipe_height), 2)
        pygame.draw.line(screen, black, (line_x, pipe_height + broken_gap + 20), (line_x, screen_height), 2)

def create_broken_effect(pipe_x, pipe_height, broken_gap, pillar_width):
    pygame.draw.rect(screen, white, [pipe_x + pillar_width // 4, pipe_height - 30, pillar_width // 2, 30])
    pygame.draw.rect(screen, white, [pipe_x + pillar_width // 8, pipe_height - 60, pillar_width // 4, 20])
    pygame.draw.rect(screen, white, [pipe_x + pillar_width // 4, pipe_height + broken_gap + 40, pillar_width // 2, 30])
    pygame.draw.rect(screen, white, [pipe_x + pillar_width // 8, pipe_height + broken_gap + 80, pillar_width // 4, 20])

# Função para exibir o fundo em loop com movimento
def draw_background():
    global bg_x
    bg_x -= bg_velocity  # Move o fundo para a direita

    # Desenha o fundo em loop
    rel_x = bg_x % bg_img.get_width()
    screen.blit(bg_img, (rel_x - bg_img.get_width(), 0))
    if rel_x < screen_width:
        screen.blit(bg_img, (rel_x, 0))

# Função para a tela de Game Over
def game_over_screen():
    global highscore
    screen.fill(white)
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over", True, red)
    screen.blit(text, [screen_width // 2 - text.get_width() // 2, screen_height // 4])

    # Centraliza os botões
    button_width = 150
    button_height = 50
    button_x = screen_width // 2 - button_width // 2

    restart_button = pygame.Rect(button_x, screen_height // 2, button_width, button_height)
    pygame.draw.rect(screen, green, restart_button)
    font = pygame.font.Font(None, 36)
    text = font.render("Restart", True, black)
    screen.blit(text, [restart_button.x + button_width // 4, restart_button.y + 10])

    quit_button = pygame.Rect(button_x, screen_height // 2 + 70, button_width, button_height)
    pygame.draw.rect(screen, green, quit_button)
    text = font.render("Quit Game", True, black)
    screen.blit(text, [quit_button.x + button_width // 6, quit_button.y + 10])

    # Exibe a pontuação e o recorde
    score_text = font.render(f"Score: {score}", True, black)
    highscore_text = font.render(f"Highscore: {highscore}", True, black)
    screen.blit(score_text, [screen_width // 2 - score_text.get_width() // 2, screen_height // 4 + 50])
    screen.blit(highscore_text, [screen_width // 2 - highscore_text.get_width() // 2, screen_height // 4 + 80])

    pygame.display.flip()
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
                    game()
                if quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

# Função principal do jogo
def game():
    global bird_y, bird_velocity, pipe_x, pipe_height, score, highscore

    bird_y = screen_height // 2
    bird_velocity = 0
    pipe_x = screen_width
    pipe_height = random.randint(150, 400)
    score = 0
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = jump_strength

        bird_velocity += gravity
        bird_y += bird_velocity

        pipe_x += pipe_velocity
        if pipe_x < -pipe_width:
            pipe_x = screen_width
            pipe_height = random.randint(150, 400)
            score += 1
            if score > highscore:
                highscore = score
                save_highscore(highscore)

        if (bird_y < 0 or bird_y > screen_height - bird_height or
                (pipe_x < bird_x + bird_width and pipe_x + pipe_width > bird_x and
                 (bird_y < pipe_height or bird_y + bird_height > pipe_height + 150))):
            running = False

        draw_background()  # Desenha o fundo com movimento
        draw_bird(bird_y)
        draw_pillars(pipe_x, pipe_height)

        font = pygame.font.Font(None, 36)
        score_text = font.render("Pontos: " + str(score), True, black)
        highscore_text = font.render("Recorde: " + str(highscore), True, black)
        screen.blit(score_text, [10, 10])
        screen.blit(highscore_text, [10, 40])

        pygame.display.flip()
        clock.tick(30)

    game_over_screen()

# Inicia o jogo chamando a função principal
game()

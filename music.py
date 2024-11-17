import pygame
import random
import os

# Lista de caminhos das músicas
music_folder = 'soundtrack'
music_files = [os.path.join(music_folder, "ES_The-Teacher-Fabien-Tell.mp3"),
               os.path.join(music_folder, "ES_Just-a-Drive Away-Raymond-Grouse.mp3")]

def play_random_music(volume=0.1):
    # Inicializa o mixer do pygame para a música
    pygame.mixer.music.stop()  # Para qualquer música que esteja tocando
    selected_music = random.choice(music_files)  # Escolhe aleatoriamente uma música
    pygame.mixer.music.load(selected_music)
    pygame.mixer.music.set_volume(volume)  # Define o volume da música
    pygame.mixer.music.play(-1)  # Toca a música em loop infinito

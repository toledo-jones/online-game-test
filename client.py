import time
import pygame
from network import Network
from player import Player

MENU_COLOR = pygame.Color((72, 61, 139))


import pygame

VERSION = "a"
NUMBER = "v0.024"
MAX_FPS = 120
WIDTH = 500
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")


def draw(win, p1, p2):
    win.fill(MENU_COLOR)
    p1.draw(win)
    p2.draw(win)

def main():
    pygame.init()
    pygame.mixer.music.set_volume(.1)
    MUSIC_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(MUSIC_END)
    clock = pygame.time.Clock()
    # MAIN LOOP
    network = Network()
    player_1 = network.get_player()

    running = True
    while running:
        # EVENT LOOP
        player_2 = network.send(player_1)
        for event in pygame.event.get():
            # ESCAPE BUTTON
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE):
                running = False
                pygame.quit()
                quit()
        player_1.move()
        # DRAW GAME STATES:
        draw(win, player_1, player_2)
        # UPDATE DISPLAY
        pygame.display.update()
        # CLICK CLOCK
        clock.tick(60)



main()
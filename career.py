import pygame
from random import randint
from careermatch import game

pygame.init()
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

#images
bg = pygame.image.load("data/images/FF24.png").convert

#texts
white = (25, 120, 165)
font = pygame.font.Font(None, 36)
text = font.render("Hello, welcome to the Fusion! The Fusion of Football!", True, white)

text_rect = text.get_rect()
text_rect.center = (960, 540)

running = True
while running:
    global frunning
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((52, 52, 52))
    screen.blit(text, text_rect)


    pygame.display.flip()

pygame.quit()
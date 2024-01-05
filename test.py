import pygame
import threading
import math
from packopening import *

screen_width,screen_height = 1920, 1080
"""
def show_splash_screen():
    global bg

    start_time = pygame.time.get_ticks()  # Get the start time

    while pygame.time.get_ticks() - start_time < 5000:  # Display for 5 seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    show_main_menu()
"""
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, (25, 120, 165), self.rect, 2)
        font = pygame.font.Font('data/fonts/justsansbold.otf', 36)
        text_surface = font.render(self.text, True, (240, 240, 240))
        screen.blit(text_surface, (self.rect.centerx - text_surface.get_width() // 2, self.rect.centery - text_surface.get_height() // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def show_main_menu():
    global running, screen
    pygame.init()

    menu_font = pygame.font.Font('data/fonts/justsansbold.otf', 36)
    menu_options = ['Quick Match', 'Career', 'Fusion Team', 'Quit The Game']
    selected_option = 0
    frunning = True

    # Load PNG images for different background colors
    background_1 = pygame.image.load('data/images/quickmatch.png').convert_alpha()
    background_2 = pygame.image.load('data/images/careermatch.png').convert_alpha()
    background_3 = pygame.image.load('data/images/ff24lobby.png').convert_alpha()
    background_4 = pygame.image.load('data/images/quitmatch.png').convert_alpha()

    # Define transition variables
    transitioning = False
    transition_duration = 35  # duration of transition
    transition_frame = 0

    # Touch-friendly buttons
    buttons = [
        Button(screen_width // 4, 400, 300, 50, 'Quick Match'),
        Button(screen_width // 4, 480, 300, 50, 'Career'),
        Button(screen_width // 4, 560, 300, 50, 'Fusion Team'),
        Button(screen_width // 4, 640, 300, 50, 'Quit The Game')
    ]

    while frunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                clear_players_data()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    if button.is_clicked(event.pos):
                        if i == 0:
                            frunning = False
                        elif i == 1:
                            # Handle Career action
                            pass
                        elif i == 2:
                            fusionteam()
                        elif i == 3:
                            pygame.quit()

        # Set the background image based on the selected menu option
        screen.fill((52, 52, 52))
        if selected_option == 0:
            screen.blit(background_1, (0, 0))
        elif selected_option == 1:
            screen.blit(background_2, (0, 0))
        elif selected_option == 2:
            screen.blit(background_3, (0, 0))
        elif selected_option == 3:
            screen.blit(background_4, (0, 0))

        # Define the positions of menu items
        for i, option in enumerate(menu_options):
            color = (25, 120, 165) if i == selected_option else (240, 240, 240)
            text = menu_font.render(option, True, color)
            text_rect = text.get_rect(center=(screen_width // 8, 440 + i * 80))
            screen.blit(text, text_rect)

        # Draw buttons
        for button in buttons:
            button.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(320)

    clear_players_data()
    pygame.quit()
def fusionteam():
    global screen
    
    pygame.init()  
    menu_font = pygame.font.Font('data/fonts/justsansbold.otf', 36)
    menu_options = ['My Team', 'Market', 'Packs', 'Main Menu']
    selected_option = 0
    trunning = True
    
    # Load PNG images for different background colors
    background_1 = pygame.image.load('data/images/myteammenu.png').convert_alpha()
    background_2 = pygame.image.load('data/images/marketmenu.png').convert_alpha()
    background_3 = pygame.image.load('data/images/packsmenu.png').convert_alpha()
    background_4 = pygame.image.load('data/images/quitmatch.png').convert_alpha()
    
    # Define transition variables
    transitioning = False
    transition_duration = 35 # duration of transition
    transition_frame = 0
    
    # Touch-friendly buttons
    buttons = [
        Button(screen_width // 4, 400, 300, 50, 'My Team'),
        Button(screen_width // 4, 480, 300, 50, 'Market'),
        Button(screen_width // 4, 560, 300, 50, 'Packs'),
        Button(screen_width // 4, 640, 300, 50, 'Main Menu')
    ]
    
    while trunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                clear_players_data()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    if button.is_clicked(event.pos):
                        if i == 0:
                            # Handle 'My Team' action
                            pass
                        elif i == 1:
                            # Handle 'Market' action
                            pass
                        elif i == 2:
                            packs()
                        elif i == 3:
                            trunning = False
                            show_main_menu()

        # Set the background image based on the selected menu option
        screen.fill((52, 52, 52))
        if selected_option == 0:
            screen.blit(background_1, (0, 0))
        elif selected_option == 1:
            screen.blit(background_2, (0, 0))
        elif selected_option == 2:
            screen.blit(background_3, (0, 0))
        elif selected_option == 3:
            screen.blit(background_4, (0, 0))
        
        # Draw buttons
        for button in buttons:
            button.draw(screen)
        
        # Define the positions of menu items
        for i, option in enumerate(menu_options):
            color = (25, 120, 165) if i == selected_option else (240, 240, 240)
            text = menu_font.render(option, True, color)
            text_rect = text.get_rect(center=(screen_width // 8, 440 + i * 80))
            screen.blit(text, text_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(320)

    clear_players_data()
    pygame.quit()
def packs():    
    global screen

    pygame.init()

    menu_font = pygame.font.Font('data/fonts/justsansbold.otf', 36)
    menu_options = ['Go Back']
    selected_option = 0

    bluepack_image = pygame.image.load("data/packimages/bluepack90.png")
    yellowpack_image = pygame.image.load("data/packimages/goldpack80.png")
    redpack_image = pygame.image.load("data/packimages/brownpack70.png")
    
    def read_latest_player():
        with open("playersdata.txt", "r") as f:
            lines = f.readlines()
            if lines:
                return lines[-1].strip()  # Return the last line without newline character
        return None
    
    def display_player_info(player_info):
        if player_info:
            text = menu_font.render(player_info, True, (240, 240, 240))
            player_item_y = 100
            text_rect = text.get_rect(center=(screen_width // 5, player_item_y))
            screen.blit(text, text_rect)

    prunning = True
    while prunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                clear_players_data()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_option = (selected_option - 1) % (len(menu_options) + 3)
                elif event.key == pygame.K_RIGHT:
                    selected_option = (selected_option + 1) % (len(menu_options) + 3)
                elif event.key == pygame.K_RETURN:
                    handle_selected_option(selected_option)
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Touch input handling
                if event.button == 1:  # Left mouse button
                    x, y = event.pos
                    handle_touch_input(x, y)

        # ... [rest of your code, including displaying options and images]

        pygame.display.flip()

    pygame.quit()

def handle_selected_option(selected_option):
    if selected_option == 0:
        # Start the game
        fusionteam()
    elif selected_option == 1:
        # Start the game
        packblue70()
    elif selected_option == 2:
        # Start the game
        packblue80()
    elif selected_option == 3:
        # Start the game
        packblue90()

def handle_touch_input(x, y):
    # Assuming a fixed layout where you can calculate touch zones.
    # Here's a basic example for handling touch zones for menu options:
    if y >= 200 and y <= 280:
        if x >= screen_width // 8 - 100 and x <= screen_width // 8 + 100:
            handle_selected_option(0)


#ends of defs and start of main
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
#images
bg = pygame.image.load("data/images/FF24.png").convert_alpha()
bg2 = pygame.image.load("data/images/ff24loading.png").convert_alpha()

#fonts
justsans = pygame.font.Font('data/fonts/justsansbold.otf', 40)

#texts
white = (25, 120, 165)
font = justsans  # Remove pygame from the front
text = font.render("Hello, welcome to the Fusion! The Fusion of Football!", True, white)

text_rect = text.get_rect()
text_rect.center = (960, 540)

def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text
#show_splash_screen()
show_main_menu()
running = True
while running:
    global frunning
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    screen.fill((52, 52, 52))
    screen.blit(text, text_rect)
    #screen.blit(update_fps(), (10,0))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        frunning = True
        show_main_menu()
    
    clock.tick(240)
    pygame.display.flip()
clear_players_data()
pygame.quit()
'''
        player_data_list = read_from_file()
        y_position = 50  # Start position for y-coordinate
        for player_data in player_data_list:
            text_surface = menu_font.render(player_data.strip(), True, (255, 255, 255))
            screen.blit(text_surface, (50, y_position))
            y_position += 30  # Move down for the next player data
'''
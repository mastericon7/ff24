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
    transition_duration = 35 # duration of transition
    transition_frame = 0

    while frunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                clear_players_data()
                return
            elif event.type == pygame.KEYDOWN:
                if not transitioning:
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(menu_options)
                    elif event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(menu_options)
                    elif event.key == pygame.K_RETURN:
                        if selected_option == 0:
                            # Start the game
                           frunning = False
                        elif selected_option == 1:
                            # Show options
                            pass
                        elif selected_option == 2:
                            fusionteam()
                        elif selected_option == 3:
                            pygame.quit()
                    # Start the transition
                    transitioning = True
                    transition_frame = 0

        # Perform the transition effect
        if transitioning:
            if transition_frame < transition_duration:
                alpha = int((transition_frame / transition_duration) * 255)
                current_bg = None

                if selected_option == 0:
                    current_bg = background_1
                elif selected_option == 1:
                    current_bg = background_2
                elif selected_option == 2:
                    current_bg = background_3
                elif selected_option == 3:
                    current_bg = background_4

                current_bg.set_alpha(alpha)
                screen.blit(current_bg, (0, 0))
                transition_frame += 1
            else:
                transitioning = False
        else:
            # Set the background image based on the selected menu option
            if selected_option == 0:
                screen.fill((52, 52, 52))
                screen.blit(background_1, (0, 0))
            elif selected_option == 1:
                screen.fill((52, 52, 52))
                screen.blit(background_2, (0, 0))
            elif selected_option == 2:
                screen.fill((52, 52, 52))
                screen.blit(background_3, (0, 0))
            elif selected_option == 3:
                screen.fill((52, 52, 52))
                screen.blit(background_4, (0, 0))

        # Define the positions of menu items
        menu_item_y = 400
        for i, option in enumerate(menu_options):
            color = (25, 120, 165) if i == selected_option else (240, 240, 240)
            text = menu_font.render(option, True, color)
            text_rect = text.get_rect(center=(screen_width // 8, menu_item_y))
            screen.blit(text, text_rect)
            menu_item_y += 80

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
    while trunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                clear_players_data()
            elif event.type == pygame.KEYDOWN:
                if not transitioning:
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(menu_options)
                    elif event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(menu_options)
                    elif event.key == pygame.K_RETURN:
                        if selected_option == 0:
                            # Start the game
                           pass
                        elif selected_option == 1:
                            # Show options
                            pass
                        elif selected_option == 2:
                            packs()
                        elif selected_option == 3:
                            trunning = False
                            show_main_menu()
                    # Start the transition
                    transitioning = True
                    transition_frame = 0
        # Perform the transition effect
        if transitioning:
            if transition_frame < transition_duration:
                alpha = int((transition_frame / transition_duration) * 255)
                current_bg = None
                if selected_option == 0: #551*738
                    current_bg = background_1
                elif selected_option == 1:
                    current_bg = background_2
                elif selected_option == 2:
                    current_bg = background_3
                elif selected_option == 3:
                    current_bg = background_4
                current_bg.set_alpha(alpha)
                screen.blit(current_bg, (0, 0))
                transition_frame += 1
            else:
                transitioning = False
        else:
            # Set the background image based on the selected menu option
            if selected_option == 0:
                screen.fill((52,52,52))
                screen.blit(background_1, (0, 0))
            elif selected_option == 1:
                screen.fill((52,52,52))
                screen.blit(background_2, (0, 0))
            elif selected_option == 2:
                screen.fill((52,52,52))
                screen.blit(background_3, (0, 0))
            elif selected_option == 3:
                screen.fill((52,52,52))
                screen.blit(background_4, (0, 0))
        # Define the positions of menu items
        menu_item_y = 400
        for i, option in enumerate(menu_options):
            color = (25, 120, 165) if i == selected_option else (240, 240, 240)
            text = menu_font.render(option, True, color)
            text_rect = text.get_rect(center=(screen_width // 8, menu_item_y))
            screen.blit(text, text_rect)
            menu_item_y += 80
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
    stadium_image = pygame.image.load("data/images/stadium_background.png")
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
                    if selected_option == 0:
                        # Start the game
                        prunning = False
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

        screen.fill((52, 52, 52))
        latest_player = read_latest_player()
        display_player_info(latest_player)
        menu_item_y = 200
        for i, option in enumerate(menu_options):
            color = (25, 120, 165) if i == selected_option else (240, 240, 240)
            text = menu_font.render(option, True, color)
            text_rect = text.get_rect(center=(screen_width // 8, menu_item_y))
            screen.blit(text, text_rect)
            menu_item_y += 80

        # Display selectable menu points from images next to each other
        image_width = bluepack_image.get_width()
        image_height = bluepack_image.get_height()
        x_position = (screen_width - 3 * 369 - 2 * 20) // 2
        if selected_option == 1:
            screen.blit(pygame.transform.scale(redpack_image, (369, 469)), (x_position, 500))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x_position - 5, 495, 379, 479), 3)
        else:
            screen.blit(pygame.transform.scale(redpack_image, (369, 469)), (x_position, 500))
        x_position += 389
        if selected_option == 2:
            screen.blit(pygame.transform.scale(yellowpack_image, (369, 469)), (x_position, 500))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x_position - 5, 495, 379, 479), 3)
        else:
            screen.blit(pygame.transform.scale(yellowpack_image, (369, 469)), (x_position, 500))
        x_position += 389
        if selected_option == 3:
            screen.blit(pygame.transform.scale(bluepack_image, (369, 469)), (x_position, 500))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x_position - 5, 495, 379, 479), 3)
        else:
            screen.blit(pygame.transform.scale(bluepack_image, (369, 469)), (x_position, 500))


        pygame.display.flip()
    pygame.quit()

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
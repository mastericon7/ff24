import pygame
import threading
import math

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

def packs():    
    global screen

    pygame.init()

    screen_width, screen_height = 1920, 1080
    screen = pygame.display.set_mode((screen_width, screen_height))

    menu_font = pygame.font.Font('data/fonts/justsansbold.otf', 36)
    menu_options = ['Go Back']
    selected_option = 1

    bluepack_image = pygame.image.load("data/images/bluepack80.png").convert_alpha()
    goldpack_image = pygame.image.load("data/images/goldpack80.png").convert_alpha()
    brownpack_image = pygame.image.load("data/images/brownpack80.png").convert_alpha()

    image_width = 369
    image_height = 469
    image_margin = 20
    num_options = 3
    total_width = num_options * image_width + (num_options - 1) * image_margin
    start_x = (screen_width - total_width) // 2
    start_y = 500

    target_y = start_y  # Initialize target position

    prunning = True
    while prunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % (len(menu_options) + 3)
                    target_y -= 100  # Move the selected option higher
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % (len(menu_options) + 3)
                    target_y += 100  # Move the selected option lower
                elif event.key == pygame.K_LEFT:
                    selected_option = (selected_option - 1) % (num_options + 1)
                    if selected_option != 0:
                        target_y -= 50  # Move the selected pack higher
                elif event.key == pygame.K_RIGHT:
                    selected_option = (selected_option + 1) % (num_options + 1)
                    if selected_option != 0:
                        target_y -= 50  # Move the selected pack higher
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        # Start the game
                        fusionteam()

        screen.fill((52, 52, 52))

        menu_item_y = start_y - 80
        for i, option in enumerate(menu_options):
            color = (25, 120, 165) if i == selected_option else (240, 240, 240)
            text = menu_font.render(option, True, color)
            text_rect = text.get_rect(center=(screen_width // 8, menu_item_y))
            screen.blit(text, text_rect)
            menu_item_y += 80

        # Display selectable menu points from images next to each other with animation
        x_position = start_x
        for i, image in enumerate([bluepack_image, goldpack_image, brownpack_image]):
            if selected_option == i + 1:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x_position - 5, target_y - 5, image_width + 10, image_height + 10), 3)
            screen.blit(pygame.transform.scale(image, (image_width, image_height)), (x_position, target_y))
            x_position += image_width + image_margin

        # Smoothly adjust the target position
        target_y += (start_y - target_y) * 0.1

        pygame.display.flip()
    pygame.quit()

#ends of defs and start of main

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

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
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        frunning = True
        show_main_menu()
    
    pygame.display.flip()
pygame.quit()
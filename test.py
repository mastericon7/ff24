import pygame
import threading
import math

screen_width, screen_height = 1920, 1080

# Define the show_main_menu function
def show_main_menu():
    global running, screen, thread_fusionteam, thread_lock, thread_fusionteam_started

    pygame.init()

    menu_font = pygame.font.SysFont('Sans-Serif', 36)
    menu_options = ['Quick Match', 'Career', 'Fusion Team', 'Quit The Game']
    selected_option = 0
    frunning = True

    # Load PNG images for different background colors
    background_1 = pygame.image.load('data/images/quickmatch.png').convert()
    background_2 = pygame.image.load('data/images/careermatch.png').convert()
    background_3 = pygame.image.load('data/images/ff24lobby.png').convert()
    background_4 = pygame.image.load('data/images/quitmatch.png').convert()

    # Define transition variables
    transitioning = False
    transition_duration = 50  # duration of transition
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
                            if not thread_fusionteam_started:
                                thread_lock.acquire()
                                thread_fusionteam.start()
                                thread_fusionteam_started = True
                                thread_lock.release()  # Release the lock after starting the thread
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


# Define the fusionteam function
def fusionteam():
    global screen

    pygame.init()  
    menu_font = pygame.font.SysFont('Sans-Serif', 36)
    menu_options = ['My Team', 'Market', 'Packs', 'Main Menu']
    selected_option = 0
    trunning = True
    # Load PNG images for different background colors
    background_1 = pygame.image.load('data/images/myteammenu.png').convert()
    background_2 = pygame.image.load('data/images/marketmenu.png').convert()
    background_3 = pygame.image.load('data/images/packsmenu.png').convert()
    background_4 = pygame.image.load('data/images/quitmatch.png').convert()
    # Define transition variables
    transitioning = False
    transition_duration = 50 # duration of transition
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
                            pass
                        elif selected_option == 3:
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
# Initialize pygame
pygame.init()

# Set the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Load images
bg = pygame.image.load("data/images/FF24.png")
bg2 = pygame.image.load("data/images/ff24loading.png")

# Set text
white = (25, 120, 165)
font = pygame.font.Font(None, 36)
text = font.render("Hello, welcome to the Fusion! The Fusion of Football!", True, white)
text_rect = text.get_rect()
text_rect.center = (960, 540)

# Initialize threading
thread_lock = threading.Lock()
thread_fusionteam = threading.Thread(target=fusionteam, args=(screen,))
thread_fusionteam_started = False

# Call the show_main_menu function
show_main_menu()

# Create a variable to control the game loop
running = True

# The main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((52, 52, 52))
    screen.blit(text, text_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        show_main_menu()

    pygame.display.flip()

# Quit pygame
pygame.quit()

import pygame  
import math  

pygame.init()  
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
menu_font = pygame.font.SysFont('Sans-Serif', 36)
menu_options = ['My Team', 'Market', 'Packs', 'Main Menu']
selected_option = 0
frunning = True
# Load PNG images for different background colors
background_1 = pygame.image.load('data/images/myteammenu.png').convert()
background_2 = pygame.image.load('data/images/marketmenu.png').convert()
background_3 = pygame.image.load('data/images/packsmenu.png').convert()
background_4 = pygame.image.load('data/images/quitmatch.png').convert()
# Define transition variables
transitioning = False
transition_duration = 50 # duration of transition
transition_frame = 0
while frunning:
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
                       frunning = False
                    elif selected_option == 1:
                        # Show options
                        pass
                    elif selected_option == 2:
                        pass
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
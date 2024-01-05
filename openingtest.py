import pygame
from packopening import *

pygame.init()
screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode((screen_width, screen_height))

menu_font = pygame.font.Font('data/fonts/justsansbold.otf', 36)
menu_options = ['Go Back']
selected_option = 0

bluepack_image = pygame.image.load("data/images/bluepack80.png")
yellowpack_image = pygame.image.load("data/images/bluepack80.png")
redpack_image = pygame.image.load("data/images/bluepack80.png")

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
                    pass
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
        screen.blit(pygame.transform.scale(bluepack_image, (369, 469)), (x_position, 500))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x_position - 5, 495, 379, 479), 3)
    else:
        screen.blit(pygame.transform.scale(bluepack_image, (369, 469)), (x_position, 500))
    x_position += 389
    if selected_option == 2:
        screen.blit(pygame.transform.scale(yellowpack_image, (369, 469)), (x_position, 500))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x_position - 5, 495, 379, 479), 3)
    else:
        screen.blit(pygame.transform.scale(yellowpack_image, (369, 469)), (x_position, 500))
    x_position += 389
    if selected_option == 3:
        screen.blit(pygame.transform.scale(redpack_image, (369, 469)), (x_position, 500))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x_position - 5, 495, 379, 479), 3)
    else:
        screen.blit(pygame.transform.scale(redpack_image, (369, 469)), (x_position, 500))

    player_data_list = read_from_file()
    y_position = 50  # Start position for y-coordinate
    for player_data in player_data_list:
        text_surface = menu_font.render(player_data.strip(), True, (255, 255, 255))
        screen.blit(text_surface, (50, y_position))
        y_position += 30  # Move down for the next player data


    pygame.display.flip()
pygame.quit()
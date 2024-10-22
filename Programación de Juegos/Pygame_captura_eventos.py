import pygame
import sys

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Captura de eventos en Pygame")

player_x = width // 2
player_y = height // 2
player_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed
            elif event.key == pygame.K_UP:
                player_y -= player_speed
            elif event.key == pygame.K_DOWN:
                player_y += player_speed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Se presionó el botón izquierdo del ratón")
            elif event.button == 3:
                print("Se presionó el botón derecho del ratón")
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            print(f"Se movió el ratón a las coordenadas ({mouse_x}, {mouse_y})")

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y, 50, 50))


    pygame.display.flip()

pygame.quit()


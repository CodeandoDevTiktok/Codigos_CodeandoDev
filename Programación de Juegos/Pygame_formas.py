import pygame
import math

pygame.init()

width = 700
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dibujar formas básicas en Pygame")

rect_color = (255, 0, 0)  # Rojo
circle_color = (0, 255, 0)  # Verde
line_color = (0, 0, 255)  # Azul
polygon_color = (255, 255, 0)  # Amarillo
ellipse_color = (255, 0, 255)  # Magenta
arc_color = (255, 255, 255)  # Blanco

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Limpiar la pantalla con negro

    # Dibujar un rectángulo en la pantalla
    pygame.draw.rect(screen, rect_color, pygame.Rect(50, 50, 120, 100), border_radius=10)
    
    # Dibujar un círculo en la pantalla
    pygame.draw.circle(screen, circle_color, (350, 100), 50)
    
    # Dibujar una línea en la pantalla
    pygame.draw.line(screen, line_color, (550, 50), (600, 150), 5)

    # Dibujar un polígono en la pantalla
    pygame.draw.polygon(screen, polygon_color, [(50, 200), (100, 300), (150, 200)])
    
    # Dibujar una elipse en la pantalla
    pygame.draw.ellipse(screen, ellipse_color, pygame.Rect(250, 200, 200, 100))

    # Dibujar un arco en la pantalla
    pygame.draw.arc(screen, arc_color, pygame.Rect(470, 200, 200, 300), math.pi/4, 3*math.pi/4, 5)
    
    pygame.display.flip()

pygame.quit()
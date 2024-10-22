import pygame

pygame.init()

ancho_ventana = 500
alto_ventana = 400

ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Dibujar rectangulos en Pygame")

color_rectangulo = (255, 0, 0)  # Rojo

jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    ventana.fill((0, 0, 0))

    pygame.draw.rect(ventana, color_rectangulo, pygame.Rect(50, 50, 120, 100), border_radius=10)

    pygame.draw.rect(ventana, color_rectangulo, pygame.Rect(50, 250, 120, 100), 2)

    rectangulo = pygame.Rect(300, 50, 120, 100)
    superficie = pygame.Surface((120,100))
    pygame.draw.rect(superficie, color_rectangulo, (0,0,120,100))
    superficie_rotada = pygame.transform.rotozoom(superficie, 48, 1)
    ventana.blit(superficie_rotada, superficie_rotada.get_rect(center=rectangulo.center))

    pygame.draw.rect(ventana, color_rectangulo, pygame.Rect(300, 250, 120, 100).inflate(15,15))

    pygame.display.flip()

pygame.quit()
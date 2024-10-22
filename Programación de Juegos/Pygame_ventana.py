import pygame

pygame.init()

ancho = 800
alto = 600

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mi juego Tiktok")

imagen_fondo = pygame.image.load("imagen_juego.jpg")

pygame.mixer.music.load("musica_fondo.wav")
pygame.mixer.music.play(-1)

corre_juego = True
while corre_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corre_juego = False

    ventana.blit(imagen_fondo, (0, 0))
    pygame.display.flip()

pygame.quit()
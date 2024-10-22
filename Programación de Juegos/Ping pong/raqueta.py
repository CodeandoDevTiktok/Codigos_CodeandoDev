import pygame
from constantes import *

class Raqueta(pygame.sprite.Sprite):
    def __init__(self, color, ancho, alto):
        super().__init__()
        #Pantalla
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(BLANCO)
        self.image.set_colorkey(BLANCO)

        pygame.draw.rect(self.image, color, [0, 0, ancho, alto])

        self.rect = self.image.get_rect()
        
    def mover_arriba(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def mover_abajo(self, pixels):
        self.rect.y += pixels
        if self.rect.y > ALTO - self.rect.height:
            self.rect.y = ALTO - self.rect.height
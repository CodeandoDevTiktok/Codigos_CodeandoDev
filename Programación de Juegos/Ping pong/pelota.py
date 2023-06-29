import pygame
import random
from constantes import *

class Pelota(pygame.sprite.Sprite):
    def __init__(self, color, ancho, alto):
        super().__init__()
        #Pantalla
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(BLANCO)
        self.image.set_colorkey(BLANCO)

        pygame.draw.rect(self.image, color, [0, 0, ancho, alto])
        #Velocidad
        self.velocidad_x = random.choice([-3, 3])
        self.velocidad_y = random.choice([-3, 3])

        self.rect = self.image.get_rect()

    #Actualiza la posicion de la pelota
    def update(self):
        #Incremento
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        #Rebote
        if self.rect.y < 0 or self.rect.y > ALTO - self.rect.height:
            self.velocidad_y *= -1

    #Reinicia posicion y velocidad
    def reiniciar(self):
        self.rect.x = ANCHO // 2
        self.rect.y = ALTO // 2
        self.velocidad_x = random.choice([-3, 3])
        self.velocidad_y = random.choice([-3, 3])
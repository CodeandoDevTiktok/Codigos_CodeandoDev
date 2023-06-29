import pygame
from raqueta import Raqueta
from pelota import Pelota
from constantes import *

def inicializar_juego():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption("Ping Pong")
    reloj = pygame.time.Clock()
    sprites = pygame.sprite.Group()
    return pantalla, reloj, sprites

def crear_raquetas(sprites):
    raqueta_jugador = Raqueta(NEGRO, 10, 60)
    raqueta_jugador.rect.x = 20
    raqueta_jugador.rect.y = ALTO // 2 - raqueta_jugador.rect.height // 2
    sprites.add(raqueta_jugador)

    raqueta_cpu = Raqueta(NEGRO, 10, 60)
    raqueta_cpu.rect.x = ANCHO - 30
    raqueta_cpu.rect.y = ALTO // 2 - raqueta_cpu.rect.height // 2
    sprites.add(raqueta_cpu)
    return raqueta_jugador, raqueta_cpu

def crear_pelota(sprites):
    pelota = Pelota(NEGRO, 10, 10)
    pelota.reiniciar()
    sprites.add(pelota)
    return pelota

def manejar_eventos():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return True
    return False

def mover_raqueta_jugador(teclas, raqueta_jugador):
    if teclas[pygame.K_w]:
        raqueta_jugador.mover_arriba(5)
    if teclas[pygame.K_s]:
        raqueta_jugador.mover_abajo(5)
        
def mover_raqueta_cpu(raqueta_cpu, pelota):
    #Pelota encima de la raqueta
    if pelota.velocidad_x > 0 and pelota.rect.y < raqueta_cpu.rect.y + raqueta_cpu.rect.height // 2:
        raqueta_cpu.mover_arriba(2)
    #Pelota debajo de la raqueta
    elif pelota.velocidad_x > 0 and pelota.rect.y > raqueta_cpu.rect.y + raqueta_cpu.rect.height // 2:
        raqueta_cpu.mover_abajo(2)

def actualizar_sprites(sprites):
    sprites.update()
    
def comprobar_colisiones(pelota, raqueta_jugador, raqueta_cpu):
    if pygame.sprite.collide_rect(pelota, raqueta_jugador) or pygame.sprite.collide_rect(pelota, raqueta_cpu):
        pelota.velocidad_x *= -1

def actualizar_puntuaciones(pelota, puntos_jugador, puntos_cpu):
    if pelota.rect.x < 0:
        puntos_cpu += 1
        pelota.reiniciar()
    elif pelota.rect.x > ANCHO:
        puntos_jugador += 1
        pelota.reiniciar()
    return puntos_jugador, puntos_cpu

def dibujar_elementos(pantalla, sprites, fuente_puntuacion, puntos_jugador, puntos_cpu):
    pantalla.fill(BLANCO)
    sprites.draw(pantalla)
    puntuacion_jugador = fuente_puntuacion.render(str(puntos_jugador), True, NEGRO)
    puntuacion_cpu = fuente_puntuacion.render(str(puntos_cpu), True, NEGRO)
    pantalla.blit(puntuacion_jugador, (ANCHO // 2 - 50, 10))
    pantalla.blit(puntuacion_cpu, (ANCHO // 2 + 30, 10))
    pygame.display.flip()

def controlar_velocidad(reloj):
    reloj.tick(60)

def main():
    pantalla, reloj, sprites = inicializar_juego()
    raqueta_jugador, raqueta_cpu = crear_raquetas(sprites)
    pelota = crear_pelota(sprites)
    puntos_jugador = 0
    puntos_cpu = 0
    fuente_puntuacion = pygame.font.Font(None, 36)
    terminado = False

    while not terminado:
        terminado = manejar_eventos()
        teclas = pygame.key.get_pressed()
        mover_raqueta_jugador(teclas, raqueta_jugador)
        mover_raqueta_cpu(raqueta_cpu, pelota)
        actualizar_sprites(sprites)
        comprobar_colisiones(pelota, raqueta_jugador, raqueta_cpu)
        puntos_jugador, puntos_cpu = actualizar_puntuaciones(pelota, puntos_jugador, puntos_cpu)
        dibujar_elementos(pantalla, sprites, fuente_puntuacion, puntos_jugador, puntos_cpu)
        controlar_velocidad(reloj)

    pygame.quit()


if __name__ == '__main__':
    main()


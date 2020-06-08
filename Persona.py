import pygame
import time
import random

class Persona(pygame.sprite.Sprite):
    ANCHO = 1000
    ALTO = 720

    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        # cargamnos la imagen
        self.image = pygame.image.load("imagenes/persona.png")
        # rectangulo de la imagen
        self.rect = self.image.get_rect()
        # coordenadas iniciales de la imagen
        self.rect.centerx = posicion[0]
        self.rect.centery = posicion[1]
        self.estado = False
        self.vivo = True

        # velocidad inicial del virus, x, y
        self.velocidad = [2, 2]

    #mover la persona a la nueva posicion
    def mover(self):
        #validar que el virus, se vaya al infino por abajo o por arriba
        if self.rect.bottom >= self.ALTO or self.rect.top <= 0:
            self.velocidad[1] = -self.velocidad[1]
        # validar que el virus, se vaya al infino por la derecha o izquierda
        if self.rect.right >= self.ANCHO or self.rect.left <= 0:
            self.velocidad[0] = -self.velocidad[0]

        self.rect.move_ip(self.velocidad)

    def estadoPersona(self):
        flag = False
        probabilidad = random.randint(0, 11)
        if probabilidad > 2:
            #self.image = pygame.image.load("imagenes/persona.png")
            self.estado = False
            self.vivo = True
            flag = True
        else:
            print("La persona Muere")
            # self.image = pygame.image.load("imagenes/craneo.png")
            self.vivo = False
            flag = False
        return flag
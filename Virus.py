import pygame


class Virus(pygame.sprite.Sprite):
    ANCHO = 1000
    ALTO = 720
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #cargamnos la imagen
        self.image = pygame.image.load("imagenes/virus.png")
        #rectangulo de la imagen
        self.rect = self.image.get_rect()
        #coordenadas iniciales de la imagen
        self.rect.centerx = self.ANCHO / 2
        self.rect.centery = self.ALTO / 2

        #velocidad inicial del virus, x, y
        self.velocidad = [2, 2]

    #mover la blita a la nueva posicion
    def mover(self):
        #validar que el virus, se vaya al infino por abajo o por arriba
        if self.rect.bottom >= self.ALTO or self.rect.top <= 0:
            self.velocidad[1] = -self.velocidad[1]
        # validar que el virus, se vaya al infino por la derecha o izquierda
        if self.rect.right >= self.ANCHO or self.rect.left <= 0:
            self.velocidad[0] = -self.velocidad[0]

        self.rect.move_ip(self.velocidad)
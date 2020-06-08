import pygame
from Persona import Persona
class Personas(pygame.sprite.Group):
    def __init__(self, cantidad):
        pygame.sprite.Group.__init__(self)
        posicion = [0, 20]
        for i in range(cantidad):
            persona = Persona(posicion)
            self.add(persona)
            persona.mover()
            posicion[0] += 40



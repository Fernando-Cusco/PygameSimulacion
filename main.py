import pygame
import sys
import random
from Virus import Virus
from Persona import Persona
from Conjunto import Personas
contagiados = 0
muertes = 0
ANCHO = 1000
ALTO = 720
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pandemia")
color_fondo = (173, 173, 173)
#reloj
reloj = pygame.time.Clock()

virus = Virus()
# personas = Personas(5)

personas = []
sanos = 50
for i in range(sanos):
    x = random.randint(10, 800)
    y = random.randint(10, 700)
    posicion = [x, y]
    persona = Persona(posicion)
    personas.append(persona)


def mensajes():
    fuente = pygame.font.SysFont('Arial', 20)
    texto = fuente.render("Personas sanas: "+str(sanos), True, (255, 255, 255))
    pos = texto.get_rect()
    pos.topleft = [0, 0]
    texto1 = fuente.render("Personas contagiadas: " + str(contagiados), True, (255, 45, 0))
    pos1 = texto1.get_rect()
    pos1.topleft = [0, 20]
    texto2 = fuente.render("Personas muertas: " + str(muertes), True, (0, 0, 0))
    pos2 = texto2.get_rect()
    pos2.topleft = [0, 40]

    pantalla.blit(texto, pos)
    pantalla.blit(texto1, pos1)
    pantalla.blit(texto2, pos2)

while True:
    #definimos los fps
    reloj.tick(25)

    #eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

    #movemos el virus
    virus.mover()
    # persona.mover()

    #colisiones virs y la persona



    #rellenamos la pantalla
    pantalla.fill(color_fondo)
    mensajes()
    #dibijamos a las persona
    for persona in(personas):
        pantalla.blit(persona.image, persona.rect)
        persona.mover()
        if pygame.sprite.collide_rect(virus, persona) and persona.estado == False and persona.vivo:
            persona.image = pygame.image.load("imagenes/infectado.png")
            persona.estado = True
            contagiados += 1
            sanos -= 1


            if persona.estadoPersona() and persona.vivo:
                contagiados -= 1
                sanos += 1
            elif not persona.estadoPersona() and not persona.vivo:
                persona.image = pygame.image.load("imagenes/craneo.png")
                muertes += 1
            print("Personas => Sanas: ", sanos, "Contagiados: ", contagiados, " Muertos: ",muertes)

    # personas.draw(pantalla)
    #dibujamos el virus en las coordenadas del objeto
    pantalla.blit(virus.image, virus.rect)
    #actuliza los elemenots de la pantalla
    pygame.display.flip()
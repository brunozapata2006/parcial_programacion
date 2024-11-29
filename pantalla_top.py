import pygame
from funciones import *
from colores import *
from configuraciones import *

def dibujar_pantalla_top_mundial(pantalla):  

    pygame.display.set_caption("Vamos a cargar preguntas!")
    
    ruta_fondo = 'assets/fondo.jpg'
    imagen_fondo = pygame.image.load(ruta_fondo)
    
    pantalla.blit(imagen_fondo, (0, 0))
    
    pos_mouse = pygame.mouse.get_pos                                           #x   #y   
    boton_volver_menu = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse)
    
    pygame.display.flip()
    
    return boton_volver_menu
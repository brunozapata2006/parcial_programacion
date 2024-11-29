from colores import *
import pygame
from pygame import surface


def guardar_pregunta_juegos(path, pregunta, respuesta1, respuesta2, respuesta3, correcta):
    with open(path, 'a', encoding='utf-8') as archivo:
        pregunta_agregada = (f'"{pregunta}","{respuesta1}","{respuesta2}","{respuesta3}","{correcta}"\n')
        archivo.write(pregunta_agregada)
        print("pregunta agregada :D")

# Función para dibujar botones transparentes con detección de hover
def dibujar_texto_con_boton_transparente(pantalla:surface, texto:str, x:int, y:int, ancho:int, alto:int, color_normal:tuple, color_hover:tuple, pos_mouse):
    '''
    Plantilla Documentacion
    ¿Para que sirve? xxx
    ¿Que parametro acepta?
    -pantalla: 
    -texto: texto a escribir en el boton.
    -x : posicion x del rectagulo en la pantallat
    -y :  posicion y del rectagulo en la pantalla
    -ancho: ancho del cuadrado
    -alto: alto del cuadrado
    -color_normal: color que se muestra al no pasar el mouse encima del texto
    -color_hover: ccolor que se muestra al pasar el mouse encima del texo
    -pos_mouse: la posicion actual del mouse
    ¿Que Retorna?
    -retorna el texto ya renderizado con un boton transparente de fondo
    '''
    pos_mouse = pygame.mouse.get_pos()    
    color_texto = color_hover if x <= pos_mouse[0] <= x + ancho and y <= pos_mouse[1] <= y + alto else color_normal
    fuente = pygame.font.SysFont("Showcard Gothic", 30)
    texto_renderizado = fuente.render(texto, True, color_texto)
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))
    mostrar_texto = pantalla.blit(texto_renderizado, texto_rect)
    
    return mostrar_texto
    
#jugar al preguntados
    
    
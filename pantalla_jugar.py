import pygame
from funciones import *
from colores import *
from configuraciones import *

def dibujar_pantalla_juego(pantalla):  
    '''
    Plantilla Documentacion
    ¿Para que sirve? Dibuja uma pantalla que muestra las preguntas para poder jugar
    ¿Que parametro acepta?
    -None
    ¿Que Retorna?
    -boton_menu : un boton con colision que devuele al menu principal
    '''
    pygame.display.set_caption("A jugar preguntados!")
    
    ruta_fondo = 'assets/fondo.jpg'
    imagen_fondo = pygame.image.load(ruta_fondo)
    
    pantalla.blit(imagen_fondo, (0, 0))
    
    pos_mouse = pygame.mouse.get_pos                                           #x   #y
    boton_volver_menu = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse)
    
    pygame.display.flip()
    
    return boton_volver_menu

def cargar_las_preguntas(archivo_csv):
    '''
    Plantilla Documentacion
    ¿Para que sirve? Sirve para cargar preguntas en la funcion panatalla_jugar
    ¿Que parametro acepta?
    -archivo-> csv : archivo desde donde se va cargar las preguntas
    ¿Que Retorna?
    -la lista de preguntas
    '''
    with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
        preguntas = []
        lectura = archivo.readlines()
        # encabezados = lectura[0].split(',')

        for lectura in lectura[1:]:
            fila = lectura.split(',')
            if len(fila) == 5:
                pregunta,respuesta1,respuesta2,respuesta3,respuesta4 = fila
                preguntas.append(pregunta,respuesta1,respuesta2,respuesta3,respuesta4)
    return preguntas

# def mostrar_pregunta(pantalla):
#     with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
#     # path = "preguntas.csv"
#     # lista_preguntas = cargar_preguntas(path)
#         for lista_preguntas in archivo:
#             pass


# 
# ruleta = pygame.image.load('assets/ruleta.png')


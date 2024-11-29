import os
import pygame
from configuraciones import *
from funciones import *
from colores import *
import time
from pantalla_jugar import *
from pantalla_top import *
from pantalla_cargar_preguntas import *
from pantalla_easter_egg import *
from pantalla_menu import *

# Inicializar Pygame
pygame.init()
pygame.mixer.init()
pygame.font.init()




#cargar icono gatito :#
icono = pygame.image.load('assets/preguntados.jpg')
pygame.display.set_icon(icono)

#texto de arriba o.o
pygame.display.set_caption("Preguntados")

#pantalla principal y fondo 
pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)

ruta_fondo = "assets/fondo.jpg"
imagen_fondo = pygame.image.load(ruta_fondo)
imagen_fondo_escalar = pygame.transform.scale(imagen_fondo, (ANCHO,ALTO))


# Opciones de menú
jugar = True
estado = "menu"  # Puede ser "menu" , "juego", "ver tops mundiales" o "cargar preguntas"

while jugar:
    pos_mouse = pygame.mouse.get_pos()
    #print(pos_mouse)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugar = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = evento.pos
            
            #estando en el menu
            if estado == "menu":
                # Detectar clics en botones del menú principal
                if 300 <= pos[0] <= 500 and 100 <= pos[1] <= 150:
                    print("Jugar")
                    estado = "juego"
                    
                elif 300 <= pos[0] <= 500 and 200 <= pos[1] <= 250:
                    print("Ver top mundiales")
                    estado = "Ver top mundiales"
                    
                elif 700  <= pos[0] <= 740 and 550 <= pos[1] <= 580: 
                    print("Saliendo...") # 625, 550
                    jugar = False
                    
                elif 300 <= pos[0] <= 500 and 300 <= pos[1] <= 350:
                    print("entrando a preguntas")
                    estado = "agregar preguntas"
                
                elif 10 <= pos[0] <= 0 and 10 <= pos[1] <= 0:
                    estado = "cargar_pregunta"
                    
                elif 600  <= pos[0] <= 680 and 550 <= pos[1] <= 580:
                    print("y esto?")
                    estado = "o.O"
                    
            #estando en el juego
            elif estado == "juego":
                if botones_de_juego.collidepoint(pos):
                    print("Volver al menú")
                    estado = "menu"
                    
            #estando en top mundiales
            elif estado == "Ver top mundiales":
                if botones_tops_mundiales.collidepoint(pos):
                    print("Volver al menú")
                    estado = "menu"

            #estando en las preguntas
            elif estado == "entrando preguntas":
                if boton_preguntas.collidepoint(pos):
                    print("Volver al menu")
                    estado = "menu"
                    #Faltaria agregar el botón 'agregar preguta' y sus repectivas posiciones
            
            
            elif estado == "agregar preguntas":
                if boton_cargar.collidepoint(pos):
                    print("boton pregunta")
                    estado = "agregar preguntas"
            #estando en ?
            elif estado == "o.O":
                if botones_easter_egg.collidepoint(pos):
                    print("Volver al menu")
                    estado = "menu"

    # Redibujar pantalla según el estado'''
    pantalla.fill((0, 0, 0))  # Limpia la pantalla
    if estado == "menu":
        pantalla.blit(imagen_fondo_escalar, (0, 0))  # Fondo del menú
        botones_menu = menu_botones(pantalla, pos_mouse)
    
    #redibujar pantalla a juego
    elif estado == "juego":
        botones_de_juego = dibujar_pantalla_juego(pantalla) 
        
    #redibujar pantalla de los tops mundiales    
    elif estado == "Ver top mundiales":
        botones_tops_mundiales = dibujar_pantalla_top_mundial(pantalla)
        
    #redibujar pantalla a pregutas
    elif estado == "entrando preguntas":
        boton_preguntas = dibujar_botones_cargar_preguntas(pantalla)
        # if modo_agregar_preguntas == True:
        #     ventana_agregar_pregunta(evento, pantalla)
    
    elif estado == "agregar preguntas":
        boton_cargar = hola(pantalla)

    #redibujar pantalla a ?
    elif estado == "o.O":
        botones_easter_egg = easter_egg(pantalla)
    
    pygame.display.flip()

pygame.quit()













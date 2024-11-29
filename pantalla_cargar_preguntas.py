import pygame
from funciones import *
from colores import *
from configuraciones import *


def dibujar_botones_cargar_preguntas(pantalla):  
    '''
    Plantilla Documentacion
    ¿Para que sirve? Dibuja una pantalla que muestra un input para poder agregar preguntas
    ¿Que parametro acepta?
    -pantalla: dibuja una nueva pantalla con el ancho y el alto
    ¿Que Retorna?
    -boton_menu_preguntas : un boton con colision que devuele al menu principal
    '''
    pygame.display.set_caption("Vamos a cargar preguntas!")
    
    ruta_fondo = 'assets/fondo.jpg'
    imagen_fondo = pygame.image.load(ruta_fondo)
    
    pantalla.blit(imagen_fondo, (0, 0))
    
    #estado = "estrando preguntas"
    pos_mouse = pygame.mouse.get_pos                                              #x   #y   
    boton_volver_menu_preguntas = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse)
    boton_agregar_preguntas = dibujar_texto_con_boton_transparente(pantalla, "agregar preguntas",300, 200 ,200, 50, WHEAT1, VIOLET, pos_mouse)

    pygame.display.flip()
    
    return boton_volver_menu_preguntas

def ventana_agregar_pregunta(eventos,pantalla):
    pregunta = ''
    respuesta_1 = ''
    respuesta_2 = ''
    respuesta_3 = ''
    respuesta_correcta = ''
    cuadro = None

    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if 100 <= evento.pos[0] <= 700:

                if 50 <= evento.pos[1] <= 90:
                    cuadro = pregunta
                elif 100 <= evento.pos[1] <= 140:
                    cuadro = respuesta_1
                elif 150 <= evento.pos[1] <= 190:
                    cuadro = respuesta_2
                elif 200 <= evento.pos[1] <= 240:
                    cuadro = respuesta_3  
                elif 300 <= evento.pos[1] <= 340:
                    cuadro = respuesta_correcta
                else:
                    cuadro = None
        if evento.type == pygame.KEYDOWN:
            if cuadro:
                if evento.key == pygame.K_BACKSPACE:
                    if cuadro == "pregunta":
                        pregunta = pregunta[:-1] #<-- sirve para borrar un texto si la persona lo desea
                    elif cuadro == "respuesta_1":
                        respuesta_1 = respuesta_1[:-1]
                    elif cuadro == "respuesta_1":
                        respuesta_2 = respuesta_2[:-1]
                    elif cuadro == "respuesta_1":
                        respuesta_3 = respuesta_3[:-1]
                    elif cuadro == "respuesta_correcta":
                        respuesta_correcta = respuesta_correcta[:-1]
                else:
                    if cuadro == "pregunta":
                        pregunta += evento.unicode #<-- al presionar la tecla "A", el += junto con el .unicode actualiza  por ej: la variable correcta a "A" y no a un str vacio
                    elif cuadro == "respuesta_1":
                        respuesta_1 += evento.unicode
                    elif cuadro == "respuesta_2":
                        respuesta_2 += evento.unicode
                    elif cuadro == "respuesta_3":
                        respuesta_3 += evento.unicode
                    elif cuadro == "respuesta_correcta":
                        respuesta_correcta += evento.unicode

    pos_mouse = pygame.mouse.get_pos 
    pregunta = dibujar_texto_con_boton_transparente(pantalla, "Pregunta", 300, 100, 200, 50, WHEAT1, RED1, pos_mouse)
    respuesta_1 = dibujar_texto_con_boton_transparente(pantalla, "Respuesta 1", 300, 200, 200, 50, WHEAT2, RED1, pos_mouse)
    respuesta_2 = dibujar_texto_con_boton_transparente(pantalla, "Respuesta 2", 300, 300, 200, 50, WHEAT2, RED1, pos_mouse)
    respuesta_3 = dibujar_texto_con_boton_transparente(pantalla, "Respuesta 3", 300, 400, 200, 50, WHEAT3, RED1, pos_mouse)
    respuesta_correcta = dibujar_texto_con_boton_transparente(pantalla, "Respuesta correcta", 300, 500, 200, 50, WHEAT3, RED1, pos_mouse)

    

    pygame.draw.rect(pantalla, SKYBLUE, (300,600,200,50))
    fuente = pygame.font.SysFont("Showcard Gothic", 30)
    texto_boton = fuente.render("Guardar pregunta", True, WHEAT4)
    pantalla.blit(texto_boton, (300 + (200 - texto_boton.get_width()) // 2, 400 + (50 - texto_boton.get_height()) // 2))

    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if 300 <= evento.pos[0] <= 500 and 40 <= evento.pos[1] <= 450:
                guardar_pregunta_juegos(pregunta, respuesta_1, respuesta_2, respuesta_3, respuesta_correcta)
                pregunta = ''
                respuesta_1 = ''
                respuesta_2 = ''
                respuesta_3 = ''
                respuesta_correcta = ''
                break
            
    return pregunta, respuesta_1, respuesta_2, respuesta_3, respuesta_correcta



def hola(pantalla):
    pos_mouse = pygame.mouse.get_pos 
    pregunta = dibujar_texto_con_boton_transparente(pantalla, "Pregunta", 300, 100, 200, 50, WHEAT1, RED1, pos_mouse)
    respuesta_1 = dibujar_texto_con_boton_transparente(pantalla, "Respuesta 1", 300, 200, 200, 50, WHEAT2, RED1, pos_mouse)
    respuesta_2 = dibujar_texto_con_boton_transparente(pantalla, "Respuesta 2", 300, 300, 200, 50, WHEAT2, RED1, pos_mouse)
    respuesta_3 = dibujar_texto_con_boton_transparente(pantalla, "Respuesta 3", 300, 400, 200, 50, WHEAT3, RED1, pos_mouse)
    respuesta_correcta = dibujar_texto_con_boton_transparente(pantalla, "Respuesta correcta", 300, 500, 200, 50, WHEAT3, RED1, pos_mouse)
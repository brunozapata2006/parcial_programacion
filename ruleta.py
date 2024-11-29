import pygame
import sys
import random
from configuraciones import *

fps = 60

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Ruleta Giratoria")
#
ruta_ruleta = "assets/ruleta.png"
imagen_ruleta = pygame.image.load(ruta_ruleta)
imagen_ruleta_escalada = pygame.transform.scale(imagen_ruleta, (550 ,550))
# Carga de la imagen de fondo
ruta_fondo = "assets/fondo.jpg"
imagen_fondo = pygame.image.load(ruta_fondo)
imagen_fondo_escalar = pygame.transform.scale(imagen_fondo, (WIDTH, HEIGHT))

# Carga de la imagen de la ruleta
flecha_2 = pygame.image.load('assets/r1.png')
ruleta_img = pygame.transform.scale(flecha_2, (200, 200))  # Escalar si es necesario

# Centro de la ruleta
ruleta_rect = ruleta_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Ángulo inicial y velocidad
angle = 0
velocity = 0
target_angle = 0
slowing_down = False

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Función para reiniciar el giro
def start_spin():
    global velocity, target_angle, slowing_down
    velocity = random.randint(20, 30)  # Velocidad inicial aleatoria
    target_angle = random.randint(0, 359)  # Ángulo final aleatorio
    slowing_down = False  # Restablecer desaceleración

# Bucle principal
running = True
start_spin()  # Inicia el primer giro
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Detecta si el clic está dentro del área de la ruleta
            if ruleta_rect.collidepoint(event.pos):
                start_spin()  # Reinicia el giro

    # Dibujar el fondo
    screen.blit(imagen_fondo_escalar, (0, 0))

    # Actualiza la rotación
    if velocity > 0:
        angle += velocity
        angle %= 360  # Mantener el ángulo entre 0-359
        if slowing_down:
            velocity -= 0.1  # Reduce la velocidad gradualmente
    else:
        # Asegura que se detenga en el ángulo objetivo
        angle = target_angle

    # Comienza a desacelerar cuando está cerca del ángulo objetivo
    if not slowing_down and abs(angle - target_angle) <= 50:
        slowing_down = True

    # Rotación de la imagen
    rotated_img = pygame.transform.rotate(ruleta_img, angle)
    rotated_rect = rotated_img.get_rect(center=ruleta_rect.center)

    # Actualiza el rectángulo para detección de clics
    ruleta_rect = rotated_rect  # Importante: Actualizar al nuevo rectángulo rotado

    # Dibuja la ruleta rotad9
    screen.blit(imagen_ruleta_escalada, (WIDTH // 6, HEIGHT // 19))
    screen.blit(rotated_img, rotated_rect.topleft)

    # Actualiza la pantalla
    pygame.display.flip()

    # Control de la velocidad del bucle
    clock.tick(fps)

# Salir de Pygame
pygame.quit()
sys.exit()
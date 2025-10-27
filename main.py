import datetime
import time
import pygame
import ctypes


ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

# Defina o horário
hora_alarme = "06:15"  # Formato HH:MM
pygame.mixer.init()
# Coloque o nome do arquivo do audio que você deseja usar como alarme
som_alarme = "ssvid.net--Passarinho-alarme-nuclear-estourado.mp3"
# Loop principal
while True:
    agora = datetime.datetime.now().strftime("%H:%M")
    print(f"Hora atual: {agora}")
    if agora == hora_alarme:
        print("Alarme tocando!")
        pygame.mixer.music.load(som_alarme)
        pygame.mixer.music.play(-1)
        time.sleep(500)  # Toca por 500 segundos
        break
    time.sleep(20)  # Verifica a cada 20 segundos

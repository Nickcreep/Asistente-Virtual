# |--------------------------------------|
# |     Librerías estándar de Python     |
# |--------------------------------------|

import webbrowser  # 🌐 Permite abrir páginas web desde Python
import subprocess  # 💻 Permite ejecutar programas externos
import urllib.parse  # 🔗 Permite trabajar con URLs y codificar texto
import os  # 🗂 Permite interactuar con el sistema operativo
from datetime import datetime  # ⏰ Para trabajar con fechas y horas
import re  # 📝 Expresiones regulares para buscar patrones en texto
import random  # 🎲 Para elegir frases aleatorias (personalidad)
import winsound  # 🔊 Para reproducir sonido al despertar
import time  # ⏳ Para pequeños descansos y manejo de errores

# Librería externa para interpretar fechas en lenguaje natural
import dateparser  # 📅 Convierte frases como "mañana a las 3pm" en objetos de fecha

# |--------------------------------------|
# |     Librerías externas de Python     |
# |--------------------------------------|
# Librerías que necesitamos instalar con pip
import speech_recognition as sr  # 🎤 Convierte voz a texto (reconocimiento de voz)
#import pyttsx3 as voz  # 🗣 comentado porque usaremos win32com
import win32com.client  # 🔊 Motor TTS de Windows, reemplaza pyttsx3, lo reeemplace porque me hacia doler la cabeza de tanto que intentaba jajajaj, pero en fin creo que win32com es mejor en Windows no crees?

# |--------------------------------------|
# |     Inicialización del motor TTS     |
# |--------------------------------------|
speaker = win32com.client.Dispatch("SAPI.SpVoice")  # 🔊 Inicializa el motor de voz

# Seleccionamos voz española (Microsoft Sabina Desktop, Español México), en caso de que no esté instalada, se usará la voz predeterminada
for i in range(speaker.GetVoices().Count):
    v = speaker.GetVoices().Item(i)
    if "Sabina" in v.GetAttribute("Name"): # 🎙 Elegimos la voz ya instalada de Windows, en este caso usare la de "Sabina" porque el asistente es mujer! Creo....🤔
        speaker.Voice = v  

speaker.Rate = -2  # Ajuste de velocidad (más tierna)
speaker.Volume = 90  # Ajuste de volumen

# |--------------------------------------|
# |              Función say             |
# |--------------------------------------|
def estado_led(accion="escuchando"):
    """
    Muestra un LED virtual:  #O algo asi XD
    - 🟢 Escuchando
    - 🔵 Hablando
    Solo se muestra cuando Cortana está activa.
    """
    if modo_reposo:
        return  # Nada en modo reposo
    if accion == "escuchando":
        print("🟢 [ESCUCHANDO]")
    elif accion == "hablando":
        print("🔵 [HABLANDO]")

def say(text):
    if not modo_reposo:
        estado_led("hablando")  # Cambia LED a “hablando”
    print(f"(Voz): {text}")  # 💻 Muestra el texto en consola
    try:
        speaker.Speak(text)  # 🔊 Convierte el texto en voz
    except Exception as e:
        if not modo_reposo:
            print(f"❗ Error al hablar: {e}")

# |--------------------------------------|
# |      Configuración del usuario       |
# |--------------------------------------|
nombre_usuario = "Nick"  # 👤 Cambia esto por tu nombre si quieres 🤔
modo_reposo = True  # 😴 Cortana inicia dormida
sonido_despertar = "C:\\Windows\\Media\\Windows Notify.wav"  # 🎵 Sonido al despertar

# |--------------------------------------|
# |      Personalidad y emociones        |
# |--------------------------------------|
emocion_actual = "neutral"  # neutral | feliz | emocionada

# Diccionario de frases según tipo y emoción
#😁Yo lo llame "Cortana" porque soy muy fan de halo jejeje
#Pueden cambiar el nombre a su gusto 👌

personalidad = {
    "despertar": [
        f"Hola {nombre_usuario} Ya estoy aquí",
        f"Hey {nombre_usuario} Lista para ayudarte",
        f"Cortana activa, dime que hacer"
    ],
    "reposo": [
        "Entrando en modo reposo",
        "Me quedaré quietecita un rato"
    ],
    "saludo": [
        f"Holaa {nombre_usuario}",
        f"¡Hey! ¿qué vamos a hacer hoy?"
    ],
    "feliz": [
        "Jejeje eso suena genial",
        "Me gusta ayudarte"
    ],
    "emocionada": [
        "¡Eso es épicooo!",
        "¡Vamos con todo!"
    ],
    "error": [
        "No entendí eso",
        "¿Puedes repetirlo, porfis?"
    ],
    "despedida": [
        f"Hasta luego {nombre_usuario} ",
        "Cuídate mucho, nos vemos pronto"
    ]
}

def decir(tipo):
    global emocion_actual
    frase = random.choice(personalidad[tipo])
    say(frase)

def despertar():
    # 🎵 Reproduce sonido
    try:
        winsound.PlaySound(sonido_despertar, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except Exception as e:
        print(f"❗ No se pudo reproducir el sonido: {e}")
    # 🗣 Dice nombre + frase tierna
    decir("despertar")

# |--------------------------------------|
# |       Diccionarios de recursos       |
# |--------------------------------------|
# Diccionarios guardan pares clave:valor
# Aquí guardamos sitios web, aplicaciones y juegos

# Sitios web que podemos abrir con un comando
sites = {
    'google': 'https://www.google.com',
    'youtube': 'https://www.youtube.com',
    'instagram': 'https://www.instagram.com',
    'facebook': 'https://www.facebook.com',
    'twitter': 'https://www.twitter.com',
    'linkedin': 'https://www.linkedin.com',
    'reddit': 'https://www.reddit.com',
    'amazon': 'https://www.amazon.com',
    'wikipedia': 'https://www.wikipedia.org',
    'netflix': 'https://www.netflix.com'
}

# Aplicaciones que podemos abrir en Windows
#Yo elegi estas apps porque son las que mas uso, pero pueden agregar las que quieran
apps = {
    'calculadora': 'calc',
    'bloc de notas': 'notepad',
    'steam': r'C:\Program Files (x86)\Steam\Steam.exe',
    'vlc': r'C:\Program Files (x86)\VideoLAN\VLC\vlc.exe'
}

# Juegos de Steam que se pueden abrir con su URI, si están instalados, si no, dará error
#PD para tener la URI de un juego, busca en Google "como encontrar steam game url [nombre del juego]" o algo asi
#Si no puede dar segundo click luego vas a propiedades en el juego y luego dice dirección de la URL lo copias y pegas
#Ejemplo: steam://rungameid/242760 para The Forest
steam_games = {
    'the forest': 'steam://rungameid/242760',
    'counter strike': 'steam://rungameid/730',
    'csgo': 'steam://rungameid/730',
    'dota 2': 'steam://rungameid/570',
    'left 4 dead 2': 'steam://rungameid/550',
    'portal': 'steam://rungameid/400',
    'terraria': 'steam://rungameid/105600',
    'gta v': 'steam://rungameid/271590',
    'gta 5': 'steam://rungameid/271590'
}

# |--------------------------------------|
# |         Funciones auxiliares         |
# |--------------------------------------|
def buscar_en_google(termino):
    #"""🔍 Busca un término en Google"""
    query = urllib.parse.quote_plus(termino) # Codifica el texto para URL
    url = f"https://www.google.com/search?q={query}" # Construye la URL
    webbrowser.open(url) # Abre la URL en el navegador

def buscar_en_youtube(termino):
    #"""📺 Busca videos en YouTube"""
    query = urllib.parse.quote_plus(termino) # Codifica el texto para URL
    url = f"https://www.youtube.com/results?search_query={query}" # Construye la URL
    webbrowser.open(url) # Abre la URL en el navegador

def abrir_aplicacion(nombre):
    #"""💻 Abre una aplicación de Windows"""
    try:
        ruta_app = apps[nombre] # Busca la ruta en el diccionario que hicimos antes
        subprocess.Popen(ruta_app) # Abre la aplicación
        decir("feliz") #Dice frase feliz
    except Exception as e: # Si hay error, lo muestra
        say(f"No pude abrir {nombre}: {e}") # Muestra error

def abrir_juego(nombre):
    #"""🎮 Abre un juego de Steam"""
    global emocion_actual # Cambia emoción a emocionada
    emocion_actual = "emocionada" # Cambia emoción a emocionada
    try:
        uri = steam_games[nombre] # Busca la URI en el diccionario
        os.startfile(uri) # Abre el juego
        decir("emocionada") # Dice frase emocionada
    except Exception as e: # Si hay error, lo muestra
        say(f"No pude abrir {nombre}: {e}") # Muestra error

def abrir_sitio(nombre): 
    #"""🌐 Abre un sitio web"""
    try:
        url = sites[nombre] # Busca la URL en el diccionario
        webbrowser.open(url) # Abre el sitio web
        decir("feliz") # Dice frase feliz
    except Exception as e: # Si hay error, lo muestra
        say(f"No pude abrir {nombre}: {e}") # Muestra error

def reproducir_musica(nombre):
    #"""🎵 Reproduce música o videos en YouTube"""
    global emocion_actual # Cambia emoción a feliz
    emocion_actual = "feliz" # Cambia emoción a feliz
    buscar_en_youtube(nombre) # Usa la función de buscar en YouTube
    decir("feliz") # Dice frase feliz

# |--------------------------------------|
# |      Bucle principal de escucha      |
# |--------------------------------------|
recognizer = sr.Recognizer() # 🎧 Creamos un reconocedor de voz

say(f"Hola {nombre_usuario}, estoy lista (modo reposo)") # Saludo inicial

errores_consecutivos = 0 # Contador de errores

while True: # Bucle infinito
    with sr.Microphone() as source: # Usamos el micrófono como fuente
        estado_led("escuchando")  # LED minimalista
        try: # Ajusta para ruido ambiental y escucha
            recognizer.adjust_for_ambient_noise(source, duration=0.5) # Ajuste de ruido
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8) # Escucha con tiempo límite
        except sr.WaitTimeoutError: # Si no escucha nada en el tiempo, continúa
            time.sleep(0.2) # Pequeña pausa antes de
            continue # Reinicia el bucle

        try: # Intenta reconocer el audio
            comando = recognizer.recognize_google(audio, language='es-MX').lower() # Reconoce en español (México)

            if not modo_reposo: # Solo muestra comando si no está en reposo
                print(f"🧠 Comando reconocido: {comando}") #

            errores_consecutivos = 0 # Resetea contador de errores

            # |----------------------------------|
            # |            Wake Word             |
            # |----------------------------------|
            if modo_reposo:
                if 'oye cortana' in comando or 'ey cortana' in comando or 'escucha cortana' in comando: # Activa si escucha wake word
                    modo_reposo = False # Desactiva modo reposo
                    emocion_actual = "feliz" # Cambia emoción a feliz
                    despertar() # Llama a función de despertar
                continue # Reinicia bucle si estaba en reposo

            # |----------------------------------|
            # |        Comando de cierre         |
            # |----------------------------------| 
            if 'cerrar asistente' in comando or 'apagar asistente' in comando or 'adiós cortana' in comando or 'hasta luego cortana' in comando: 
                # Cierra el asistente
                decir("despedida") # Dice frase de despedida
                break # Sale del bucle principal

            accion_realizada = False # Bandera para acciones realizadas

            # |----------------------------------|
            # |        Abrir aplicaciones        |
            # |----------------------------------|
            #Esta parte abre las aplicaciones que definimos en el diccionario "apps" si no las encuentra, no hace nada
            for app_name in apps: # Recorre las aplicaciones
                if f"abre {app_name}" in comando or f"abrir {app_name}" in comando: # Si el comando coincide lo abre
                    abrir_aplicacion(app_name) # Abre la aplicación
                    accion_realizada = True # Marca que se realizó una acción
                    break # Sale del bucle
            if accion_realizada: #realizó una acción
                continue # Reinicia el bucle

            # |----------------------------------|
            # |          Abrir juegos            |
            # |----------------------------------|
            for juego_name in steam_games: # Recorre los juegos
                if f"abre {juego_name}" in comando or f"abrir {juego_name}" in comando: # Si el comando coincide lo abre
                    abrir_juego(juego_name) # Abre el juego
                    accion_realizada = True # Marca que se realizó una acción
                    break # Sale del bucle
            if accion_realizada: #realizó una acción
                continue # Reinicia el bucle

            # |----------------------------------|
            # |        Abrir sitios web          |
            # |----------------------------------|
            for site_name in sites: # Recorre los sitios web
                if f"abre {site_name}" in comando or f"abrir {site_name}" in comando: # Si el comando coincide lo abre
                    abrir_sitio(site_name) # Abre el sitio web
                    accion_realizada = True     # Marca que se realizó una acción
                    break # Sale del bucle
            if accion_realizada: #realizó una acción
                continue # Reinicia el bucle

            # |----------------------------------|
            # |       Búsqueda en Google         |
            # |----------------------------------|
            #Esta parte es para buscar en google, por ej: Buscar gatos/Busca gatos
            if 'buscar' in comando or 'busca' in comando: # Si el comando tiene la palabra buscar o busca
                termino = comando.replace('buscar', '').replace('busca', '').strip() # Quita la palabra buscar o busca
                if termino: # Si hay término para buscar
                    buscar_en_google(termino) # Llama a la función de buscar en Google
                continue # Reinicia el bucle

            # |----------------------------------|
            # |   Búsqueda de videos en YouTube  |
            # |----------------------------------|
            #Esta parte es para buscar videos en youtube, por ej: video de gatos/videos de gatos
            if 'video' in comando or 'videos' in comando: # Si el comando tiene la palabra video o videos
                termino = comando.replace('video', '').replace('videos', '').strip() # Quita la palabra video o videos
                if termino:  # Si hay término para buscar
                    buscar_en_youtube(termino) # Llama a la función de buscar en YouTube
                continue # Reinicia el bucle

            # |----------------------------------|
            # |    Reproducir música o videos    |
            #------------------------------------|
            #Esta parte es para reproducir musica o videos, por ej: reproduce Piter G/pon Piter G , soy muy fan de Piter G xD
            if 'reproduce' in comando or 'pon' in comando: # Si el comando tiene la palabra reproduce o pon
                musica = comando.replace('reproduce', '').replace('pon', '').strip() # Quita la palabra reproduce o pon
                if musica: # Si hay término para buscar
                    reproducir_musica(musica) # Llama a la función de reproducir música
                continue # Reinicia el bucle

            # |----------------------------------|
            # |          Comando de hora         |
            # |----------------------------------|
            #Esta parte es para decir la hora y fecha actual
            if any(f in comando for f in ['hora', 'qué hora es', 'dime la hora', 'me puedes decir la hora']): # Si el comando tiene alguna de estas frases
                ahora = datetime.now() # Obtiene la fecha y hora actual

                dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']   #Días de la semana en español
                meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                         'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']   #Meses del año en español

                dia_semana = dias[ahora.weekday()] # Obtiene el día de la semana
                mes = meses[ahora.month - 1] # Obtiene el mes

                hora_num = ahora.hour # Obtiene la hora numérica
                # Determina el período del día
                if 5 <= hora_num < 12: 
                    periodo = "de la mañana" 
                elif 12 <= hora_num < 20:
                    periodo = "de la tarde"
                else:
                    periodo = "de la noche"

                mensaje = f"Hoy es {dia_semana}, {ahora.day} de {mes} de {ahora.year}, y son las {ahora.hour:02d}:{ahora.minute:02d} {periodo}" # Construye el mensaje completo
                say(mensaje) # Dice la hora y fecha
                continue # Reinicia el bucle

            # |----------------------------------|
            # |           Modo reposo            |
            # |----------------------------------|
            #Esta parte es para poner a cortana en modo reposo o que descanse
            if 'modo reposo' in comando or 'descansa' in comando or 'duerme' in comando: # Si el comando tiene alguna de estas frases
                decir("reposo") # Dice frase de modo reposo
                modo_reposo = True # Activa modo reposo
                continue # Reinicia el bucle

            # |----------------------------------|
            # |         Saludos simples          |
            # |----------------------------------|
            #Y para finalizar, esta parte es para saludar a cortana ¿Que? ¿Poque lo hice? no lo sé XD
            if 'hola' in comando:
                decir("saludo")
                continue

        except sr.UnknownValueError: # Si no entiende el audio
            errores_consecutivos += 1 # Incrementa contador de errores
            if not modo_reposo: # Solo muestra error si no está en reposo
                if errores_consecutivos % 2 == 0 and audio.frame_data:  # Cada 2 errores y si hay datos de audio
                    decir("error") # Dice frase de error
                    time.sleep(0.3) # Pequeña pausa antes de continuar

        except sr.RequestError: # Si hay error con el servicio de reconocimiento
            if not modo_reposo: # Solo muestra error si no está en reposo
                print("🚫 Error de conexión con el servicio de reconocimiento de voz.")

        except Exception as e: # Cualquier otro error
            if not modo_reposo: # Solo muestra error si no está en reposo
                print(f"❗ Ocurrió un error: {e}") 

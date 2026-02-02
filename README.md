
Asistente Virtual en Python 🟢🔵

Un asistente de voz hecho en Python que puede abrir aplicaciones, sitios web, reproducir música, decir la hora y mucho más. Este proyecto está pensado para Windows y utiliza reconocimiento de voz y TTS (Text-to-Speech).

🛠 Características
Activación por wake word: “Oye Cortana” o “Escucha Cortana”.
Abrir aplicaciones de Windows (Bloc de notas, Calculadora, Steam, VLC, etc.).
Abrir juegos de Steam mediante su URI.
Abrir sitios web populares (Google, YouTube, Instagram, etc.).
Buscar en Google y YouTube con comandos de voz.
Reproducir música o videos en YouTube.
Decir la hora y fecha de manera amigable.
Modo reposo para descansar cuando no se use.
Personalidad y emociones con frases aleatorias para despertar, saludar o reaccionar.
Visualización de un LED virtual para indicar estado:

🟢 Escuchando

🔵 Hablando

📦 Requisitos
Windows 10 o superior
Python 3.8+


Librerías necesarias:

pip install SpeechRecognition
pip install pywin32
pip install dateparser


Nota: Se recomienda tener instalada la voz Sabina (Español México) para una experiencia más realista. Si no está disponible, se usará la voz predeterminada de Windows.

⚙️ Instalación

Clona o descarga este repositorio.
Instala los requerimientos usando pip.
Asegúrate de tener las rutas correctas para las aplicaciones y juegos en los diccionarios apps y steam_games.


Ajusta tu nombre y configuración inicial en la sección Configuración del usuario:

nombre_usuario = "Nick"  
modo_reposo = True
sonido_despertar = "C:\\Windows\\Media\\Windows Notify.wav"

🗣 Uso
Ejecuta el script cortana.py con Python:

python cortana.py

Cuando Cortana esté en modo reposo, activa diciendo:

Oye Cortana


🎨 Personalización

Frases y personalidad: Puedes modificar el diccionario personalidad para cambiar frases de saludo, despertar, reposo, emoción, etc.
Aplicaciones y juegos: Agrega o elimina elementos en los diccionarios apps y steam_games.
Sitios web: Personaliza los sitios web en el diccionario sites.
Sonido de despertar: Cambia la ruta del archivo .wav en sonido_despertar.

⚠️ Notas

Este proyecto está diseñado solo para Windows debido al uso de win32com y winsound.
Algunas funciones (como abrir juegos de Steam) requieren que la URI del juego esté correctamente configurada.
Se recomienda usar un micrófono de buena calidad para mejorar el reconocimiento de voz.

💡 Próximas mejoras

Añadir control de volumen y reproducción de música local.
Integrar respuestas más inteligentes con IA.
Interfaz gráfica opcional con LEDs y estado de Cortana
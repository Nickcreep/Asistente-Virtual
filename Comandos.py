# --------------------------------------
#       PANEL DE COMANDOS CORTANA
# --------------------------------------
# Para mostrar en consola de forma visual

def mostrar_comandos():
    print("\n\033[1;34m# |--------------------------------------|")
    print("# |           COMANDOS DE CORTANA        |")
    print("# |--------------------------------------|\033[0m\n")

    paneles = [
        ("Activación (Wake)", ["🟢 oye cortana", "🟢 ey cortana", "🟢 escucha cortana"], "Despierta a Cortana del modo reposo"),
        ("Despedida / Cierre", ["🔴 cerrar asistente", "🔴 apagar asistente", "🔴 adiós cortana", "🔴 hasta luego cortana"], "Apaga el asistente"),
        ("Abrir aplicaciones", ["💻 abre [nombre_app]", "💻 abrir [nombre_app]"], "Ej: abre calculadora, abrir bloc de notas, abre steam"),
        ("Abrir juegos", ["🎮 abre [nombre_juego]", "🎮 abrir [nombre_juego]"], "Ej: abre csgo, abrir dota 2, abre gta 5"),
        ("Abrir sitios web", ["🌐 abre [sitio]", "🌐 abrir [sitio]"], "Ej: abre google, abrir youtube, abre instagram"),
        ("Buscar en Google", ["🔍 buscar [término]", "🔍 busca [término]"], "Ej: buscar gatos divertidos"),
        ("Buscar videos en YouTube", ["📺 video [término]", "📺 videos [término]"], "Ej: video tutorial Python"),
        ("Reproducir música/videos", ["🎵 reproduce [término]", "🎵 pon [término]"], "Ej: reproduce Piter G"),
        ("Hora y fecha", ["⏰ qué hora es", "⏰ dime la hora", "⏰ me puedes decir la hora"], "Cortana dice hora y fecha actuales"),
        ("Modo reposo", ["😴 modo reposo", "😴 descansa", "😴 duerme"], "Cortana se pone en modo reposo"),
        ("Saludos", ["👋 hola"], "Cortana responde con un saludo")
    ]

    for titulo, comandos, descripcion in paneles:
        print(f"\033[1;33m# | {titulo:<30} |\033[0m")
        for c in comandos:
            print(f"#    {c}")
        print(f"#    ➤ {descripcion}")
        print("# |--------------------------------------|")
    print("\n")

# Llamamos a la función
mostrar_comandos()

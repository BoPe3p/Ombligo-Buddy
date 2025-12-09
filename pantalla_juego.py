import flet as ft
import datetime
import database

# --- CONFIGURACIÓN DEL JUEGO ---
# Definimos los tragos aquí porque pertenecen a la pantalla del juego
LISTA_TRAGOS = [
    {"nombre": "Chela", "puntos": 5, "icono": "🍺", "color": "orange"},
    {"nombre": "Shot", "puntos": 20, "icono": "🥃", "color": "red"},
    {"nombre": "Piscola", "puntos": 10, "icono": "🥤", "color": "brown"},
    {"nombre": "Kevin/Melvin", "puntos": 15, "icono": "🍷", "color": "purple"},
    {"nombre": "Tropical Gin", "puntos": 10, "icono": "🍹", "color": "yellow"},
    {"nombre": "Vodka", "puntos": 15, "icono": "🍾", "color": "grey"},
    {"nombre": "Energetica", "puntos": 1, "icono": "☕", "color": "red"},
    {"nombre": "Agua", "puntos": -1, "icono": "💧", "color": "blue"},
    {"nombre": "Waje", "puntos": -50, "icono": "🤮", "color": "green"},
]

def registrar_accion(e, page):
    # Lógica para guardar el trago
    datos = e.control.data
    trago_info = datos['trago']
    jugador_info = datos['jugador']
    
    # Feedback inmediato al usuario (para que no sienta que se pegó)
    page.open(
        ft.SnackBar(content=ft.Text(f"Enviando a la nube... ☁️"))
    )
    
    # --- 2. LLAMAMOS A GOOGLE SHEETS ---
    exito = database.guardar_accion(
        jugador_info['nombre'], 
        trago_info['nombre'], 
        trago_info['puntos']
    )

    if exito:
        mensaje = f"¡Anotado! {trago_info['nombre']} para {jugador_info['nombre']}"
        color = "green"
    else:
        mensaje = "Error de conexión: Se guardó solo localmente"
        color = "red"

    page.open(ft.SnackBar(content=ft.Text(mensaje), bgcolor=color))

def interfaz_juego(page, jugador, funcion_volver):
    page.clean() 

    # 1. Encabezado
    header = ft.Container(
        padding=20,
        bgcolor="white",
        border_radius=15,
        content=ft.Row([
            ft.Image(src=jugador['foto'], width=50, height=50, border_radius=25, fit=ft.ImageFit.COVER),
            ft.Column([
                ft.Text(jugador['nombre'], size=20, weight="bold"),
                ft.Text("¡A sumar puntos!", color="grey")
            ])
        ])
    )

    # 2. Botones de tragos
    botones_tragos = []
    for trago in LISTA_TRAGOS:
        paquete_datos = {"jugador": jugador, "trago": trago}
        
        btn = ft.Container(
            data=paquete_datos,
            on_click=lambda e: registrar_accion(e, page), 
            bgcolor="white",
            border_radius=15,
            padding=15,
            content=ft.Column([
                ft.Text(trago['icono'], size=40),
                ft.Text(trago['nombre'], weight="bold"),
                ft.Text(f"{trago['puntos']} pts", color=trago['color'], weight="bold")
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
        botones_tragos.append(btn)

    grid_tragos = ft.GridView(
        expand=True,
        runs_count=2,
        max_extent=160,
        child_aspect_ratio=1.0,
        spacing=10,
        run_spacing=10,
        controls=botones_tragos
    )

    # 3. Botón Salir
    btn_volver = ft.ElevatedButton("Cambiar Jugador", on_click=funcion_volver, color="red")

    page.add(header, ft.Divider(), grid_tragos, btn_volver)
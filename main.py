import flet as ft
import flet_audio as fa
import pantalla_juego
import random

def main(page: ft.Page):
    # Configuración básica de la ventana 
    page.title = "Ombligoat"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 360
    page.window_height = 800
    page.padding = 20

    # --- DATOS DE LOS K ---
    amigos = [
        {"id": 1, "nombre": "Rafalorcaa", "color": "blue", "foto": 'fotogato.jpg'},
        {"id": 2, "nombre": "Belto", "color": "blue", "foto": 'fotogato.jpg'},
        {"id": 3, "nombre": "Longa", "color": "blue", "foto": 'fotogato.jpg'},
        {"id": 4, "nombre": "Goonzalo", "color": "blue", "foto": 'fotogato.jpg'},
        {"id": 5, "nombre": "BP11", "color": "blue", "foto": 'fotogato.jpg'},
        {"id": 6, "nombre": "Benjita", "color": "blue", "foto": 'fotogato.jpg'},

    ]

    # --- NAVEGACIÓN ---
    
    def ir_al_inicio(e=None):
        # Esta función la pasaremos al otro archivo para poder volver
        page.clean()
        cargar_pantalla_seleccion()

    def ir_al_juego(jugador):
        # Llamamos a la función que creamos en el OTRO archivo
        pantalla_juego.interfaz_juego(page, jugador, ir_al_inicio)

    # --- MUSICA ---
    def music_button(e):

        if e.state == fa.AudioState.PAUSED:
            b.text = "Resume playing"
            b.on_click = lambda e: audio1.resume()

        elif e.state == fa.AudioState.PLAYING:
            b.text = "Pause playing"
            b.on_click = lambda e: audio1.pause()

        b.update()

    n = random.randint(1, 4)

    audio1 = fa.Audio(
        src= f"Musica maestro{n}.mp3",
        autoplay=True,
        on_state_changed=music_button,
    )
    b = ft.ElevatedButton("Pause playing", on_click=lambda _: audio1.pause())

    page.overlay.append(audio1)
    page.add(ft.Text("8===============================================D."), b)

    # --- PANTALLA SELECCIÓN ---
    
    def cargar_pantalla_seleccion():
        titulo = ft.Text("¿Quién eres hoy?", size=30, weight=ft.FontWeight.BOLD)
        
        items_grid = []
        for amigo in amigos:
            items_grid.append(
                ft.Container(
                    data=amigo,
                    on_click=lambda e: ir_al_juego(e.control.data),
                    bgcolor=amigo["color"], 
                    border_radius=20,
                    padding=10,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Image(src=amigo["foto"], width=70, height=70, border_radius=35, fit=ft.ImageFit.COVER),
                            ft.Text(amigo["nombre"], color="white", weight="bold", size=16)
                        ]
                    )
                )
            )

        grilla = ft.GridView(
            expand=1, runs_count=2, max_extent=150, child_aspect_ratio=1.0, spacing=10, run_spacing=10, controls=items_grid
        )
        page.add(titulo, ft.Divider(), grilla)

    # Arrancamos
    cargar_pantalla_seleccion()

ft.app(target=main, assets_dir="assets")
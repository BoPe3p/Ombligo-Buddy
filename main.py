import flet as ft
import flet_audio as fa
import pantalla_juego
import pantalla_ranking
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
        {"id": 2, "nombre": "Belto", "color": "blue", "foto": 'maxito.jpeg'},
        {"id": 3, "nombre": "Longa", "color": "blue", "foto": 'longa.jpeg'},
        {"id": 4, "nombre": "Goonzalo", "color": "blue", "foto": 'goonzalindo.jpeg'},
        {"id": 5, "nombre": "BP11", "color": "blue", "foto": 'BP11.jpeg'},
        {"id": 6, "nombre": "Benjita", "color": "blue", "foto": 'fotogato.jpg'},

    ]

    # --- MUSICA ---
    n = random.randint(1, 4)

    audio1 = fa.Audio(
        src= f"Musica maestro{n}.mp3",
        autoplay=True,
        volume=0.5,
        release_mode='loop'
    )

    page.overlay.append(audio1)
    page.update()

    # --- NAVEGACIÓN ---
    
    def ir_al_inicio(e=None):
        page.clean()
        cargar_pantalla_seleccion()

    def ir_al_juego(jugador):
        pantalla_juego.interfaz_juego(page, jugador, ir_al_inicio)

    def ir_al_ranking(jugador):
        pantalla_ranking.interfaz_ranking(page, ir_al_inicio)

    page.add(ft.Text("8===============================================D."))

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

        btn_ranking = ft.ElevatedButton(
            text="Ver Ranking",
            icon="emoji_events", 
            bgcolor="orange",    
            color="white",
            width=200,
            height=50,
            on_click=ir_al_ranking 
        )

        page.add(titulo, ft.Divider(), grilla, ft.Divider(), btn_ranking)

    # Arrancamos
    cargar_pantalla_seleccion()

ft.app(target=main, assets_dir="assets")
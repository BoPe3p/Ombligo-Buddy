import flet as ft
import database

def interfaz_ranking(page, funcion_volver):
    page.clean() 

    titulo = ft.Text("RANKING 🏆", size=30, weight=ft.FontWeight.BOLD)
    loader = ft.ProgressBar(width=200, color="amber", bgcolor="#eeeeee")
    txt_cargando = ft.Text("Consultando al VAR...", color="grey")
    columna_ranking = ft.ListView(expand=True, spacing=10)
    btn_volver = ft.ElevatedButton("Salir", on_click=funcion_volver, color="red")

    page.add(
        titulo, 
        ft.Divider(), 
        ft.Column([loader, txt_cargando], alignment=ft.MainAxisAlignment.CENTER), 
        columna_ranking, 
        ft.Divider(), 
        btn_volver
    )
    page.update()

    # 2. Ranking
    ranking = database.obtener_ranking()

    page.controls.pop(2)

    max_puntaje = ranking[0][1] if ranking else 1

    for i, jugador in enumerate(ranking):
        nombre = jugador[0]
        puntos = jugador[1]
        posicion = i + 1
        progreso = puntos / max_puntaje if max_puntaje > 0 else 0

        icono_lead = ft.Text(f"#{posicion}", size=15, weight="bold")
        color_icono = 'blue'
        
        if posicion == 1:
            icono_lead = ft.Icon(name="emoji_events", color="yellow")
            color_icono = "yellow"
        elif posicion == 2:
            icono_lead = ft.Icon(name='looks_two', color="grey")
            color_icono = "grey"
        elif posicion == 3:
            icono_lead = ft.Icon(name='looks_3', color="brown")
            color_icono = "brown"

        tarjeta = ft.Card(
            elevation=3,
            content=ft.Container(
                padding=10,
                content=ft.ListTile(
                    leading=icono_lead,
                    title=ft.Text(nombre, weight="bold"),
                    subtitle=ft.ProgressBar(value=progreso, color=color_icono, bgcolor="#eeeeee"),
                    trailing=ft.Text(f"{puntos} pts", size=16, weight="bold")
                )
            )
        )

        columna_ranking.controls.append(tarjeta)

    page.update()
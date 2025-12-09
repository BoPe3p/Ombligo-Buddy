import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

# --- CONFIGURACIÓN ---
NOMBRE_HOJA = "App Ombligo"  
ARCHIVO_CREDENCIALES = "credenciales.json" 

def conectar():
    """Conecta con Google y devuelve la hoja de cálculo"""
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(ARCHIVO_CREDENCIALES, scope)
        client = gspread.authorize(creds)
        
        # Abre la hoja de cálculo. Si no existe la pestaña, usa la primera (sheet1)
        sheet = client.open(NOMBRE_HOJA).sheet1 
        return sheet
    except Exception as e:
        print(f"Error al conectar con Google Sheets: {e}")
        return None

def guardar_accion(jugador, trago, puntos):
    """Guarda una nueva fila en el Excel online"""
    hoja = conectar()
    
    if hoja:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d")
        hora = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Fila a guardar: [Fecha, Hora, Jugador, Trago, Puntos]
        fila = [fecha, hora, jugador, trago, puntos]
        
        hoja.append_row(fila)
        print(f"✅ Guardado en la nube: {fila}")
        return True
    else:
        print("❌ No se pudo guardar (Modo Offline)")
        return False
    
def obtener_ranking():
    """Descarga los daots y obtiene el ranking de jugadores"""
    hoja = conectar()
    if not hoja:
        return []
    
    registro = hoja.get_all_records()
    puntajes = {}

    for fila in registro:
        nombre = fila['Jugador'] # <- Lo que sale en el sheet
        puntos = int(fila['Puntos'])

        if nombre in puntajes:
            puntajes[nombre] += puntos
        else:
            puntajes[nombre] = puntos
        
    ranking_ordenado = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
    return ranking_ordenado
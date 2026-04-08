"""
config_cloud.py
Configuración optimizada para GitHub y Streamlit Cloud.
"""
import os

# Obtenemos la ruta donde reside este archivo para crear rutas relativas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# El catálogo ahora está en la misma carpeta del proyecto
RUTA_EXCEL = os.path.join(BASE_DIR, "Catalogo_Final_Cloud.xlsx")

# Las portadas estarán en una carpeta dentro del repositorio de GitHub
# NOTA: Deberás copiar tu carpeta '03_Portadas' dentro de la carpeta del proyecto
RUTA_PORTADAS = os.path.join(BASE_DIR, "03_Portadas")

# Constantes visuales
COLUMNAS_POR_FILA = 5
DIMENSION_PORTADA = (300, 420)
COLOR_PLACEHOLDER = (240, 240, 240)
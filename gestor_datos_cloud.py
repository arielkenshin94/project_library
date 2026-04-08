"""
gestor_datos_cloud.py
Lectura de datos apuntando al ecosistema Cloud.
"""
import pandas as pd
import streamlit as st
from config_cloud import RUTA_EXCEL

@st.cache_data
def cargar_datos() -> pd.DataFrame:
    """Carga el catálogo purificado con los enlaces de Drive."""
    return pd.read_excel(RUTA_EXCEL)
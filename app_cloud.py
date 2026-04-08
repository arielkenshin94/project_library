"""
app_cloud.py
Orquestador de la versión Cloud.
Ejecutar con: streamlit run app_cloud.py
"""

import streamlit as st

st.set_page_config(page_title="Biblioteca Cloud", layout="wide")

from gestor_datos_cloud import cargar_datos
from interfaz_cloud import renderizar_cuadricula


def main() -> None:
    try:
        df_libros = cargar_datos()

        if not df_libros.empty:
            st.title("☁️ Biblioteca de Análisis de Datos (Cloud)")
            st.markdown("---")

            lista_cuadernos = ["Todos los libros"] + sorted(
                df_libros["Cuaderno_Principal"].dropna().unique().tolist()
            )
            cuaderno_elegido = st.selectbox(
                "📖 Selecciona tu Cuaderno de Estudio:", lista_cuadernos
            )

            if cuaderno_elegido != "Todos los libros":
                df_mostrar = df_libros[
                    df_libros["Cuaderno_Principal"] == cuaderno_elegido
                ]
            else:
                df_mostrar = df_libros

            renderizar_cuadricula(df_mostrar)

    except Exception as e:
        st.error(f"Hubo un error en la aplicación: {e}")


if __name__ == "__main__":
    main()

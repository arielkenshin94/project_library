"""
interfaz_cloud.py
Interfaz visual adaptada para la nube.
Usa st.link_button para redirigir a Google Drive.
"""

import os
import streamlit as st
import pandas as pd
from PIL import Image, ImageOps
from config_cloud import (
    RUTA_PORTADAS,
    COLUMNAS_POR_FILA,
    DIMENSION_PORTADA,
    COLOR_PLACEHOLDER,
)


@st.dialog("Detalles de la Obra")
def abrir_detalles(
    titulo: str,
    autor: str,
    anio: str,
    categoria: str,
    sinopsis: str,
    tags: str,
    ruta_img: str,
    enlace_drive: str,
) -> None:
    """Despliega el Pop-Up con la información y el botón web de Drive."""
    st.markdown(f"### {titulo}")
    st.caption(
        f"✍️ **Autor:** {autor} | 📅 **Año:** {anio} | 🏷️ **Categoría:** {categoria}"
    )
    st.markdown("---")

    col_img, col_info = st.columns([1, 1.8])

    with col_img:
        if os.path.exists(ruta_img):
            st.image(ruta_img, use_container_width=True)
        else:
            st.info("Sin portada")

    with col_info:
        st.markdown("**Sinopsis:**")
        st.write(sinopsis)
        st.markdown(f"**Etiquetas:** `{tags}`")
        st.markdown("---")
        st.markdown(
            "[🔗 Abrir NotebookLM](https://notebooklm.google.com/)",
            unsafe_allow_html=True,
        )

        st.write("")

        # --- LÓGICA CLOUD: Botón de redirección web ---
        if pd.notna(enlace_drive) and enlace_drive != "Sin Enlace":
            st.link_button(
                "☁️ Leer en Google Drive",
                url=enlace_drive,
                use_container_width=True,
                type="primary",
            )
        else:
            st.error("Enlace en la nube no disponible.")


def renderizar_cuadricula(df_mostrar: pd.DataFrame) -> None:
    """Renderiza la cuadrícula y extrae el enlace web del catálogo."""
    st.write(f"Mostrando **{len(df_mostrar)}** obras.")
    st.markdown("---")

    cols = st.columns(COLUMNAS_POR_FILA)

    for index, fila in df_mostrar.reset_index().iterrows():
        col = cols[index % COLUMNAS_POR_FILA]

        with col:
            with st.container(border=True):
                nombre_pdf = fila.get("Nombre_Fisico_Final")
                titulo = str(fila.get("Título", "Sin título"))
                autor = str(fila.get("Autor", "Desconocido"))

                # --- IMAGEN CON TAMAÑO ESTRICTO ---
                ruta_img = ""
                if pd.notna(nombre_pdf):
                    nombre_img = (
                        str(nombre_pdf).replace(".pdf", ".jpg").replace(".PDF", ".jpg")
                    )
                    ruta_img = os.path.join(RUTA_PORTADAS, nombre_img)

                    if os.path.exists(ruta_img):
                        img_original = Image.open(ruta_img)
                        img_uniforme = ImageOps.fit(
                            img_original,
                            DIMENSION_PORTADA,
                            method=Image.Resampling.LANCZOS,
                        )
                        st.image(img_uniforme, use_container_width=True)
                    else:
                        img_placeholder = Image.new(
                            "RGB", DIMENSION_PORTADA, color=COLOR_PLACEHOLDER
                        )
                        st.image(img_placeholder, use_container_width=True)

                # --- TEXTO CON ALTURA ESTRICTA ---
                titulo_corto = titulo[:45] + "..." if len(titulo) > 45 else titulo
                autor_corto = autor[:25] + "..." if len(autor) > 25 else autor

                html_texto = f"""
                    <div style="height: 85px; margin-top: 10px; overflow: hidden; display: flex; flex-direction: column;">
                        <span style="font-weight: 600; line-height: 1.2; font-size: 14px; margin-bottom: 5px;">{titulo_corto}</span>
                        <span style="color: #555; font-size: 12px;">✍️ {autor_corto}</span>
                    </div>
                """
                st.markdown(html_texto, unsafe_allow_html=True)

                # --- BOTÓN ALINEADO AL FINAL ---
                enlace_nube = str(fila.get("Enlace_Drive", ""))

                if st.button(
                    "🔍 Ver Detalles",
                    key=f"detalles_cloud_{index}",
                    use_container_width=True,
                ):
                    abrir_detalles(
                        titulo=titulo,
                        autor=autor,
                        anio=fila.get("Año", ""),
                        categoria=fila.get("Categoría", ""),
                        sinopsis=fila.get("Sinopsis", "Sin descripción."),
                        tags=fila.get("Tags", ""),
                        ruta_img=ruta_img,
                        enlace_drive=enlace_nube,
                    )

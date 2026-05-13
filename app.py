import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(page_title="Escrutinio San Fernando", layout="wide")

# --- INICIALIZACIÓN DE DATOS ---
if 'mesas_master' not in st.session_state:
    # Datos iniciales (San Fernando)
    data_inicial = [
        ["CASA DE LA CULTURA", 2, 1, "U"], ["CASA DE LA CULTURA", 3, 1, "A"], ["CASA DE LA CULTURA", 3, 1, "B"], ["CASA DE LA CULTURA", 3, 6, "U"],
        ["CASA DE LA JUVENTUD", 6, 10, "A"], ["CASA DE LA JUVENTUD", 6, 10, "B"], ["CASA DE LA JUVENTUD", 6, 22, "U"], ["CASA DE LA JUVENTUD", 6, 28, "A"], ["CASA DE LA JUVENTUD", 6, 28, "B"],
        ["CEIP ALMIRANTE LAULHÉ", 4, 1, "U"], ["CEIP ALMIRANTE LAULHÉ", 4, 5, "U"], ["CEIP ALMIRANTE LAULHÉ", 4, 6, "A"], ["CEIP ALMIRANTE LAULHÉ", 4, 6, "B"],
        ["CEIP ALMIRANTE LAULHÉ (CALLE)", 4, 2, "A"], ["CEIP ALMIRANTE LAULHÉ (CALLE)", 4, 2, "B"],
        ["CEIP ARDILA", 6, 9, "U"], ["CEIP ARDILA", 6, 19, "U"],
        ["CEIP ARQUITECTO LEOZ", 6, 12, "U"], ["CEIP ARQUITECTO LEOZ", 6, 13, "A"], ["CEIP ARQUITECTO LEOZ", 6, 13, "B"],
        ["CEIP CAMPOSOTO", 6, 24, "A"], ["CEIP CAMPOSOTO", 6, 24, "B"], ["CEIP CAMPOSOTO", 6, 31, "A"], ["CEIP CAMPOSOTO", 6, 31, "B"],
        ["CEIP CASERÍA DE OSSIO", 1, 5, "A"], ["CEIP CASERÍA DE OSSIO", 1, 5, "B"], ["CEIP CASERÍA DE OSSIO", 1, 14, "A"], ["CEIP CASERÍA DE OSSIO", 1, 14, "B"], ["CEIP CASERÍA DE OSSIO", 1, 15, "A"], ["CEIP CASERÍA DE OSSIO", 1, 15, "B"], ["CEIP CASERÍA DE OSSIO", 1, 17, "U"],
        ["CEIP CECILIO PUJAZÓN", 1, 1, "A"], ["CEIP CECILIO PUJAZÓN", 1, 1, "B"], ["CEIP CECILIO PUJAZÓN", 1, 4, "A"], ["CEIP CECILIO PUJAZÓN", 1, 4, "B"],
        ["CEIP CONSTITUCIÓN", 6, 8, "A"], ["CEIP CONSTITUCIÓN", 6, 8, "B"], ["CEIP CONSTITUCIÓN", 6, 17, "A"], ["CEIP CONSTITUCIÓN", 6, 17, "B"], ["CEIP CONSTITUCIÓN", 6, 17, "C"],
        ["CEIP ERYTHEIA", 6, 7, "A"], ["CEIP ERYTHEIA", 6, 7, "B"], ["CEIP ERYTHEIA", 6, 11, "A"], ["CEIP ERYTHEIA", 6, 11, "B"], ["CEIP ERYTHEIA", 6, 32, "U"],
        ["CEIP JUAN SEBASTIÁN ELCANO", 1, 8, "A"], ["CEIP JUAN SEBASTIÁN ELCANO", 1, 8, "B"], ["CEIP JUAN SEBASTIÁN ELCANO", 1, 11, "A"], ["CEIP JUAN SEBASTIÁN ELCANO", 1, 11, "B"],
        ["CEIP LAS CORTES", 6, 4, "U"], ["CEIP LAS CORTES", 6, 5, "A"], ["CEIP LAS CORTES", 6, 5, "B"],
        ["CEIP LOS ESTEROS", 1, 2, "U"], ["CEIP LOS ESTEROS", 1, 3, "U"],
        ["CEIP MANUEL DE FALLA", 6, 2, "A"], ["CEIP MANUEL DE FALLA", 6, 2, "B"], ["CEIP MANUEL DE FALLA", 6, 3, "U"], ["CEIP MANUEL DE FALLA", 6, 18, "U"],
        ["CEIP PADRE JOSÉ CASAL CARRILLO", 5, 1, "A"], ["CEIP PADRE JOSÉ CASAL CARRILLO", 5, 1, "B"], ["CEIP PADRE JOSÉ CASAL CARRILLO", 5, 2, "U"], ["CEIP PADRE JOSÉ CASAL CARRILLO", 5, 7, "A"], ["CEIP PADRE JOSÉ CASAL CARRILLO", 5, 7, "B"],
        ["CEIP QUINTANILLA", 1, 6, "U"], ["CEIP QUINTANILLA", 1, 10, "U"], ["CEIP QUINTANILLA", 1, 16, "U"],
        ["CEIP REINA DE LA PAZ", 6, 6, "U"], ["CEIP REINA DE LA PAZ", 6, 15, "A"], ["CEIP REINA DE LA PAZ", 6, 15, "B"], ["CEIP REINA DE LA PAZ", 6, 20, "A"], ["CEIP REINA DE LA PAZ", 6, 20, "B"],
        ["CEIP SAN IGNACIO", 1, 9, "A"], ["CEIP SAN IGNACIO", 1, 9, "B"], ["CEIP SAN IGNACIO", 3, 5, "A"], ["CEIP SAN IGNACIO", 3, 5, "B"],
        ["CEIP SERVANDO CAMÚÑEZ", 4, 4, "A"], ["CEIP SERVANDO CAMÚÑEZ", 4, 4, "B"],
        ["CENTRO DE CONGRESOS", 4, 3, "A"], ["CENTRO DE CONGRESOS", 4, 3, "B"], ["CENTRO DE CONGRESOS", 5, 3, "U"],
        ["CENTRO DOCENTE LA SALLE-REAL", 5, 4, "A"], ["CENTRO DOCENTE LA SALLE-REAL", 5, 4, "B"],
        ["CENTRO DOCENTE MIRAMAR", 5, 5, "A"], ["CENTRO DOCENTE MIRAMAR", 5, 5, "B"],
        ["CENTRO HERMANA CRISTINA", 6, 26, "A"], ["CENTRO HERMANA CRISTINA", 6, 26, "B"], ["CENTRO HERMANA CRISTINA", 6, 30, "A"], ["CENTRO HERMANA CRISTINA", 6, 30, "B"],
        ["COLEGIO COMPAÑÍA DE MARÍA (PABELLÓN)", 6, 1, "A"], ["COLEGIO COMPAÑÍA DE MARÍA (PABELLÓN)", 6, 1, "B"], ["COLEGIO COMPAÑÍA DE MARÍA (PABELLÓN)", 6, 21, "U"],
        ["IES BAHÍA", 6, 16, "A"], ["IES BAHÍA", 6, 16, "B"], ["IES BAHÍA", 6, 25, "A"], ["IES BAHÍA", 6, 25, "B"], ["IES BAHÍA", 6, 27, "A"], ["IES BAHÍA", 6, 27, "B"],
        ["IES ISLA DE LEÓN", 1, 7, "A"], ["IES ISLA DE LEÓN", 1, 7, "B"], ["IES ISLA DE LEÓN", 1, 12, "A"], ["IES ISLA DE LEÓN", 1, 12, "B"],
        ["IES LAS SALINAS", 6, 14, "A"], ["IES LAS SALINAS", 6, 14, "B"], ["IES LAS SALINAS", 6, 23, "U"], ["IES LAS SALINAS", 6, 29, "A"], ["IES LAS SALINAS", 6, 29, "B"],
        ["IES SANCTI PETRI", 3, 4, "U"], ["IES SANCTI PETRI", 3, 7, "A"], ["IES SANCTI PETRI", 3, 7, "B"], ["IES SANCTI PETRI", 3, 8, "U"],
        ["PABELLÓN CUBIERTO EL PARQUE", 5, 6, "A"], ["PABELLÓN CUBIERTO EL PARQUE", 5, 6, "B"],
        ["REAL, 63", 3, 2, "A"], ["REAL, 63", 3, 2, "B"]
    ]
    st.session_state.mesas_master = pd.DataFrame(data_inicial, columns=["Colegio", "Dist", "Secc", "Mesa"])
    st.session_state.votos = pd.DataFrame(columns=[
        "ID_Mesa", "Colegio", "Dist", "Secc", "Interventor", "Electores", "PP", "PSOE", "VOX", "Adelante", "Por_And", "Otros"
    ])

# Colores oficiales para los gráficos
COLOR_MAP = {
    "PP": "#1E4B8F", "PSOE": "#EF1C27", "VOX": "#63BE21",
    "Adelante": "#00C2E0", "Por_And": "#622D8B", "Otros": "#A0A0A0"
}

st.title("🗳️ Portal de Escrutinio San Fernando")

# Uso de tabs con keys para evitar el error de removeChild
tab_votos, tab_analisis, tab_config = st.tabs(["Registro de Datos", "Análisis por Zona", "Configuración"])

# --- PESTAÑA 1: REGISTRO ---
with tab_votos:
    st.header("Entrada de Datos")
    df_m = st.session_state.mesas_master
    opciones = df_m.apply(lambda x: f"{x['Dist']}-{x['Secc']}-{x['Mesa']} | {x['Colegio']}", axis=1).tolist()
    
    with st.form("form_registro", clear_on_submit=False):
        c_top1, c_top2 = st.columns(2)
        seleccion = c_top1.selectbox("Busca tu Mesa", opciones, key="sel_mesa")
        responsable = c_top2.text_input("Interventor / Apoderado", key="inp_resp")
        
        censo = st.number_input("Censo Total de la Mesa", min_value=0, step=1, key="num_censo")
        
        st.divider()
        st.subheader("Resultados del Escrutinio")
        v1, v2, v3 = st.columns(3)
        v_pp = v1.number_input("PP", min_value=0, step=1)
        v_psoe = v2.number_input("PSOE", min_value=0, step=1)
        v_vox = v3.number_input("VOX", min_value=0, step=1)
        v_ade = v1.number_input("Adelante Andalucía", min_value=0, step=1)
        v_por = v2.number_input("Por Andalucía", min_value=0, step=1)
        v_otr = v3.number_input("Otros", min_value=0, step=1)
        
        if st.form_submit_button("Guardar Mesa"):
            id_m = seleccion.split(" | ")[0]
            col_m = seleccion.split(" | ")[1]
            d_val = int(id_m.split("-")[0])
            s_val = int(id_m.split("-")[1])
            
            nueva_fila = {
                "ID_Mesa": id_m, "Colegio": col_m, "Dist": d_val, "Secc": s_val,
                "Interventor": responsable, "Electores": censo, "PP": v_pp, "PSOE": v_psoe,
                "VOX": v_vox, "Adelante": v_ade, "Por_And": v_por, "Otros": v_otr
            }
            # Actualizar datos
            st.session_state.votos = st.session_state.votos[st.session_state.votos.ID_Mesa != id_m]
            st.session_state.votos = pd.concat([st.session_state.votos, pd.DataFrame([nueva_fila])], ignore_index=True)
            st.success(f"✅ Mesa {id_m} registrada con éxito.")

# --- PESTAÑA 2: ANÁLISIS ---
with tab_analisis:
    if st.session_state.votos.empty:
        st.warning("No hay datos cargados. Registra alguna mesa para ver el análisis.")
    else:
        filtro = st.radio("Nivel de agrupación:", ["Global Municipio", "Por Distrito", "Por Sección"], horizontal=True, key="filtro_ana")
        df_v = st.session_state.votos
        cols_p = ["PP", "PSOE", "VOX", "Adelante", "Por_And", "Otros"]

        if filtro == "Global Municipio":
            totales = df_v[cols_p].sum().reset_index()
            totales.columns = ["Partido", "Votos"]
            fig_g = px.bar(totales, x="Partido", y="Votos", color="Partido", color_discrete_map=COLOR_MAP, title="Total San Fernando")
            st.plotly_chart(fig_g, use_container_width=True)
            st.dataframe(totales.set_index("Partido").T, use_container_width=True)

        elif filtro == "Por Distrito":
            df_dist = df_v.groupby("Dist")[cols_p].sum().reset_index()
            st.subheader("Resultados por Distritos")
            st.dataframe(df_dist, hide_index=True)
            fig_d = px.bar(df_dist, x="Dist", y=cols_p, barmode="group", color_discrete_map=COLOR_MAP, title="Comparativa por Distritos")
            st.plotly_chart(fig_d, use_container_width=True)

        elif filtro == "Por Sección":
            df_secc = df_v.groupby(["Dist", "Secc"])[cols_p].sum().reset_index()
            st.subheader("Detalle por Secciones Electorales")
            st.dataframe(df_secc, hide_index=True)

# --- PESTAÑA 3: CONFIGURACIÓN ---
with tab_config:
    st.header("Mantenimiento de Mesas")
    st.info("Desde aquí puedes añadir nuevas mesas o eliminar las existentes. Pulsa en 'Aplicar Cambios' para guardar.")
    
    # Clave fija para evitar errores de renderizado
    df_actualizado = st.data_editor(
        st.session_state.mesas_master, 
        num_rows="dynamic", 
        key="editor_maestro",
        use_container_width=True
    )
    
    if st.button("Aplicar Cambios al Maestro"):
        st.session_state.mesas_master = df_actualizado
        st.success("Configuración actualizada.")

    st.divider()
    st.subheader("Exportar Datos")
    csv_data = st.session_state.votos.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Descargar Resultados Actuales (CSV)", csv_data, "resultados_san_fernando.csv", "text/csv")

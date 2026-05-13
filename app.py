import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración inicial
st.set_page_config(page_title="Gestión Electoral San Fernando", layout="wide")

# --- PERSISTENCIA DE DATOS (Simulada para Web) ---
# En una versión web profesional, esto se conectaría a una base de datos.
# Para esta versión, usaremos session_state para que sea funcional al instante.

if 'mesas_master' not in st.session_state:
    # Carga inicial de todas tus mesas
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

# --- INTERFAZ ---
st.title("🏛️ Control Electoral Municipal")

tabs = st.tabs(["🗳️ Registro de Votos", "📊 Análisis y Gráficos", "⚙️ Configuración de Mesas"])

# --- TAB 1: REGISTRO DE VOTOS ---
with tabs[0]:
    st.header("Entrada de Datos por Mesa")
    
    # Crear ID único para el selector
    df_m = st.session_state.mesas_master
    opciones = df_m.apply(lambda x: f"{x['Dist']}-{x['Secc']}-{x['Mesa']} | {x['Colegio']}", axis=1).tolist()
    
    with st.form("form_votos"):
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            seleccion = st.selectbox("Selecciona la Mesa", opciones)
            interventor = st.text_input("Nombre de la persona en el colegio")
        with col_m2:
            censo = st.number_input("Número de electores totales", min_value=0)
        
        st.subheader("Escrutinio")
        c1, c2, c3 = st.columns(3)
        v_pp = c1.number_input("PP", min_value=0)
        v_psoe = c2.number_input("PSOE", min_value=0)
        v_vox = c3.number_input("VOX", min_value=0)
        v_adelante = c1.number_input("Adelante Andalucía", min_value=0)
        v_por_and = c2.number_input("Por Andalucía", min_value=0)
        v_otros = c3.number_input("Otros", min_value=0)
        
        if st.form_submit_button("Grabar Mesa"):
            id_m = seleccion.split(" | ")[0]
            colegio = seleccion.split(" | ")[1]
            dist_val = int(id_m.split("-")[0])
            secc_val = int(id_m.split("-")[1])
            
            nueva_data = {
                "ID_Mesa": id_m, "Colegio": colegio, "Dist": dist_val, "Secc": secc_val,
                "Interventor": interventor, "Electores": censo, "PP": v_pp, "PSOE": v_psoe,
                "VOX": v_vox, "Adelante": v_adelante, "Por_And": v_por_and, "Otros": v_otros
            }
            # Eliminar si ya existía la mesa para actualizarla
            st.session_state.votos = st.session_state.votos[st.session_state.votos.ID_Mesa != id_m]
            st.session_state.votos = pd.concat([st.session_state.votos, pd.DataFrame([nueva_data])], ignore_index=True)
            st.success(f"Datos guardados para la mesa {id_m}")

# --- TAB 2: ANÁLISIS ---
with tabs[1]:
    if st.session_state.votos.empty:
        st.info("No hay datos grabados todavía.")
    else:
        st.header("Resultados Agrupados")
        
        modo = st.radio("Agrupar por:", ["Municipio (Global)", "Distrito", "Sección"], horizontal=True)
        
        df_v = st.session_state.votos
        cols_votos = ["PP", "PSOE", "VOX", "Adelante", "Por_And", "Otros"]
        
        if modo == "Municipio (Global)":
            res = df_v[cols_votos].sum().reset_index()
            res.columns = ["Partido", "Votos"]
            fig = px.bar(res, x="Partido", y="Votos", color="Partido", title="Resultado Global")
            st.plotly_chart(fig, use_container_width=True)
            st.table(res)
            
        elif modo == "Distrito":
            res_dist = df_v.groupby("Dist")[cols_votos].sum()
            st.dataframe(res_dist)
            fig_dist = px.bar(res_dist.reset_index(), x="Dist", y=cols_votos, title="Votos por Distrito")
            st.plotly_chart(fig_dist, use_container_width=True)
            
        elif modo == "Sección":
            res_secc = df_v.groupby(["Dist", "Secc"])[cols_votos].sum()
            st.dataframe(res_secc)

# --- TAB 3: CONFIGURACIÓN ---
with tabs[2]:
    st.header("Gestión del Maestro de Mesas")
    
    # Editor de datos (Permite borrar, añadir y editar filas directamente)
    df_editado = st.data_editor(st.session_state.mesas_master, num_rows="dynamic", use_container_width=True)
    
    if st.button("Guardar cambios en el Maestro"):
        st.session_state.mesas_master = df_editado
        st.success("Listado de mesas actualizado correctamente.")
        
    st.divider()
    # Opción de descargar los datos para no perderlos
    csv = st.session_state.votos.to_csv(index=False).encode('utf-8')
    st.download_button("Descargar Backup de Votos (CSV)", csv, "votos_san_fernando.csv", "text/csv")
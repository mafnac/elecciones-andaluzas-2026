import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(page_title="Escrutinio San Fernando", layout="wide")

# --- CLAVE DE ACCESO (Cámbiala aquí) ---
PASSWORD_SISTEMA = "SF2026"  # Puedes poner la que prefieras

# --- INICIALIZACIÓN DE DATOS ---
if 'mesas_master' not in st.session_state:
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
        ["CEIP REINA DE LA PAZ", 6, 6, "U"], ["CEIP REINA DE LA PAZ", 6, 15, "A"], ["CEIP REINA DE la PAZ", 6, 15, "B"], ["CEIP REINA DE LA PAZ", 6, 20, "A"], ["CEIP REINA DE LA PAZ", 6, 20, "B"],
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

# Colores oficiales
COLOR_MAP = {
    "PP": "#1E4B8F", "PSOE": "#EF1C27", "VOX": "#63BE21",
    "Adelante": "#00C2E0", "Por_And": "#622D8B", "Otros": "#A0A0A0"
}

st.title("🗳️ Portal de Escrutinio San Fernando")

tab_votos, tab_analisis, tab_config = st.tabs(["Registro de Datos", "Análisis por Zona", "🔒 Configuración"])

# --- PESTAÑA 1: REGISTRO (Mantiene autocompletado) ---
with tab_votos:
    st.header("Entrada de Datos")
    
    df_m = st.session_state.mesas_master
    opciones = df_m.apply(lambda x: f"{x['Dist']}-{x['Secc']}-{x['Mesa']} | {x['Colegio']}", axis=1).tolist()
    seleccion = st.selectbox("Selecciona la Mesa", opciones, key="main_selector")
    
    id_actual = seleccion.split(" | ")[0]
    col_actual = seleccion.split(" | ")[1]
    
    datos_existentes = st.session_state.votos[st.session_state.votos.ID_Mesa == id_actual]
    
    if not datos_existentes.empty:
        fila = datos_existentes.iloc[0]
        v_interventor, v_censo = fila["Interventor"], int(fila["Electores"])
        v_pp, v_psoe, v_vox = int(fila["PP"]), int(fila["PSOE"]), int(fila["VOX"])
        v_ade, v_por, v_otr = int(fila["Adelante"]), int(fila["Por_And"]), int(fila["Otros"])
        st.info(f"📍 Datos actuales de la mesa {id_actual}")
    else:
        v_interventor, v_censo = "", 0
        v_pp = v_psoe = v_vox = v_ade = v_por = v_otr = 0
        st.write("✨ Mesa sin datos.")

    with st.form("form_registro"):
        c_top1, c_top2 = st.columns(2)
        resp = c_top1.text_input("Interventor / Apoderado", value=v_interventor)
        censo_in = c_top2.number_input("Censo Total", min_value=0, value=v_censo)
        
        c1, c2, c3 = st.columns(3)
        pp_in = c1.number_input("PP", min_value=0, value=v_pp)
        psoe_in = c2.number_input("PSOE", min_value=0, value=v_psoe)
        vox_in = c3.number_input("VOX", min_value=0, value=v_vox)
        ade_in = c1.number_input("Adelante", min_value=0, value=v_ade)
        por_in = c2.number_input("Por Andalucía", min_value=0, value=v_por)
        otr_in = c3.number_input("Otros", min_value=0, value=v_otr)
        
        if st.form_submit_button("Guardar Datos"):
            d_val, s_val = int(id_actual.split("-")[0]), int(id_actual.split("-")[1])
            nueva_fila = {
                "ID_Mesa": id_actual, "Colegio": col_actual, "Dist": d_val, "Secc": s_val,
                "Interventor": resp, "Electores": censo_in, "PP": pp_in, "PSOE": psoe_in,
                "VOX": vox_in, "Adelante": ade_in, "Por_And": por_in, "Otros": otr_in
            }
            st.session_state.votos = st.session_state.votos[st.session_state.votos.ID_Mesa != id_actual]
            st.session_state.votos = pd.concat([st.session_state.votos, pd.DataFrame([nueva_fila])], ignore_index=True)
            st.success("✅ ¡Guardado!")
            st.rerun()

# --- PESTAÑA 2: ANÁLISIS ---
with tab_analisis:
    if st.session_state.votos.empty:
        st.warning("No hay votos registrados.")
    else:
        # Gráfico resumen
        df_v = st.session_state.votos
        cols_p = ["PP", "PSOE", "VOX", "Adelante", "Por_And", "Otros"]
        totales = df_v[cols_p].sum().reset_index()
        totales.columns = ["Partido", "Votos"]
        fig = px.bar(totales, x="Partido", y="Votos", color="Partido", color_discrete_map=COLOR_MAP)
        st.plotly_chart(fig, use_container_width=True)

# --- PESTAÑA 3: CONFIGURACIÓN CON SEGURIDAD ---
with tab_config:
    st.header("Zona de Administración")
    
    # Verificación de identidad
    password_input = st.text_input("Introduce la clave de administrador para editar:", type="password")
    
    if password_input == PASSWORD_SISTEMA:
        st.success("Acceso concedido.")
        st.subheader("Maestro de Mesas")
        df_edit = st.data_editor(st.session_state.mesas_master, num_rows="dynamic")
        
        if st.button("Confirmar cambios en el Maestro"):
            st.session_state.mesas_master = df_edit
            st.success("Base de mesas actualizada.")
            
        st.divider()
        if st.button("⚠️ BORRAR TODOS LOS VOTOS (Reiniciar Jornada)"):
            st.session_state.votos = pd.DataFrame(columns=st.session_state.votos.columns)
            st.warning("Se han borrado todos los registros de votos.")
            st.rerun()
    elif password_input != "":
        st.error("❌ Clave incorrecta. Contacta con el administrador.")
    else:
        st.info("🔒 Por favor, introduce la clave para realizar cambios estructurales.")

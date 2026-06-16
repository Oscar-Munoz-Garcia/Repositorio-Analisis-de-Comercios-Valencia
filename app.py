import streamlit as st
import pandas as pd
import plotly.express as px
# import folium (para mapas interactivos)

# 1. CONFIGURACIÓN DE PÁGINA (Estética Professional)
st.set_page_config(
    page_title="Valencia Retail Intelligence",
    page_icon="📍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ESTILO CSS CUSTOM (Para que no parezca una app estándar)
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { font-size: 20px; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("📍 Valencia Commerce Insights")
st.markdown("Plataforma de Toma de Decisiones Estratégicas para el Ayuntamiento e Inversores")

# --- TABS PRINCIPALES ---
tab_ayto, tab_inv = st.tabs(["🏛️ Gestión Municipal", "💼 Análisis de Inversión"])

# ==========================================
# SECCIÓN 1: AYUNTAMIENTO
# ==========================================
with tab_ayto:
    st.header("Análisis General de Barrios")
    
    # FILTRO GLOBAL: Selección de tipo de comercio
    tipo_comercio = st.multiselect(
        "Filtrar por categoría de comercio:", 
        ["Alimentación", "Hostelería", "Moda", "Servicios", "Tecnología"],
        default=["Alimentación", "Hostelería"]
    )
    
    # 1.1 KPIS GENERALES
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        # LÓGICA: Calcular total de comercios activos en Valencia filtrados por tipo
        st.metric("Total Comercios", "14,235", "+2.5%")
    with col2:
        # LÓGICA: % de ocupación de locales comerciales
        st.metric("Ocupación Media", "88%", "Estable")
    with col3:
        # LÓGICA: Gasto medio por habitante en la zona
        st.metric("Gasto Promedio", "1.2k €/mes", "+5%")
    with col4:
        # LÓGICA: Identificar el barrio con mayor densidad comercial actual
        st.metric("Barrio Top", "Ruzafa")

    # 1.2 GRÁFICOS Y ESTADÍSTICAS
    c_izq, c_der = st.columns([1, 1])
    with c_izq:
        st.subheader("Distribución de Comercios por Distrito")
        # LÓGICA: Gráfico de barras (Plotly) comparando distritos
        st.info("Aquí insertaremos un gráfico comparativo de volumen por distrito.")
        
    with c_der:
        st.subheader("Evolución de Aperturas (Último Año)")
        # LÓGICA: Gráfico de líneas con tendencia temporal
        st.info("Gráfico de serie temporal de nuevas licencias.")

    # 1.3 MAPA CHOROPLETH MUNICIPAL
    st.subheader("Mapa de Saturación Comercial por Barrio")
    # LÓGICA: Cargar GeoJSON de barrios de Valencia y cruzar con vuestros datos
    # Visualizar mediante color la densidad o el KPI seleccionado.
    st.markdown("---")
    st.warning("Visualización de Mapa Choropleth (Integrar Folium/Pydeck aquí)")
    st.markdown("---")

    # 1.4 ANÁLISIS ESPECÍFICO DE UN BARRIO (Selector al final)
    st.header("🔍 Zoom: Análisis de Barrio Concreto")
    barrio_sel = st.selectbox("Selecciona un barrio para ver detalle:", ["Ruzafa", "El Carmen", "Malilla", "Benimaclet"])
    
    col_b1, col_b2 = st.columns([1, 2])
    with col_b1:
        # LÓGICA: KPIs micro del barrio seleccionado (Población, edad media, renta)
        st.write(f"**KPIs de {barrio_sel}:**")
        st.json({"Renta Media": "35k", "Población": "25,000", "Competencia": "Alta"})
    with col_b2:
        # LÓGICA: Recomendación municipal para ese barrio (ej: incentivar farmacias)
        st.success(f"Propuesta de Política: Incentivar apertura de 'Servicios de Proximidad' en {barrio_sel}.")

# ==========================================
# SECCIÓN 2: INVERSOR
# ==========================================
with tab_inv:
    st.header("Radar de Oportunidades de Inversión")
    
    # 2.1 RECOMENDACIÓN TOP 5 GENERAL
    st.subheader("✨ Las 5 Mejores Oportunidades en Valencia")
    # LÓGICA: Algoritmo que cruza Demanda Insatisfecha + Renta + Alquiler Local
    recs = pd.DataFrame({
        "Barrio": ["Malilla", "Cabanyal", "Patraix", "Nou Moles", "Ruzafa"],
        "Negocio Sugerido": ["Gimnasio", "Coworking", "Cafetería", "Supermercado", "Lavandería"],
        "Puntuación Éxito": [98, 95, 92, 89, 85]
    })
    st.table(recs) # Diseño limpio de tabla para inversión

    # 2.2 BÚSQUEDA POR TIPO DE COMERCIO
    st.markdown("---")
    comercio_inv = st.selectbox("¿Qué tipo de negocio quieres abrir?", ["Librería", "Restaurante Vegano", "Tienda de Mascotas"])
    
    col_inv1, col_inv2 = st.columns([1, 2])
    with col_inv1:
        st.markdown(f"#### Mejores barrios para {comercio_inv}")
        # LÓGICA: Filtrar vuestro algoritmo para mostrar barrios con "Demanda > Oferta" para ese tipo.
        st.write("1. **Quatre Carreres** (Baja competencia)")
        st.write("2. **La Saïdia** (Alta demanda joven)")
    with col_inv2:
        # LÓGICA: Choropleth de oportunidad específica (Mapa de calor de demanda)
        st.info("Mapa interactivo de Oportunidad por Negocio.")

    # 2.3 MAPA EXPLORATORIO (HOVER)
    st.header("🗺️ Explorador Inteligente")
    st.write("Desplaza el cursor por el mapa para descubrir el comercio 'más rentable' en cada zona.")
    # LÓGICA: Implementar un mapa interactivo (Folium o Plotly Mapbox) donde el hover 
    # muestre el nombre del barrio y el comercio con mayor "gap" de demanda.
    st.markdown("---")
    st.info("Mapa de Valencia: Al pasar el cursor verás: 'Barrio X' -> 'Mejor opción: Peluquería'")
    st.markdown("---")
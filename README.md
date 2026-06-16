# GeoMarket-VLC · App Streamlit

Plataforma interactiva de inteligencia comercial urbana para Valencia.

## Estructura de archivos esperada

```
app/
├── app.py                          ← este archivo
├── requirements.txt
├── geomarket_vlc_features.csv      ← del notebook de pipeline
├── geomarket_vlc_barrios.geojson   ← del notebook de pipeline
└── models/                         ← del notebook de modelado
    ├── modelo_rf.pkl
    ├── modelo_xgb.pkl
    ├── modelo_stacking.pkl
    ├── shap_explainer.pkl
    └── feature_names.pkl
```

## Ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

La app se abrirá en `http://localhost:8501`.

## Despliegue en Streamlit Cloud

1. Subir esta carpeta a un repositorio de GitHub
2. Conectarlo en https://share.streamlit.io
3. Apuntar a `app.py`

## Pestañas

1. **Diagnóstico Territorial** — Visión global con KPIs y mapa multicapa
2. **Recomendador de Emprendimiento** — Score 0-100 por barrio y sector
3. **Panel del Planificador** — Predicción ML, SHAP y simulador de escenarios

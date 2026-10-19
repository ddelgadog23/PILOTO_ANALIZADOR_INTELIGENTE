import streamlit as st
import pandas as pd

st.title("🚀 Mi Primer Dashboard - MVP")
st.write("¡El servidor está funcionando y listo para analizar el inventario!")

try:
    # 1. Cargar los datos desde el archivo CSV
    ds = pd.read_csv('datos/GroceryDataset.csv') 
    
    # 2. Mostrar una vista previa de los datos
    st.subheader("Vista previa de los datos")
    st.dataframe(ds.head())

    # 3. Agrupar y graficar
    if 'Sub Category' in ds.columns and 'Price' in ds.columns:
        
        # --- LIMPIEZA DE DATOS AVANZADA ---
        # Extrae solo el primer número válido encontrado en la celda (ignorando palabras como "through")
        ds['Price'] = ds['Price'].astype(str).str.extract(r'(\d+\.?\d*)')[0].astype(float)
        
        # Agrupamos
        precio_promedio = ds.groupby('Sub Category')['Price'].mean()
        
        # Graficamos
        st.subheader("Precio Promedio por Categoría")
        st.bar_chart(precio_promedio)
        
    else:
        st.warning("Las columnas 'Sub Category' o 'Price' no se encuentran en el dataset.")

except FileNotFoundError:
    st.error("No se encontró el archivo GroceryDataset.csv. Verifica la ruta.")
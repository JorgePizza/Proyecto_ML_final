importar streamlit como st
importar pandas como pd
importar plotly.express como px

st.set_page_config(page_title="Perfiles Clínicos", layout="wide")
st.title("🧠 Análisis de Perfiles Clínicos en Hospitalización Psiquiátrica")

Descargar CSV (desde el mismo repositorio)
@st.cache_data
def cargar_datos():
devolver pd.read_csv("resultados_clustering.csv")

df = cargar_datos()

Filtros por clúster
cluster = st.selectbox("Selecciona un cluster:", sorted(df['Cluster'].unique()))
df_filtrado = df[df['Cluster'] == clúster]

Mostrar resumen
st.subheader("Pacientes del Cluster Seleccionado")
st.write(f"Total de pacientes: {len(df_filtrado)}")
st.dataframe(df_filtrado)

Estadísticas
st.subheader("Promedio de Edad y Días de Internamiento")
st.write(df_filtrado[['Edad', 'Días_internamiento']].describe())

Visualización
fig = px.scatter(df, x="Edad", y="Días_internamiento", color=df["Cluster"].astype(str),
title="Distribución de pacientes por cluster",
etiquetas={"color": "Cluster"})
st.plotly_chart(fig, use_container_width=True)

import pandas as pd
import streamlit as st

def classifica_porte(total):
    if total <= 200:
        return "Pequena"
    elif total <= 400:
        return "Média"
    else:
        return "Grande"

censo = pd.read_csv("escolas_sp_regioes_2024_geo.csv")

st.title("Painel de Escolas de Regiões de SP - painel elaborado por Arthur Condão")
st.caption("Adaptado do Censo Escolar 2024 (INEP) - painel elaborado por Arthur Condão")

regiao = st.selectbox(
    "Escolha a Região",
    ["Todas", "Região Metropolitana de SP",
     "Baixada Santista", "Litoral Norte", "Vale do Ribeira"]
)

if regiao != "Todas":
    censo = censo[censo["regiao"] == regiao]

opcoes_loc = ["Todas", "Todas as diferenciadas"] + sorted(censo["loc_diferenciada"].unique())
loc = st.selectbox("Localização diferenciada", opcoes_loc)

if loc == "Todas as diferenciadas":
    censo = censo[censo["loc_diferenciada"] != "Não"]
elif loc != "Todas":
    censo = censo[censo["loc_diferenciada"] == loc]
    
col1, col2 = st.columns(2)

col1.metric("Qtde de Escolas", len(censo))
col2.metric("Total de Matrículas", censo["matriculas"].sum())

censo["porte"] = censo["matriculas"].apply(classifica_porte)

st.subheader("Escolas por Dependência e Porte")
grafico = pd.crosstab(censo["dependencia"], censo["porte"])
grafico = grafico.reindex(columns=["Pequena", "Média", "Grande"], fill_value=0)
st.bar_chart(grafico)

st.subheader("Escolas por Porte")
st.bar_chart(censo["porte"].value_counts())

st.subheader("Escolas por Abastecimento de Agua")
st.bar_chart(censo["agua"].value_counts())

st.subheader("Mapa das escolas")
st.map(censo[["latitude", "longitude"]])

st.subheader("Lista das escolas")
st.dataframe(censo[["municipio", "escola", "matriculas", "porte"]])
censo["servicos"] = (
    (censo["agua"] == "Rede pública").astype(int)
    + (censo["energia"] == "Rede pública").astype(int)
    + (censo["esgoto"] == "Rede pública").astype(int)
    + (censo["lixo"] == "Coleta").astype(int)
)

st.subheader("Escolas por número de serviços públicos básicos")
st.caption("Conta quantos destes a escola recebe: água da rede pública, energia da rede pública, esgoto da rede pública e coleta de lixo (de 0 a 4).")
st.bar_chart(censo["servicos"].value_counts().sort_index())

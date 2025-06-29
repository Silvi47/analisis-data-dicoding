import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Analisis Data E‑Commerce 2016‑2018",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Analisis Data E-Commerce Tahun 2016, 2017, dan 2018")

# Render a bar
def bar_chart(df, x, y, color=None, title=None, palette=None, show_values=False):
    fig = px.bar(
        df,
        x=x,
        y=y,
        color=color,
        text=y if show_values else None,
        title=title,
        color_discrete_sequence=palette,
    )

    fig.update_traces(
        hovertemplate="%{x}<br>%{y}",
        textposition="outside",
    )
    fig.update_layout(
        xaxis_title=None,
        yaxis_title=None,
        margin=dict(t=60, r=20, l=20, b=40),
    )
    st.plotly_chart(fig, use_container_width=True)

trend_df = pd.DataFrame(
    {
        "Kuartal": ["1", "2", "3", "4"],
        "Jumlah Pesanan": [2446, 2349, 1633, 2072],
        "Kategori": [
            "computers_accessories",
            "health_beauty",
            "health_beauty",
            "bed_bath_table",
        ],
    }
)

recency_df = pd.DataFrame(
    {
        "Tahun": ["2016", "2017", "2018"],
        "Rata‑rata Recency (Hari)": [695.608974, 383.173871, 127.502706],
    }
)
monetary_df = pd.DataFrame(
    {
        "Tahun": ["2016", "2017", "2018"],
        "Rata‑rata Monetary (Rp)": [159.570256, 138.087597, 137.351014],
    }
)

st.subheader("Kategori Produk Paling Tren per Kuartal (2017 & 2018)")
bar_chart(
    trend_df,
    x="Kuartal",
    y="Jumlah Pesanan",
    color="Kategori",
    palette=px.colors.qualitative.Set2
)

st.markdown("---")

st.header("Rata‑rata Recency dan Monetary Customer per Tahun")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Rata‑rata Recency Customer per Tahun")
    bar_chart(
        recency_df,
        x="Tahun",
        y="Rata‑rata Recency (Hari)",
        palette=px.colors.qualitative.Set2,
    )
with col2:
    st.subheader("Rata‑rata Monetary Customer per Tahun")
    bar_chart(
        monetary_df,
        x="Tahun",
        y="Rata‑rata Monetary (Rp)",
        palette=px.colors.sequential.Rainbow,
    )
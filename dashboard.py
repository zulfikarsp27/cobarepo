import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ---------------------------------------------------------
# 1. SETUP DASAR STREAMLIT
# ---------------------------------------------------------
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Bike Sharing Interactive Dashboard")
st.markdown("Dibuat dengan Streamlit untuk analisis data Bike Sharing.")

# ---------------------------------------------------------
# 2. LOAD & PREPARASI DATA
# ---------------------------------------------------------
@st.cache_data
def load_data():
    # Ganti 'hour.csv' dengan path dataset Anda
    df = pd.read_csv("hour.csv")
    # Kolom bawaan: 
    # ['instant', 'dteday', 'season', 'yr', 'mnth', 'hr', 'holiday',
    #  'weekday', 'workingday', 'weathersit', 'temp', 'atemp',
    #  'hum', 'windspeed', 'casual', 'registered', 'cnt']
    
    # Buat kolom 'hour' agar lebih jelas
    df['hour'] = df['hr']
    
    # Optional: Convert 'weekday' ke nama hari
    weekday_map = {0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 
                   4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'}
    df['weekday_name'] = df['weekday'].map(weekday_map)
    
    # Buat kolom 'day_type' (Hari Kerja vs Hari Libur)
    df['day_type'] = df['workingday'].apply(lambda x: "Hari Kerja" if x == 1 else "Hari Libur")
    
    return df

df = load_data()

# ---------------------------------------------------------
# 3. SIDEBAR FILTERS
# ---------------------------------------------------------
st.sidebar.header("Opsi Filter")

day_type = st.sidebar.selectbox(
    "Pilih Tipe Hari:",
    options=["Semua", "Hari Kerja", "Hari Libur"],
    index=0
)

# Filter jam
min_hour, max_hour = st.sidebar.slider(
    "Rentang Jam (0 - 23):",
    min_value=0, max_value=23,
    value=(0, 23), step=1
)

# Terapkan Filter
filtered_df = df.copy()
if day_type == "Hari Kerja":
    filtered_df = filtered_df[filtered_df["workingday"] == 1]
elif day_type == "Hari Libur":
    filtered_df = filtered_df[filtered_df["workingday"] == 0]

filtered_df = filtered_df[(filtered_df["hour"] >= min_hour) & (filtered_df["hour"] <= max_hour)]

# ---------------------------------------------------------
# 4. EDA (EXPLORATORY DATA ANALYSIS)
# ---------------------------------------------------------
st.markdown("## Exploratory Data Analysis (EDA)")

# 4.1 Informasi Dasar
st.markdown("### 4.1. Info Dasar Data")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Jumlah Baris (Row)", len(df))
with col2:
    st.metric("Jumlah Kolom (Column)", len(df.columns))
with col3:
    st.metric("Periode Data", f"{df['dteday'].min()} - {df['dteday'].max()}")

st.write("Data preview (setelah filter):")
st.dataframe(filtered_df.head(5))

# 4.2 Distribusi Musiman / Bulanan
st.markdown("### 4.2. Distribusi Penggunaan Sepeda per Bulan")
monthly_usage = filtered_df.groupby("mnth")["cnt"].mean().reset_index()
fig_monthly = px.bar(
    monthly_usage, x="mnth", y="cnt", 
    title="Rata-rata Penggunaan Sepeda per Bulan (Setelah Filter)",
    labels={"mnth":"Bulan", "cnt":"Rata-rata Jumlah Penyewa"}
)
st.plotly_chart(fig_monthly, use_container_width=True)

# 4.3 Korelasi Antar-Variabel
st.markdown("### 4.3. Korelasi Antar Variabel Utama")
corr_cols = ["temp", "hum", "windspeed", "cnt"]
corr_data = filtered_df[corr_cols].corr()
fig_corr = go.Figure(data=go.Heatmap(
    z=corr_data.values,
    x=corr_data.columns,
    y=corr_data.columns,
    colorscale='RdBu',
    zmin=-1, zmax=1
))
fig_corr.update_layout(title="Heatmap Korelasi", xaxis_nticks=36)
st.plotly_chart(fig_corr, use_container_width=True)

st.markdown("""
**Insight EDA:**  
- **Distribusi Bulanan**: Ada variasi musiman, di mana bulan-bulan tertentu (biasanya cuaca lebih nyaman) cenderung memiliki penggunaan lebih tinggi.  
- **Korelasi**: 'temp' dan 'cnt' memiliki korelasi positif (ketika suhu lebih nyaman, penggunaan meningkat), sedangkan 'windspeed' cenderung berkorelasi negatif dengan 'cnt'.
""")

# ---------------------------------------------------------
# 5. TIGA PERTANYAAN BISNIS
# ---------------------------------------------------------
st.markdown("## 3 Pertanyaan Bisnis Utama")

# 5.1 Kapan jam sibuk penggunaan sepeda?
st.markdown("### 1. Kapan jam sibuk penggunaan sepeda?")
hourly_usage = filtered_df.groupby("hour")["cnt"].mean().reset_index()
fig_hourly = px.line(
    hourly_usage, 
    x="hour", y="cnt", 
    title="Rata-rata Penggunaan Sepeda per Jam (Setelah Filter)",
    markers=True
)
fig_hourly.update_layout(xaxis_title="Jam (0-23)", yaxis_title="Rata-rata Jumlah Penyewa")
st.plotly_chart(fig_hourly, use_container_width=True)

st.markdown("""
**Insight:**  
- Umumnya, jam 7–9 pagi dan jam 17–18 sore adalah **jam sibuk** (peak hours).  
- Hal ini mengindikasikan penggunaan sepeda yang tinggi untuk **berangkat/pulang kerja**.
""")

# 5.2 Bagaimana perbedaan penggunaan di hari kerja vs hari libur?
st.markdown("### 2. Bagaimana perbedaan penggunaan di hari kerja vs hari libur?")
day_type_df = df.copy()
day_type_df["day_type"] = day_type_df["workingday"].apply(lambda x: "Hari Kerja" if x == 1 else "Hari Libur")

avg_usage_day_type = day_type_df.groupby(["day_type", "hour"])["cnt"].mean().reset_index()
fig_daytype = px.line(
    avg_usage_day_type, 
    x="hour", y="cnt", 
    color="day_type",
    title="Perbandingan Rata-rata Penggunaan: Hari Kerja vs Hari Libur",
    markers=True
)
fig_daytype.update_layout(xaxis_title="Jam (0-23)", yaxis_title="Rata-rata Jumlah Penyewa")
st.plotly_chart(fig_daytype, use_container_width=True)

st.markdown("""
**Insight:**  
- **Hari Kerja**: Dua puncak jelas (pagi & sore) mencerminkan pola komuter.  
- **Hari Libur**: Penggunaan lebih merata, cenderung naik siang–sore untuk rekreasi. 
""")

# 5.3 Bagaimana pengaruh cuaca/temperatur terhadap penggunaan sepeda?
st.markdown("### 3. Bagaimana pengaruh cuaca atau temperatur terhadap penggunaan sepeda?")
fig_temp = px.scatter(
    filtered_df, 
    x="temp", y="cnt", 
    color="weathersit",
    title="Pengaruh Temperatur & Kondisi Cuaca terhadap Penggunaan Sepeda (Setelah Filter)",
    labels={"temp": "Temperatur (Normalized)", "cnt": "Jumlah Penyewa", "weathersit": "Kondisi Cuaca"}
)
st.plotly_chart(fig_temp, use_container_width=True)

st.markdown("""
**Insight:**  
- Semakin **nyaman** suhu (temp), umumnya penggunaan lebih tinggi.  
- Cuaca buruk (hujan/lebat) menurunkan jumlah pengguna.
""")

# ---------------------------------------------------------
# 6. KESIMPULAN & REKOMENDASI
# ---------------------------------------------------------
st.markdown("## Kesimpulan & Rekomendasi")

st.markdown("""
1. **Jam Sibuk**: 
   - Pagi (7–9) dan sore (17–18). Pastikan ketersediaan sepeda lebih banyak.
2. **Hari Kerja vs Libur**:
   - Hari kerja: fokus pada jam berangkat/pulang kerja.  
   - Hari libur: siapkan penawaran/promo untuk jam siang–sore.
3. **Cuaca & Temperatur**:
   - Manfaatkan musim hangat untuk kampanye/ event.  
   - Siapkan strategi jika cuaca buruk (mis. stasiun beratap, promosi indoor).
""")

# ---------------------------------------------------------
# OPSIONAL: TAMPILKAN DATAFRAME LENGKAP
# ---------------------------------------------------------
if st.checkbox("Tampilkan data mentah (preview)"):
    st.dataframe(filtered_df.head(20))

st.write("___")
st.write("**Catatan:** Dashboard ini dibuat untuk mempermudah eksplorasi dan analisis data Bike Sharing.")

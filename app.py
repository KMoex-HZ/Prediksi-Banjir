import streamlit as st
import pickle
import numpy as np

# Load model yang sudah disimpan
with open("models/xgb_flood_model.pkl", "rb") as file:
    model = pickle.load(file)

# Judul aplikasi
st.title("🌊 Prediksi Risiko Banjir dengan Machine Learning")

st.write("Masukkan nilai faktor-faktor berikut untuk mendapatkan prediksi kemungkinan banjir:")

# Input user (21 fitur sesuai dataset)
features = []
feature_names = [
    "MonsoonIntensity", "TopographyDrainage", "RiverManagement", "Deforestation",
    "Urbanization", "ClimateChange", "DamsQuality", "Siltation",
    "AgriculturalPractices", "Encroachments", "IneffectiveDisasterPreparedness",
    "DrainageSystems", "CoastalVulnerability", "Landslides", "Watersheds",
    "DeterioratingInfrastructure", "PopulationScore", "WetlandLoss",
    "InadequatePlanning", "PoliticalFactors"
]

# Buat slider untuk input
for name in feature_names:
    value = st.slider(name, min_value=0, max_value=10, value=5)  # Rentang nilai bisa disesuaikan
    features.append(value)

# Prediksi saat tombol ditekan
if st.button("🔍 Prediksi"):
    input_data = np.array(features).reshape(1, -1)
    prediction = model.predict(input_data)[0]
    
    # Tampilkan hasil prediksi
    st.subheader("📊 Hasil Prediksi:")
    st.write(f"**Kemungkinan Banjir: {prediction:.4f}**")

    # Tampilkan kategori risiko berdasarkan nilai prediksi
    if prediction < 0.3:
        st.success("✅ Risiko Banjir: **Rendah**")
    elif prediction < 0.6:
        st.warning("⚠️ Risiko Banjir: **Sedang**")
    else:
        st.error("🚨 Risiko Banjir: **Tinggi**")

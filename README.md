# 🌊 Prediksi Risiko Banjir dengan Machine Learning

## 🔍 Deskripsi Proyek
Proyek ini bertujuan untuk membangun model prediksi risiko banjir berdasarkan berbagai faktor lingkungan dan sosial-ekonomi. Dengan menggunakan algoritma **XGBoost**, model ini mampu memprediksi probabilitas terjadinya banjir dengan tingkat akurasi yang tinggi.

Aplikasi ini juga memiliki antarmuka berbasis **Streamlit**, sehingga pengguna dapat memasukkan data dan mendapatkan hasil prediksi dengan mudah.

---
## 📃 Dataset
Dataset yang digunakan berasal dari **Flood Prediction Dataset** yang tersedia di Kaggle, dibuat oleh **Naiya Khalid** dan diperbarui 8 bulan yang lalu. Dataset ini berisi informasi penting mengenai faktor-faktor yang mempengaruhi risiko banjir.

**Detail Dataset:**
- **Sumber:** [Kaggle - Flood Prediction Dataset](https://www.kaggle.com/datasets)
- **Jumlah Sampel:** 50.000 baris
- **Jumlah Fitur:** 21 fitur numerik
- **Target Variabel:** `FloodProbability` (Probabilitas banjir)
- **Lisensi:** Attribution 4.0 International (CC BY 4.0)
- **Frekuensi Update:** Tidak diperbarui

**Fitur Penting dalam Dataset:**
- **MonsoonIntensity** (Intensitas Muson)
- **TopographyDrainage** (Drainase Topografi)
- **RiverManagement** (Manajemen Sungai)
- **Deforestation** (Deforestasi)
- **Urbanization** (Urbanisasi)
- **ClimateChange** (Perubahan Iklim)
- **DamsQuality** (Kualitas Bendungan)
- **Siltation** (Sedimentasi)
- **AgriculturalPractices** (Praktik Pertanian)
- **Encroachments** (Pelanggaran Lahan)
- **IneffectiveDisasterPreparedness** (Kesiapsiagaan Bencana yang Buruk)
- **DrainageSystems** (Sistem Drainase)
- **CoastalVulnerability** (Kerentanan Pesisir)
- **Landslides** (Longsor)
- **Watersheds** (Daerah Aliran Sungai)
- **DeterioratingInfrastructure** (Infrastruktur yang Memburuk)
- **PopulationScore** (Kepadatan Penduduk)
- **WetlandLoss** (Kehilangan Lahan Basah)
- **InadequatePlanning** (Perencanaan yang Tidak Memadai)
- **PoliticalFactors** (Faktor Politik)

Tidak ada nilai yang hilang pada dataset ini, sehingga tidak diperlukan imputasi data.

---
## 🎯 Model yang Digunakan
Beberapa model diuji untuk memprediksi **FloodProbability**, dan hasil evaluasi menunjukkan bahwa **XGBoost** memberikan performa terbaik setelah fine-tuning hyperparameter.

| Model                     | MSE    | RMSE   |
|---------------------------|--------|--------|
| **Linear Regression**     | 0.0000 | 0.0000 |
| **Random Forest**         | 0.0007 | 0.0259 |
| **XGBoost (Fine-Tuned)**  | 0.0000 | 0.0060 |

---
## 💻 Instalasi & Cara Menjalankan
### 🛠️ Persyaratan
Pastikan Anda memiliki **Python 3.8+** dan menginstal pustaka berikut:
```sh
pip install -r requirements.txt
```

### 🔄 Training Model
Jalankan skrip berikut untuk melatih model dan menyimpannya:
```sh
python train_model.py
```

### 🏢 Menjalankan Aplikasi Streamlit
Setelah model dilatih, jalankan aplikasi dengan perintah:
```sh
streamlit run app.py
```
Aplikasi akan terbuka di **http://localhost:8501**.

---
## 🌟 Fitur Aplikasi
✅ **Input data langsung melalui antarmuka Streamlit**  
✅ **Prediksi probabilitas banjir berdasarkan faktor lingkungan**  
✅ **Hasil prediksi dalam bentuk angka & kategori risiko (Rendah, Sedang, Tinggi)**  
✅ **Tampilan sederhana & mudah digunakan**  

---
## 💎 Kontribusi
Jika ingin berkontribusi pada proyek ini:
1. **Fork repo ini**
2. **Buat branch baru** (`feature-branch`)
3. **Commit perubahan** (`git commit -m "Deskripsi perubahan"`)
4. **Buat pull request**

---
## 🚀 Pengembangan Selanjutnya
- [ ] Menambahkan fitur **visualisasi data historis**
- [ ] Menggunakan **model deep learning** untuk peningkatan akurasi
- [ ] Deploy aplikasi ke **Streamlit Cloud / Hugging Face Spaces**

Jika ada pertanyaan atau saran, silakan hubungi saya!

---
**💪 Dibuat dengan semangat, semoga bermanfaat!** 🚀




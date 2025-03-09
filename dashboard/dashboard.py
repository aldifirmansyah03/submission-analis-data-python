import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Pastikan path dataset utama benar
dataset_path =dataset_path = "dashboard/main_data.csv"

# Load dataset utama
if os.path.exists(dataset_path):
    df = pd.read_csv(dataset_path, parse_dates=["order_purchase_timestamp"])
else:
    st.error("❌ File main_data.csv tidak ditemukan! Pastikan sudah dibuat di folder yang benar.")
    st.stop()


# Tambahkan Judul Dashboard
st.title("📊 E-Commerce Dashboard")

# Sidebar untuk memilih analisis
st.sidebar.header("Pilih Analisis")

# Pilihan Analisis
menu = st.sidebar.radio(
    "Pilih salah satu:",
    ["Performa Penjualan", "Kategori Produk", "Distribusi Pelanggan"]
)

# 🟢 **Analisis Performa Penjualan**
if menu == "Performa Penjualan":
    st.subheader("📅 Performa Penjualan per Bulan")

    # Buat kolom 'order_purchase_month' jika belum ada
    df["order_purchase_month"] = df["order_purchase_timestamp"].dt.to_period("M")

    # Hitung jumlah order per bulan
    monthly_sales = df.groupby("order_purchase_month")["order_id"].count()

    # Visualisasi
    fig, ax = plt.subplots(figsize=(10, 5))
    monthly_sales.plot(kind="bar", color="skyblue", ax=ax)
    plt.xticks(rotation=45)
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Order")
    plt.title("Jumlah Order per Bulan")

    st.pyplot(fig)

# 🔵 **Analisis Kategori Produk**
elif menu == "Kategori Produk":
    st.subheader("🏷️ Kategori Produk Terlaris")

    # Hitung jumlah produk terjual per kategori
    top_selling_products = df.groupby("product_category_name")["order_id"].count().nlargest(10)

    # Visualisasi
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(y=top_selling_products.index, x=top_selling_products.values, palette="Blues_r", ax=ax)
    plt.xlabel("Jumlah Order")
    plt.ylabel("Kategori Produk")
    plt.title("10 Kategori Produk Terlaris")

    st.pyplot(fig)

# 🔴 **Analisis Distribusi Pelanggan**
elif menu == "Distribusi Pelanggan":
    st.subheader("📍 Distribusi Pelanggan berdasarkan Negara Bagian")

    # Hitung jumlah pelanggan per state
    customer_distribution = df["customer_state"].value_counts()

    # Visualisasi
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=customer_distribution.index, y=customer_distribution.values, palette="viridis", ax=ax)
    plt.xlabel("State")
    plt.ylabel("Jumlah Pelanggan")
    plt.title("Distribusi Pelanggan berdasarkan Negara Bagian")

    st.pyplot(fig)

# Tambahkan informasi footer
st.sidebar.info("Dashboard dibuat menggunakan Streamlit 🚀")

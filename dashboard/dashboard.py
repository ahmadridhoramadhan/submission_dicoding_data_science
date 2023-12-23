import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

try:
    merged_all_customers = pd.read_csv('dashboard/merged_all_customers.csv')
    merged_all_ratings = pd.read_csv('dashboard/merged_all_ratings.csv')
    merged_all_sale = pd.read_csv('dashboard/merged_all_sale.csv')
except FileNotFoundError:
    merged_all_customers = pd.read_csv('merged_all_customers.csv')
    merged_all_ratings = pd.read_csv('merged_all_ratings.csv')
    merged_all_sale = pd.read_csv('merged_all_sale.csv')



def show_product_sales_visualization():
    # Menghitung jumlah produk yang dibeli untuk setiap produk
    product_counts = merged_all_sale.groupby('product_category_name')['order_item_id'].sum().reset_index()

    # Menemukan 5 produk yang paling sering dibeli
    top_products = product_counts.nlargest(5, 'order_item_id')

    # Menemukan 5 produk yang paling jarang dibeli
    low_products = product_counts.nsmallest(5, 'order_item_id').sort_values(by='order_item_id', ascending=False)


    # Membuat palet warna
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    # Membuat dua canvas bersampingan
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

    # Visualisasi kategori produk yang paling banyak dibeli
    sns.barplot(x="order_item_id", y="product_category_name", hue="product_category_name", data=top_products.reset_index()[['product_category_name', 'order_item_id']], palette=colors, ax=ax[0], legend=False)
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("Kategori Produk Terlaris", loc="center", fontsize=15)
    ax[0].tick_params(axis='y', labelsize=12)

    # Visualisasi kategori produk yang paling sedikit dibeli
    sns.barplot(x="order_item_id", y="product_category_name", hue="product_category_name", data=low_products.reset_index()[['product_category_name', 'order_item_id']], palette=sorted(colors, reverse=True), ax=ax[1], legend=False)
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Kategori Produk Paling Tidak Laris", loc="center", fontsize=15)
    ax[1].tick_params(axis='y', labelsize=12)

    plt.suptitle("Kategori Produk Terbaik dan Tidak Terbaik berdasarkan Jumlah Penjualan", fontsize=20)

    # Display the plot in Streamlit
    st.pyplot(fig)












def show_product_categories_rating_visualization():
    # Menemukan 5 kategori produk dengan rating paling tinggi
    top_categories = merged_all_ratings.groupby('product_category_name')['review_score'].mean().nlargest(5)

    # Menemukan 5 kategori produk dengan rating paling rendah
    low_categories = merged_all_ratings.groupby('product_category_name')['review_score'].mean().nsmallest(5)


    # Membuat palet warna
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    # Membuat dua canvas bersampingan
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

    # Visualisasi kategori produk dengan rating paling tinggi
    sns.barplot(x="review_score", y="product_category_name", hue="product_category_name", data=top_categories.reset_index(), palette=colors, ax=ax[0], legend=False)
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("Kategori Produk rating tertinggi", loc="center", fontsize=15)
    ax[0].tick_params(axis='y', labelsize=12)

    # Visualisasi kategori produk dengan rating paling rendah
    sns.barplot(x="review_score", y="product_category_name", hue="product_category_name", data=low_categories.reset_index().sort_values(by='review_score', ascending=False), palette=sorted(colors, reverse=True), ax=ax[1], legend=False)
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Kategori Produk rating paling rendah", loc="center", fontsize=15)
    ax[1].tick_params(axis='y', labelsize=12)

    # set min dan max ratting
    ax[0].set_xlim([0, 5])
    ax[1].set_xlim([5, 0])

    plt.suptitle("Kategori Produk Terbaik dan Tidak Terbaik berdasarkan Jumlah Penjualan", fontsize=20)

    # Display the plot in Streamlit
    st.pyplot(fig)




def show_product_categories_sales_in_each_city_visualization():
    # Menghitung jumlah produk yang dibeli untuk setiap kota
    city_product_counts = merged_all_customers.groupby('customer_city')['order_item_id'].sum()

    # Mengambil 10 kota dengan pembelian barang paling banyak
    top_cities = city_product_counts.nlargest(10)

    # Membuat palet warna
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    # Membuat canvas
    fig, ax = plt.subplots(figsize=(12, 6))

    # Visualisasi kategori produk yang paling banyak dibeli
    sns.barplot(x="order_item_id", y="customer_city", hue="customer_city", data=top_cities.reset_index(), palette=colors, ax=ax, legend=False)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='y', labelsize=12)

    plt.suptitle("kota paling sering melakukan pembelian", fontsize=20)
    st.pyplot(fig)







st.header('dicoding project analysis E-commerce publik:sparkles:')
st.subheader('performance product categories')
show_product_sales_visualization()

st.subheader('product categories rating')
show_product_categories_rating_visualization()

st.subheader('product categories sales in each city')
show_product_categories_sales_in_each_city_visualization()
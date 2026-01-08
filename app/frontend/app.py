import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import requests
from backend.google_image import search_image

st.title("Menu Scanner Demo")

uploaded = st.file_uploader("Upload menu image")

if uploaded:
    st.image(uploaded, caption="Menu uploaded")

    # Send to backend
    files = {"file": uploaded.getvalue()}
    res = requests.post("http://localhost:8000/process_menu", files={"file": uploaded})
    items = res.json()["items"]

    st.header("Detected items")

    for item in items:
        img = search_image(item["name"])
        st.subheader(f"{item['name']} — {item['price']} TWD")
        if img:
            st.image(img, width=200)

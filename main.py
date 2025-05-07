import streamlit as st
import qrcode
from io import BytesIO
import numpy as np
import cv2

st.set_page_config(page_title="QR Code Encoder/Decoder", layout="centered")

st.title("🔳 QR Code Encoder & Decoder")

tab1, tab2 = st.tabs(["🧩 Encode", "🔍 Decode"])

with tab1:
    st.header("QR Code Generator (Encoder)")
    text = st.text_input("Enter text to encode into QR Code")
    
    if st.button("Generate QR Code"):
        if text.strip():
            qr_img = qrcode.make(text)
            
            buffer = BytesIO()
            qr_img.save(buffer, format="PNG")
            buffer.seek(0)

            st.image(
                buffer,
                caption="Your QR Code has been generated"
            )

            buffer.seek(0)
            st.download_button(
                label="📥 Download QR Code",
                data=buffer,
                file_name="myqrcode.png",
                mime="images/png"
            )
        else:
            st.warning("❗ Please enter some text to generate a QR Code.")

with tab2:
    st.header("QR Code Reader")
    upload = st.file_uploader(
        label="Upload your QR Code here for decoding"
    )

    if upload:
        file_byte = np.asarray(bytearray(upload.read()))
        image = cv2.imdecode(file_byte, cv2.IMREAD_COLOR)

        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(image)

        if data:
            st.success("✅ QR Code Decoded Successfully!")
            st.text_area("Decoded Text", data, height=100)
        else:
            st.error("❌ Could not detect or decode the QR Code.")
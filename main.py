import cv2
import streamlit as st
import numpy as np

def enhance_video(input_file, output_file):
    cap = cv2.VideoCapture(input_file)

    if not cap.isOpened():
        st.error("Gagal membuka video")
        return

    width = int(cap.get(3))
    height = int(cap.get(4))

    # Ganti ekstensi file output sesuai dengan format yang diinginkan (.mp4)
    output_file = output_file.replace('.avi', '.mp4')

    # Ganti nilai fourcc sesuai dengan format video MP4
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        enhanced_frame = cv2.flip(frame, 0)

        out.write(enhanced_frame)

    cap.release()
    out.release()

if __name__ == "__main__":
    st.title("Enhance Video App")

    uploaded_file = st.file_uploader("Pilih video untuk ditingkatkan", type=["mp4", "avi"])

    if uploaded_file is not None:
        st.video(uploaded_file)

        output_file = 'enhanced_video.avi'
        enhance_video(uploaded_file, output_file)

        st.success(f"Video telah ditingkatkan. Silakan unduh [di sini](enhanced_video.mp4).")

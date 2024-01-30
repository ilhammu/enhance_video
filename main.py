import cv2
import streamlit as st
import numpy as np
import tempfile
import os

def enhance_video(input_file, output_file):
    # Buka file video
    cap = cv2.VideoCapture(input_file)

    # Periksa apakah video berhasil dibuka
    if not cap.isOpened():
        st.error("Gagal membuka video")
        return

    # Dapatkan properti video
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Buat objek VideoWriter untuk menyimpan video hasil perbaikan
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (width, height))

    while cap.isOpened():
        # Baca frame dari video
        ret, frame = cap.read()

        if not ret:
            break

        # Proses frame untuk meningkatkan kualitas (contoh: flip vertikal)
        enhanced_frame = cv2.flip(frame, 0)

        # Tulis frame yang telah ditingkatkan ke file video output
        out.write(enhanced_frame)

        # Tampilkan frame yang telah ditingkatkan
        st.image(enhanced_frame, channels="BGR")

    # Tutup file video input dan output
    cap.release()
    out.release()

    # Tampilkan tautan unduh setelah pemrosesan selesai
    st.success(f"Video telah ditingkatkan. Unduh di sini: [Download Video]({output_file})")

if __name__ == "__main__":
    st.title("Enhance Video App")

    uploaded_file = st.file_uploader("Pilih video untuk ditingkatkan", type=["mp4", "avi"])

    if uploaded_file is not None:
        # Simpan video sementara sebagai file lokal
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            video_path = temp_file.name

        # Tampilkan video yang diunggah
        st.video(video_path)

        output_file = 'enhanced_video.avi'
        enhance_video(video_path, output_file)

        # Hapus file sementara setelah video ditingkatkan
        os.remove(video_path)

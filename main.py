import cv2
import streamlit as st
import numpy as np
import tempfile
import os
import requests

def enhance_video(input_file, output_file):
    cap = cv2.VideoCapture(input_file)

    if not cap.isOpened():
        st.error("Gagal membuka video")
        return

    width = int(cap.get(3))
    height = int(cap.get(4))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        enhanced_frame = cv2.flip(frame, 0)

        out.write(enhanced_frame)

    cap.release()
    out.release()

def upload_to_tmpfiles(video_path):
    url = "https://tmpfiles.org/api/v1/upload"
    files = {'file': open(video_path, 'rb')}
    response = requests.post(url, files=files)
    return response.json()['url']

if __name__ == "__main__":
    st.title("Enhance Video App")

    uploaded_file = st.file_uploader("Pilih video untuk ditingkatkan", type=["mp4", "avi"])
    st.info('Maksimal video yang dapat diunggah 100MB')
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

        st.success("Video telah ditingkatkan.")
        
        # Unggah video yang telah ditingkatkan ke tmpfiles.org
        enhanced_video_url = upload_to_tmpfiles(output_file)

        # Tampilkan video yang telah ditingkatkan dari tmpfiles.org
        st.video(enhanced_video_url)

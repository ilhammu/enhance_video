import streamlit as st
import cv2
import os

def enhance_video(input_file, output_file):
    cap = cv2.VideoCapture(input_file)

    if not cap.isOpened():
        st.error("Gagal membuka video")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_fps = cap.get(cv2.CAP_PROP_FPS)

    # Use MP4V codec directly for MP4 output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, frame_fps, (width, height), isColor=False)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray)

    cap.release()
    out.release()

st.title("Enhance Video App")

video_data = st.file_uploader("Upload file", ['mp4', 'mov', 'avi'])

if video_data:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(video_data.getvalue())
        video_path = temp_file.name

        st.video(video_path)

        output_file = 'enhanced_video.mp4'
        enhance_video(video_path, output_file)

        os.remove(video_path)  # Remove temporary file

        st.success("Video telah ditingkatkan.")
        st.video(output_file)  # Display the enhanced MP4 video

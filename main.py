import streamlit as st
import cv2
import numpy as np
from io import BytesIO
import base64

st.title('Video Quality Enhancement')

# Upload a video file
video_file = st.file_uploader("Upload a video", type=["mp4"])

if video_file is not None:
    # Read the uploaded video
    video_bytes = video_file.read()

    # Perform video enhancement (e.g., using OpenCV)
    cap = cv2.VideoCapture(BytesIO(video_bytes))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 360))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Apply enhancement operations (e.g., denoising, color correction, sharpening) to the frame
        # For example, you can perform simple grayscale conversion and edge detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        # Write the enhanced frame to the output video
        out.write(frame)

    # Release everything if job is finished
    cap.release()
    out.release()

    # Read the enhanced video file
    with open('output.mp4', 'rb') as file:
        enhanced_video_bytes = file.read()

    st.video(enhanced_video_bytes)

    # Cleanup temporary files
    os.remove('output.mp4')

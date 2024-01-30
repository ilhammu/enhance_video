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
    video_nparray = np.frombuffer(video_bytes, np.uint8)
    frame_array = []
    cap = cv2.VideoCapture(video_nparray.tobytes())

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Apply enhancement operations (e.g., denoising, color correction, sharpening) to the frame
        # For example, you can perform simple grayscale conversion and edge detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        frame_array.append(frame)

    # Write the enhanced frames to a new video file
    height, width, _ = frame_array[0].shape
    out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()

    # Read the enhanced video file
    with open('output.mp4', 'rb') as file:
        enhanced_video_bytes = file.read()

    st.video(enhanced_video_bytes, format='video/mp4')

    # Cleanup temporary files
    os.remove('output.mp4')

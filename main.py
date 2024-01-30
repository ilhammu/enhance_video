import streamlit as st
import cv2
import subprocess

video_data = st.file_uploader("Upload file", ['mp4','mov', 'avi'])

temp_file_to_save = './temp_file_1.mp4'
temp_file_result  = './temp_file_2.mp4'

# func to save BytesIO on a drive
def write_bytesio_to_file(filename, bytesio):
    """
    Write the contents of the given BytesIO to a file.
    Creates the file or overwrites the file if it does not exist yet.
    """
    with open(filename, "wb") as f:
        f.write(bytesio.getbuffer())

def enhance_video_quality(input_file, output_file):
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

        # Proses peningkatan kualitas di sini
        # Misalnya, lakukan operasi pengolahan gambar seperti sharpening atau konversi warna

        out.write(frame)

    cap.release()
    out.release()

if video_data is not None:
    write_bytesio_to_file(temp_file_to_save, video_data)

    # Peningkatan kualitas video
    enhance_video_quality(temp_file_to_save, temp_file_result)

    # Convert video to H264 format using ffmpeg
    subprocess.run(['ffmpeg', '-i', temp_file_result, '-c:v', 'libx264', temp_file_result])

    # Display the enhanced video
    st.video(temp_file_result)
import streamlit as st
import cv2
import subprocess

video_data = st.file_uploader("Upload file", ['mp4','mov', 'avi'], key="file_uploader1")


temp_file_to_save = './temp_file_1.mp4'
temp_file_result  = './temp_file_2.mp4'

# func to save BytesIO on a drive
def write_bytesio_to_file(filename, bytesio):
    """
    Write the contents of the given BytesIO to a file.
    Creates the file or overwrites the file if it does not exist yet.
    """
    with open(filename, "wb") as f:
        f.write(bytesio.getbuffer())

def enhance_video_quality(input_file, output_file):
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

        # Proses peningkatan kualitas di sini
        # Misalnya, lakukan operasi pengolahan gambar seperti sharpening atau konversi warna

        out.write(frame)

    cap.release()
    out.release()

if video_data is not None:
    write_bytesio_to_file(temp_file_to_save, video_data)

    # Peningkatan kualitas video
    enhance_video_quality(temp_file_to_save, temp_file_result)

    # Convert video to H264 format using ffmpeg
    subprocess.run(['ffmpeg', '-i', temp_file_result, '-c:v', 'libx264', temp_file_result])

    # Display the enhanced video
    st.video(temp_file_result)



#from streamlit.proto.Image_pb2 import Image
import cv2
import streamlit as st
import numpy as np
from PIL import Image,ImageEnhance

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)


while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #FRAME_WINDOW.image(frame)

    #converted_img = np.array(frame.convert('RGB'))
    #gray_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
    #FRAME.image(gray_img)
    #img = Image.fromarray(frame)
    #img_convert = img.convert("RGB")
    #convert = np.array(img_convert)
    #cinza = cv2.cvtColor(convert,cv2.COLOR_RGB2GRAY)

    img = Image.fromarray(frame)
    img_convert = img.convert("RGB")
    #convert = np.array(img_convert)
    contraste = ImageEnhance.Contrast(img_convert)
    contraste_img = contraste.enhance(500.0)
    #FRAME.image(contraste_img)
    FRAME_WINDOW.image(contraste_img)
else:
    st.write('Stopped')
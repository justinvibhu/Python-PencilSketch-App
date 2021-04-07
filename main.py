import streamlit as st
import cv2
import numpy as np
from PIL import Image


def Pencil(x, y):
    return cv2.divide(x, 225-y, scale=256)


def PencilSkecher(input_img):
    img_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smooth = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
    final_img = Pencil(img_gray, img_smooth)
    return final_img

# front end


st.title("PencilSketcher App")
st.write("This Apps is to help to convert your photo into realitics Pencil Sketch")

# file uploader
file_img = st.sidebar.file_uploader(
    "Upload Your Photo", type=['jpg', 'jpeg', 'png'])

if file_img is None:
    st.write("Please any Image ")
else:
    input_image = Image.open(file_img)
    final_sketch = PencilSkecher(np.array(input_image))
    st.write("*** INPUT IMAGE ***")
    st.image(file_img, width=500, caption="Original Image")
    st.write("*** OUTPUT IMAGE ***")
    st.image(final_sketch, width=500, caption="Sketch Image")

# Importlibraries
import streamlit as st
import numpy as np
from PIL import Image

# title of the app
st.title('Image flip app')

# file uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Check if an image has been uploaded
if uploaded_file is not None:
    # Open the image 
    image = Image.open(uploaded_file)

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Display original image
    st.image(image, caption='Original Image')

    # checkbox to flip the image
    flip_image = st.checkbox('Flip Image')

    # if the checkbox is checked
    if flip_image:
        # Flip the image
        flipped_image = np.fliplr(image_array)

        # Convert the flipped image 
        flipped_image = Image.fromarray(flipped_image)

        # Display the flipped image
        st.image(flipped_image, caption='Flipped Image')

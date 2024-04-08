import streamlit as st
from streamlit_drawable_canvas import st_canvas
from joblib import load
from PIL import Image
import numpy as np

knn_clf_loaded = load('knn22_mnist_model.joblib')

st.title('Handwritten Digit Recognition')
st.markdown('Draw a digit on the canvas below and click the "Predict" button.')

canvas_result = st_canvas(
    fill_color="black", 
    stroke_width=20,
    stroke_color="white",
    background_color="black",
    width=280,
    height=280,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button('Predict'):
    if canvas_result.image_data is not None:
        img_data = canvas_result.image_data
        
        img = Image.fromarray(img_data.astype('uint8'), 'RGBA')
        img_gray = img.convert('L')
        
        img_resized = img_gray.resize((28, 28))
        
        img_array = np.array(img_resized).reshape(784) / 255.0
        
        prediction = knn_clf_loaded.predict([img_array])
        
        st.write(f'Predicted digit: {prediction[0]}')

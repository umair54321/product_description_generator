import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure the Generative AI API
API_KEY = st.secrets["gemini_api_key"]
genai.configure(api_key=API_KEY )

# Load the Generative Model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Streamlit UI
st.title("Product Description Generator")
st.write("Upload an image, and the model will generate a product description.")

# File uploader for image input
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Generate the product description
    if st.button("Generate Description"):
        # Prompt the model with the uploaded image and a description request
        response = model.generate_content([image, "Write a product description of this product image"])

        # Display the generated description
        st.markdown("**Generated Description:**")
        st.markdown(">" + response.text)

else:
    st.write("Please upload an image to generate a description.")

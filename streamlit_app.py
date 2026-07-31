import streamlit as st
import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

# Load model
MODEL_PATH = "./SI26-urdu-ocr-model"

processor = TrOCRProcessor.from_pretrained(MODEL_PATH)
model = VisionEncoderDecoderModel.from_pretrained(MODEL_PATH)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval()

st.set_page_config(page_title="Urdu OCR", page_icon="📝")

st.title("📝 Urdu OCR")
st.write("Upload an image containing printed Urdu text to extract the text.")

uploaded_file = st.file_uploader(
    "Choose an Urdu image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    pixel_values = processor(
        images=image,
        return_tensors="pt"
    ).pixel_values.to(device)

    with torch.no_grad():
        generated_ids = model.generate(pixel_values)

    prediction = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    st.subheader("Extracted Urdu Text")

    st.text_area(
        "",
        prediction,
        height=120
    )

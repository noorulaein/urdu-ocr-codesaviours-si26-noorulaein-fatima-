import gradio as gr
import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

# Load model from the current directory
processor = TrOCRProcessor.from_pretrained(".")
model = VisionEncoderDecoderModel.from_pretrained(".")
model.eval()

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

def extract_urdu_text(image):
    if image is None:
        return "Please upload an image."

    pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)

    with torch.no_grad():
        generated_ids = model.generate(pixel_values)

    text = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    if text.strip() == "":
        return "Could not extract text."

    return text

demo = gr.Interface(
    fn=extract_urdu_text,
    inputs=gr.Image(type="pil", label="Upload Urdu Image"),
    outputs=gr.Textbox(label="Extracted Urdu Text"),
    title="Urdu OCR - Code Saviours SI-26",
    description="Upload an Urdu image and extract its text."
)

demo.launch()

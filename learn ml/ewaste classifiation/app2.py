from keras.models import load_model 
from PIL import Image, ImageOps  
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

@st.cache_resource
def load_classification_model():
    try:
        model = load_model("keras_model.h5", compile=False)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

@st.cache_data
def get_class_names():
    try:
        with open("labels.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        st.error("Labels file not found.")
        st.stop()

@st.cache_data
def classify_waste(_img, _model, _class_names):
    np.set_printoptions(suppress=True)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = _img.convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    prediction = _model.predict(data)
    index = np.argmax(prediction)
    class_name = _class_names[index]
    confidence_score = prediction[0][index]
    return class_name, confidence_score, prediction[0]


def disposal_checklist(label):
    checklists = {
        "0 Mother Board (PCB)": [
            "Separate PCBs from other e-waste.",
            "Deliver to an authorized e-waste recycler.",
            "Avoid burning or throwing in landfills."
        ],
        "1 Battery": [
            "Remove batteries from devices before disposal.",
            "Drop off at designated battery recycling points.",
            "Avoid mixing batteries with general waste."
        ],
        "2 Mobile": [
            "Back up and erase personal data.",
            "Donate or recycle through authorized centers.",
            "Avoid selling to unauthorized collectors."
        ],
        "3 class": [
            "Unplug and remove water connections.",
            "Contact a recycling center for pickup.",
            "Ensure proper dismantling for parts recycling."
        ]
    }
    return checklists.get(label, ["Dispose of responsibly at a local recycling center."])

st.set_page_config(layout='wide', page_title="Waste Classifier")

st.sidebar.title("How to Use")
st.sidebar.markdown("""
1. **Upload Image**: Click "Browse files" to upload an image of waste.
2. **Reference Images**:
""")
st.sidebar.image("https://tse3.mm.bing.net/th?id=OIP.UsliiPhVmb4IQHGkPHyNLwHaE7&pid=Api&P=0&h=180", caption="Motherboard Example", width=200)
st.sidebar.image("https://www.lifewire.com/thmb/iyUZpl6BuU1dkIo35ApAcE_RTA4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-671200866-battery-recycle-containter-xxx-ca748fd416884c1b8e626b7852d0538a.jpg", caption="Battery Example", width=200)
st.sidebar.image("https://tse4.mm.bing.net/th?id=OIP.L_IBmQ5JmWqU-k1Ezm9DjgHaFj&pid=Api&P=0&h=180", caption="Mobile Example", width=200)
st.sidebar.image("https://tse3.mm.bing.net/th?id=OIP.UOQb7-1NxgwXN817Qo_CVwHaFj&pid=Api&P=0&h=180", caption="Washing Machine Example", width=200)
st.sidebar.info("Ensure clear and well-lit images for better classification.")

st.title("Waste Classifier Sustainability App")

model = load_classification_model()
class_names = get_class_names()


input_img = st.file_uploader("Upload your waste image", type=['jpg', 'png', 'jpeg','webp'])
if input_img is not None:
    image_file = Image.open(input_img)
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.info("Your Uploaded Image")
        st.image(image_file, caption="Uploaded Image", width=300)
        

    with col2:
        st.info("Classification Result")
        label, confidence_score, prediction = classify_waste(image_file, model, class_names)
        st.success(f"**Classified as:** {label}")
        st.metric("Confidence Score", f"{confidence_score:.2f}")
        
    with col3:
        checklist_items = disposal_checklist(label)
        st.info("Follow these steps to dispose of responsibly:")
        progress = 0
        progress_bar = st.progress(progress)
        for step in checklist_items:
            if st.checkbox(step):
                progress += 100 // len(checklist_items)
                progress_bar.progress(progress)
        if progress == 100:
            st.success("All steps completed! Thank you for recycling responsibly.")

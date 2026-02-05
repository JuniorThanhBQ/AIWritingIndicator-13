import streamlit as st
import pandas as pd
import numpy as np
import time
from transformers import pipeline
from services.pdf_reader_services import PdfReaderManager
from services.pipeline import PipelineManager

MODEL_NAME = "Juner/AI-generated-text-detection"

@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model=MODEL_NAME
    )

clf = load_model()

st.set_page_config(
    page_title="AI Writing Indicator", 
    layout="wide"              
)
st.title("Chương trình kiểm tra AI")
data = st.file_uploader("Tải file pdf", type="pdf")

if data:
    data_text = PdfReaderManager.load_file(data)
    write_permission = True
    label = "Nội dung từ File PDF:"
else:
    data_text = ""
    write_permission = False
    label = "Nhập văn bản tại đây:"

text = st.text_area(label=label, value=data_text, disabled=write_permission)

if st.button("Kiểm tra ngay"):
    text = PipelineManager.input_processing(text)

    if text.strip() == "":
        st.warning("Vui lòng nhập văn bản hợp lệ để kiểm tra!")

    with st.spinner("Đang phân tích dữ liệu..."):  
        try:
            output_processing = PipelineManager.output_processing(text, clf, st)
        except Exception as e:
            st.error(f"Hệ thống đang bị lỗi vui lòng quay lại sau!")

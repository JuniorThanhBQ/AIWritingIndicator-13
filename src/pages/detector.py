import streamlit as st
from transformers import pipeline

from services.generate_docx_services import generate_docx
from services.pdf_reader_services import PdfReaderManager
from services.pipeline import PipelineManager
from utils.utils import init_page, render_footer


@st.cache_resource
def load_model():
    return pipeline("text-classification", model="Juner/AI-generated-text-detection")


clf = load_model()

init_page("AI Detector")

st.markdown("""
<div class="header-split">
    <h1 class="title-split">AI <span class="blue-grad">Writing</span> Indicator</h1>
    <div class="status-badge">Trạng thái: Hoạt động</div>
</div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns(2, gap="medium")

with col_left:
    st.markdown('<p class="label-v3">INPUT TẠI ĐÂY</p>', unsafe_allow_html=True)
    data = st.file_uploader("Upload PDF file", type="pdf", label_visibility="collapsed")

    if data:
        data_text = PdfReaderManager.load_file(data)
        write_permission = True
    else:
        data_text = ""
        write_permission = False

    text = st.text_area(
        label="Input Area",
        value=data_text,
        height=500,
        placeholder="Dán văn bản hoặc tải file PDF",
        disabled=write_permission,
        label_visibility="collapsed"
    )

    check_btn = st.button("PHÂN TÍCH NGAY", use_container_width=True)

with col_right:
    st.markdown('<p class="label-v3">KẾT QUẢ PHÂN TÍCH</p>', unsafe_allow_html=True)
    result_placeholder = st.container(border=True)

    with result_placeholder:
        if check_btn:
            processed_text = PipelineManager.input_processing(text)

            if not processed_text.strip():
                st.info("Vui lòng nhập nội dung ở bên trái.")
            else:
                with st.spinner("Đang xử lý yêu cầu"):
                    try:
                        PipelineManager.output_processing(
                            processed_text, clf, st
                        )
                        result = clf(processed_text)

                        if isinstance(result, list):
                            result = result[0]

                        label = result.get("label", "Unknown")
                        score = result.get("score", 0)

                        label_map = {
                            "LABEL_0": "Do con người viết",
                            "LABEL_1": "Do AI viết"
                        }

                        label = label_map.get(label, label)
                        result_label = label

                        st.markdown(
                            '<div style="margin-top:20px;"></div>',
                            unsafe_allow_html=True
                        )

                        docx_file = generate_docx(
                            processed_text,
                            result_label,
                            score
                        )

                        st.download_button(
                            label="XUẤT BÁO CÁO (.DOCX)",
                            data=docx_file,
                            file_name="Kết quả kiểm tra.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            use_container_width=True
                        )

                    except Exception as e:
                        st.error(f"Lỗi kết nối mô hình: {e}")

        else:
            st.markdown(
                '<div class="empty-state"><p>Kết quả sẽ hiển thị tại đây.</p></div>',
                unsafe_allow_html=True
            )

render_footer()

import streamlit as st

def load_css():
    try:
        with open("assets/css/styles_home.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css()

st.set_page_config(page_title="AI Writing Indicator", layout="wide")

st.markdown("""
<div class="main-wrapper">
    <div class="header-section">
        <p class="eyebrow">OPEN UNIVERSITY • RESEARCH PROJECT</p>
        <h1 class="main-title">AI WRITING<br><span class="text-outline">INDICATOR</span></h1>
        <p class="sub-text">Hệ thống phân tích ngôn ngữ tự nhiên, xác định độ tin cậy và nguồn gốc văn bản bằng thuật toán nâng cao.</p>
    </div>
""", unsafe_allow_html=True)

st.write("")
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
    <div class="glass-card">
        <div class="card-num">01</div>
        <div class="card-content">
            <h3>NHẬP VĂN BẢN</h3>
            <p>Kiểm tra trực tiếp các đoạn văn bản ngắn hoặc bài luận. Nhận kết quả phân tích theo thời gian thực với biểu đồ chi tiết.</p>
            <div class="action-link">BẮT ĐẦU PHÂN TÍCH →</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card">
        <div class="card-num">02</div>
        <div class="card-content">
            <h3>XỬ LÝ TỆP TIN</h3>
            <p>Hỗ trợ quét tệp số lượng lớn (PDF, DOCX). Hệ thống tự động bóc tách nội dung và xuất báo cáo kiểm định chuyên sâu.</p>
            <div class="action-link">TẢI TỆP LÊN →</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="footer-minimal">
        <div class="footer-content">
            <span>© 2026 OUEL PROJECT</span>
            <span class="dot">•</span>
            <span>DEVELOPED BY OU STUDENTS</span>
            <span class="dot">•</span>
            <span>v2.0 STABLE</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
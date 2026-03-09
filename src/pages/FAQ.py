import streamlit as st

def load_css():
    try:
        with open("assets/css/styles_FAQ.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

st.set_page_config(page_title="Tài liệu hướng dẫn | OUEL", layout="wide")
load_css()

st.markdown("""
<div class="guide-wrapper-light">
    <div class="header-light">
        <div class="badge-light">KỶ NGUYÊN SỐ</div>
        <h1 class="hero-text-light">AI Writing <span class="gradient-text-blue">Indicator</span></h1>
        <p class="description-light">Tài liệu hướng dẫn vận hành hệ thống kiểm định văn bản dành cho sinh viên Open University.</p>
    </div>
""", unsafe_allow_html=True)

cols = st.columns(4)
navs = ["01 CHUẨN BỊ", "02 KIỂM ĐỊNH", "03 KẾT QUẢ", "04 LƯU TRỮ"]
for i, name in enumerate(navs):
    cols[i].markdown(f'<div class="nav-item-light">{name}</div>', unsafe_allow_html=True)

st.write("")

def render_step_light(num, title, text, points):
    col1, col2 = st.columns([1.2, 1], gap="large")
    with col1:
        st.markdown(f"""
        <div class="step-box-light">
            <div class="step-num-light">{num}</div>
            <h2 class="step-title-light">{title}</h2>
            <p class="step-summary-light">{text}</p>
            <div class="step-points-light">
                {"".join([f'<div class="point-item-light">{p}</div>' for p in points])}
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="ui-mockup-light">
            <div class="mockup-indicator">MÔ PHỎNG {num}</div>
            <div class="mockup-line"></div>
            <div class="mockup-line" style="width: 60%;"></div>
            <div class="mockup-btn"></div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="main-content-light">', unsafe_allow_html=True)

render_step_light("01", "KHỞI TẠO VÀ ĐỊNH DANH",
               "Thiết lập môi trường làm việc ban đầu để hệ thống nhận diện người dùng.",
               ["Đăng nhập thông qua tài khoản sinh viên OU", "Xác nhận quyền truy cập API", "Chọn mục tiêu TOEIC (Ví dụ: 650+)"])

st.markdown('<div class="spacer-light"></div>', unsafe_allow_html=True)

render_step_light("02", "PHƯƠNG THỨC KIỂM ĐỊNH",
               "Tải lên nội dung cần đánh giá độ thuần thục và nguồn gốc.",
               ["Dán văn bản trực tiếp (Plain Text)", "Tải tệp tin PDF/Word (Lọc bỏ hình ảnh tự động)", "Xác nhận bắt đầu quá trình phân tích"])

st.markdown('<div class="spacer-light"></div>', unsafe_allow_html=True)

render_step_light("03", "ĐỌC HIỂU CHỈ SỐ AI",
               "Giải mã các báo cáo được hệ thống trích xuất sau quá trình quét.",
               ["Mức độ dự đoán AI (Tính bằng %)", "Highlight các đoạn văn bản nghi vấn", "Gợi ý chỉnh sửa để tăng tính học thuật"])

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h2 class='faq-header-light'>GIẢI ĐÁP THẮC MẮC</h2>", unsafe_allow_html=True)
f1, f2 = st.columns(2)
with f1:
    with st.expander("Làm sao để tăng độ chính xác?"):
        st.write("Văn bản nên có độ dài tối thiểu 150 từ để thuật toán phân tích được cấu trúc câu tốt nhất.")
with f2:
    with st.expander("Hệ thống có lưu bài viết không?"):
        st.write("Dữ liệu chỉ lưu tạm thời trong phiên làm việc và được xóa ngay sau khi bạn đóng trình duyệt.")

st.markdown("""
    <div class="footer-light">
        <p>© 2026 OUEL ENGLISH LEARNING • OPTIMIZED FOR ACADEMIC INTEGRITY</p>
    </div>
</div>
""", unsafe_allow_html=True)
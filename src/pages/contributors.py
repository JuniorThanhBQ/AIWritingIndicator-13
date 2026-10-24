import streamlit as st

from utils.utils import init_page, render_footer

init_page("Những nhà phát triển")

st.markdown("""
<div class="main-wrapper">
    <div class="header-section">
        <p class="eyebrow">HCMC-OU • AI DETECTOR PROJECT</p>
        <h1 class="main-title">NHÀ PHÁT TRIỂN</h1>
        <p class="sub-text">Ba thành viên cùng xây dựng công cụ AI Writing Indicator, từ dữ liệu và mô hình đến ứng dụng thực tế. Dự án xuất phát từ ý tưởng đơn thuần nhưng đã được hiện thực hóa bằng các kỹ thuật trí tuệ nhân tạo.</p>
    </div>
""", unsafe_allow_html=True)

contributors = [
    {
        "name": "Đào Thị Kim Ngân",
        "student_id": "2351050111",
        "role": "Thành viên",
        "focus": "Dữ liệu và huấn luyện mô hình",
        "responsibilities": "Xây dựng code templates, thiết kế pipeline xử lý, chuẩn bị dữ liệu và huấn luyện mô hình.",
        "github": "https://github.com/kngann2201",
    },
    {
        "name": "Nguyễn Thanh Phong",
        "student_id": "2351050133",
        "role": "Thành viên",
        "focus": "Ứng dụng và tích hợp hệ thống",
        "responsibilities": "Phát triển ứng dụng, tích hợp mô hình vào hệ thống và xây dựng bộ kiểm thử ứng dụng để đánh giá hiệu quả thực tế của mô hình.",
        "github": "https://github.com/ITPhongou23",
    },
    {
        "name": "Văn Trung Thành",
        "student_id": "2351050164",
        "role": "Trưởng nhóm",
        "focus": "Nghiên cứu và định hướng dự án",
        "responsibilities": "Phân tích lý thuyết, lập kế hoạch thực hiện, thu thập dữ liệu, hỗ trợ xử lý dữ liệu và huấn luyện mô hình, đánh giá kết quả và viết báo cáo tổng kết.",
        "github": "https://github.com/JuniorThanhBQ",
    },
]

for column, contributor in zip(st.columns(3, gap="medium"), contributors):
    with column.container(border=True, height="stretch"):
        st.badge(contributor["role"], color="blue")
        st.subheader(contributor["name"])
        st.caption(f"MSSV: {contributor['student_id']}")
        st.markdown(f"**{contributor['focus']}**")
        st.markdown(contributor["responsibilities"])
        st.space("stretch")
        st.link_button(
            f"GitHub",
            contributor["github"],
            icon=":material/open_in_new:",
            width="stretch",
        )

st.divider()
st.subheader("Ghi chú đặc biệt từ Thành", anchor=False)
st.markdown(
    "Cảm ơn hai bạn đã đồng hành cùng mình trong dự án này. Đó là một hành trình dài "
    "với nhiều gian nan và thử thách, nhưng chúng ta đã cùng nhau vượt qua, và mình "
    "rất vui vì điều đó. Để tiếp tục duy trì và phát triển repository này lâu dài, "
    "mình xin phép khởi động lại vòng đời phát triển phần mềm (SDLC) của dự án "
    "nhằm khám phá và phát triển thêm những khía cạnh mới."
)
st.caption("Văn Trung Thành (JuniorThanhBQ)")

render_footer()

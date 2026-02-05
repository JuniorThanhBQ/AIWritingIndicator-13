#!/bin/bash

read -p "Bạn đang đứng ở thư mục root của dự án? (y/n): " confirm

if [[ "$confirm" != [yY] && "$confirm" != [yY][eE][sS] ]]; then
    echo "Vui lòng đứng ở thư mục root của dự án để chạy src/run_streamlit."
    exit 1
fi

if [ ! -d "venv" ]; then
    python -m venv venv
    echo "Đã tạo môi trường ảo"
else
    echo "Đã tồn tại môi trường ảo"
fi

if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    echo "Lỗi kích hoạt"
    exit 1
fi

if [ -f "requirements/requirements.txt" ]; then
    pip install -r requirements/requirements.txt
else
    pip install streamlit
fi

cd src
streamlit run app.py
#!/bin/bash

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

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    pip install streamlit
fi

cd src
streamlit run app.py
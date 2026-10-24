.DEFAULT_GOAL := help

.PHONY: help upgrade run sync-all

help:
	@echo "make upgrade   - Upgrade dependencies with uv sync --upgrade"
	@echo "make run       - Start Streamlit with uv run streamlit run src/main.py"
	@echo "make install  - Sync all workspace packages with uv sync --all-packages"

install:
	uv sync --all-packages

upgrade:
	uv sync --upgrade

run:
	uv run streamlit run src/main.py

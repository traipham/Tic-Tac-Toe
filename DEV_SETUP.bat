@ECHO OFF
if exist .venv (
    echo virtual environment already exist!

    .\.venv\Scripts\activate.bat

    pip install -e tkinter_page_router\.
) else (
    python3 -m venv .venv 
)



import streamlit as st
import io
from io import StringIO
from ai import get_code
from load_code import run_function
from dotenv import load_dotenv

load_dotenv()

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

conversion_text = st.text_area("Transformation Text", placeholder="write description of transformation here")
if st.button("Apply transformation"):
    conversion_code = get_code(conversion_text, model="gpt-3.5-turbo", header_rows=None)
    st.code(conversion_code, language='python')

    memory_buffer = io.StringIO()
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    run_function(conversion_code, stringio, memory_buffer)

    st.write(memory_buffer.getvalue())


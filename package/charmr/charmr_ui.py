import streamlit as st
import io
from io import StringIO
from ai import get_code
from load_code import run_function
from dotenv import load_dotenv
import streamlit_scrollable_textbox as stx

load_dotenv()

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    stx.scrollableTextbox(str(bytes_data), height=300, border=False)

    conversion_text = st.text_area("Transformation Text", placeholder="write description of transformation here")
    if st.button("Apply transformation"):
        with st.spinner("AI Processing Request"):
            conversion_code = get_code(conversion_text, model="gpt-3.5-turbo", header_rows=None)
        with st.expander("Transformation Code", expanded=False):
            st.code(conversion_code, language='python')

        with st.spinner("Running Transformation Code"):
            memory_buffer = io.StringIO()
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            run_function(conversion_code, stringio, memory_buffer)

        st.write(memory_buffer.getvalue())

        st.download_button(
            label="Download Result",
            data=memory_buffer.getvalue(),
            file_name='result.txt',
            # mime='text/csv',
        )


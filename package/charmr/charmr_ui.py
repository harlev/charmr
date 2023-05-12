import streamlit as st
import io
from io import StringIO
from ai import get_code
from load_code import run_function
from dotenv import load_dotenv
import streamlit_scrollable_textbox as stx

load_dotenv()

st.set_page_config(
    page_title="Charmr - AI File Transform",
    page_icon=":magic-wand:",
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden; height: 0%;}
        <style>
        div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
        div[data-testid="stDecoration"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
        div[data-testid="stStatusWidget"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("Charmr AI")
st.markdown("""
Use the power of AI to transform files, using a plain text description.  
Get the command line version [GitHub](https://github.com/harlev/charmr)  
Install the [Python package](https://pypi.org/project/charmr/)  
  
#### Examples
These are the commands you can use to tranform your files. The examples deal with CSV and JSOM, but other file format should work too.
* convert csv to json
* read the csv, remove the header row, keep only the second column and output the square of the values
* input a csv file with day,month,year column headers. output a JSON file with an extra field which is the unix timestamp for the date represented in each row  
  
**Note:** The AI is clever and creative. But it is not perfect. You may need to use some *Prompt Engineering* to get the result you want

""")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    input_stringio = uploaded_file.getvalue().decode("utf-8")
    with st.expander("Input File", expanded=True):
        stx.scrollableTextbox(input_stringio, height=300, border=False)

    input_sample = input_stringio[:1000]

    conversion_text = st.text_area("Transformation Text", placeholder="write description of transformation here")
    if st.button("Apply transformation"):
        with st.spinner("AI Processing Request"):
            conversion_code = get_code(conversion_text, model="gpt-3.5-turbo", header_rows=input_sample)
        with st.expander("Transformation Code", expanded=False):
            st.code(conversion_code, language='python')

        with st.spinner("Running Transformation Code"):
            memory_buffer = io.StringIO()
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            run_function(conversion_code, stringio, memory_buffer)

        formatTed_output = memory_buffer.getvalue().replace("\n", "  \n")
        st.write(formatTed_output)

        st.download_button(
            label="Download Result",
            data=memory_buffer.getvalue(),
            file_name='result.txt',
            # mime='text/csv',
        )


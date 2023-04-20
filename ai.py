import openai
import os

SYSTEM = """you are a file converter code generator. 
You will get a description of the source and target files format, and any conversion, manipulation, 
filtering or transformation to apply on the source to generate the target. 
You will output a python function.
The source input is a stream.
skip empty lines or lines with only whitespace in the input stream.
The target output is a stream as well.
The function name will be "file_convert". 
function signature is "file_convert(input_stream, output_stream)"
Generate only the code, with no comments. 
Don't generate any wrapper to the code. 
The output should be compilable as python code, version 3.8.
prefer string manipulation over using external packages where possible. 
Do not output any explanation."""


prompt_with_rows = """
{prompt}. 
here are the first rows of the input file, use them to understand the file structure: 
{header_rows}
"""


def get_code(prompt: str, model="gpt-3.5-turbo", header_rows=None):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if header_rows:
        prompt = prompt_with_rows.format(prompt=prompt, header_rows=header_rows)

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": f"{SYSTEM}"},
            {"role": "user", "content": f"{prompt}"},
        ],
        temperature=0.0,
        max_tokens=2048
        )

    code = response["choices"][0]["message"]["content"]
    code = code.strip("```")

    return code




import openai
import os

SYSTEM = """you are a file converter code generator. 
You will get a description of the source and target files format, and any conversion, manipulation, 
filtering or transformation to apply on the source to generate the target. 
You will output a python function that accepts the text of the source file as a string and returns the target file content as string.
The function name will be "file_convert". 
Generate only the code, with no comments. 
Don't generate any wrapper to the code. 
The output should be compilable as python code, version 3.8.
prefer string manipulation over using external packages where possible. 
Do not output any explanation."""


def get_code(prompt: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
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




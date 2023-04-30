# charmr
#### a Magical AI File Converter

[![PyPI version](https://badge.fury.io/py/charmr.svg)](https://badge.fury.io/py/charmr)
<a href="https://github.com/harlev/charmr/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
</a>
[![Downloads](https://pepy.tech/badge/charmr)](https://pepy.tech/project/charmr)

This application will convert, transform, filter etc. any text based common file format into another file, based on a text description of the required result.  
It is using GPT-3.5/4 to generate code that will run the conversion locally. The actual input data is not being sent outside of the local machine.

### Getting Started
```commandline
pip install charmr
```

### Set OpenAI API Key
```commandline
export OPENAI_API_KEY=<your open ai api key>
```

### Usage
```options:
options:
  -h, --help            show this help message and exit
  --input_file INPUT_FILE, -i INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE, -o OUTPUT_FILE
                        Output file
  --conversion CONVERSION, -c CONVERSION
                        Conversion description
  --alias ALIAS, -a ALIAS
                        Conversion alias, for reuse
  --view_code_only, -v  View code without running
  --gpt_4, -4           Use GPT-4
  --include_input_rows INCLUDE_INPUT_ROWS, -r INCLUDE_INPUT_ROWS
                        Include N input rows in prompt

  ```

* Define `--input_file`, `--output_file` and `--conversion` for basic functionality.
* Can also use stdin and/or stdout instead of defining in/out path.
* Adding an `--alias` will save the conversion in a `.charmr` file.  
* Then you can specify `--alias` without providing `--conversion` to repeat the same conversion.  
* Define `--view_code_only` will only print out the code without running it. Use this to review generated code for safety. Specifying `--alias` will save it to be reused.
* Use `--gpt_4` to use GPT-4 to generate code. Default is `gpt-3.5-turbo`
* Specify `include_input_rows` with number of rows to include in prompt. This can improve code generation.

e.g. `charmr -i input.csv -o output.json -c "convert csv to json"`  
OR   `charmr -c "convert csv to json" < input.csv > output.json`  
OR a more fluent use
```
cat input.csv | charmr -4 -c "convert the csv to json and keep just the first and third columns" | jq .
[
  {
    "a": "1",
    "c": "3"
  },
  {
    "a": "4",
    "c": "6"
  }
]
```  
Emulating the `cut` utility:  
`cat input.csv | cut -d"," -f2`  
Same thing with `charmr`  
`cat input.csv | charmr -4 -c "read the csv and keep only the second column"`  

Then combining transformation and filtering  
`cat input.csv | charmr -4 -c "read the csv, remove the header row, keep only the second column and output the square of the values"`

### Examples
#### Basic conversion
input `csv`  
```
a, b, c
1, 2, 3
4, 5, 6
```
conversion `convert csv to json`  
output `json`
```json
[{"a": "1", " b": " 2", " c": " 3"}, {"a": "4", " b": " 5", " c": " 6"}]
```

#### Column manipulation
input `csv`  
```
a, b, c
1, 2, 3
4, 5, 6
```
conversion `the input file is a CSV with column headers a,b,c. the output file is a CSV. create a new column ac with the multiplication of a and c`  
output `csv`
```
a,b,c,ac
1,2,3,3
4,5,6,24
```

#### Conversion Logic
input `csv`
```
day,month,year
11,3,2021
2,8,1999
```
conversion `input a csv file with day,month,year column headers. output a JSON file with an extra field which is the unix timestamp for the date represented in each row"`  
output `json`
```json
[{"day": "11", "month": "3", "year": "2021", "timestamp": 1615449600}, {"day": "2", "month": "8", "year": "1999", "timestamp": 933577200}]
```


### Disclaimer
The success of each conversion depends on GPT-3.5 generating the correct code for the task.
It also depends on the conversion string correctly describing the input and the logic of manipulating it.  


### Security / Safety
Input file data never leaves your local machine. Only the conversion description is sent to OpenAI to generate the conversion code.  
Note that using the '--include_input_rows N' option **will** send the first N rows of the input file to GPT to help with code generation accuracy

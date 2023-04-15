# charmr
#### a Magical File Converter

This application will convert, transform, filter etc. any text based common file format into another file, based on a text description of the required result. 

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
  ```

* define `--input_file`, `--output_file` and `--conversion` for basic functionality.  
* adding an `--alias` will save the conversion in a `.charmr` file.  
* then you can specify `--alias` without providing `--conversion` to repeat the same conversion.  
* define `--view_code_only` will only print out the code without running it. Use this to review generated code for safety. Specifying `--alias` will save it to be reused.  

e.g. `charmr -i input.csv -o output.json -c "convert csv to json" `

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
conversion `the input file is a CSV with column heasers a,b,c. the output file is a CSV. create a new column ac with the multiplication of a and c`  
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
Input file data never leaves your local machine. Only the conversion description is sent to OpanAI to generate the conversion code.
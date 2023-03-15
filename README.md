# charmr
#### a Magical File Converter

This application will convert, transform, filter etc. any text based common file format into another file, based on a text description of the required result. 

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

e.g. `python main.py -i input.csv -o output.json -c "convert csv to json" `

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
conversion `move column a after column c. create a new column ac with the multiplication of a and c`  
output `json`
```json
[{"a": "1", " b": " 2", " c": " 3"}, {"a": "4", " b": " 5", " c": " 6"}]
```

### Security / Safety

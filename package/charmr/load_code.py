def run_function(code_string, in_stream, out_stream):
    # Compile the code string
    compiled_code = compile(code_string, '<string>', 'exec')

    # Create a dictionary to hold the function namespace
    function_namespace = {}

    # Execute the compiled code in the function namespace
    exec(compiled_code, function_namespace)

    # Get the function from the namespace
    function = function_namespace.get('file_convert')

    # Call the function with the given parameter
    result = function(in_stream, out_stream)

    # Return the result
    return result




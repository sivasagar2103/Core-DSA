from typing import get_type_hints, Callable
from inspect import signature

def get_doc(fun: Callable) -> str:
    """
    Generate documentation for a function following specific formatting rules.
    
    Parameters:
    - fun: A function with int or str parameters and int or str return type
    
    Returns:
    - A formatted documentation string
    """
    # Get the function name
    name_of_fun = fun.__name__
    
    # Get function signature
    sig = signature(fun)
    params = sig.parameters
    num_of_params = len(params)
    
    # Get return type
    type_hints = get_type_hints(fun)
    return_type = type_hints.get('return', None)
    
    # Initialize documentation string and args list
    doc_str = "function name\n"
    doc_str += f"    {name_of_fun}\n"
    doc_str += f"params ({num_of_params})\n"
    
    # Initialize args list for example usage
    args = []
    int_count = 0
    str_count = 0
    
    # Process parameters
    for param_name, param in params.items():
        param_type = type_hints.get(param_name, None)
        
        # Add parameter info with proper indentation
        doc_str += f"    {param_name} "
        
        if param_type == int:
            doc_str += "int\n"
            int_count += 1
            # For int parameters, use consecutive values starting from 2
            args.append(int_count + 1)  # Start from 2
        elif param_type == str:
            doc_str += "str\n"
            str_count += 1
            # For str parameters, use consecutive 3-letter strings
            char = chr(ord('a') + str_count - 1)
            args.append(char * 3)  # "aaa", "bbb", etc.
    
    # Add return type info
    doc_str += "return type\n"
    if return_type:
        doc_str += f"    {return_type.__name__}\n"
    else:
        doc_str += "    None\n"
    
    # Add example usage
    doc_str += "example usage\n"
    
    # Format args for display
    formatted_args = []
    for arg in args:
        if isinstance(arg, str):
            formatted_args.append(f"'{arg}'")
        else:
            formatted_args.append(str(arg))
    
    # Format example function call
    example_call = f"{name_of_fun}({', '.join(formatted_args)})"
    doc_str += f"    {example_call}\n"
    
    # Execute the function with the example args to get the return value
    try:
        result = fun(*args)
        if isinstance(result, str):
            result_str = f"'{result}'"
        else:
            result_str = str(result)
        doc_str += f"-> {result}\n"
    except Exception as e:
        # If execution fails, don't include the result
        pass
    
    return doc_str


# Example test case
if __name__ == "__main__":
    def get_person_info(first_name: str, last_name: str, age: int) -> str:
        return f"{first_name} {last_name}, {age}"
    
    # Test the get_doc function
    doc = get_doc(get_person_info)
    print(doc)
    
    # Expected output:
    # function name
    #     get_person_info
    # params (3)
    #     first_name str
    #     last_name str
    #     age int
    # return type
    #     str
    # example usage
    #     get_person_info('aaa', 'bbb', 2)
    # -> aaa bbb, 2
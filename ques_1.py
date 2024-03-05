""" 1. Write a decorator to log the following details whenever a function is called
# 	a. The File needs to be name of the <module>_<YYYYMMDD>.log
# 	b. The messages in the logs file should follow the format as below
# 		<module name> <function name> <DD-MM-YY> <hh:mm:ss> <Dict of Arguments passed to the function>
"""

import datetime

def log_decorator(func):
    """function that logs the details"""

    def wrapper(*args, **kwargs):
        """wrapper function for logging"""
        date = datetime.datetime.now()
        module_name = func.__module__
        function_name = func.__name__
        formatted_date = date.strftime("%d-%m-%y")
        time = date.strftime("%H:%M:%S")

        #Extract arguments passed to the function
        args_dict = {}
        if args:
            args_dict['args'] = args
        if kwargs:
            args_dict['kwargs'] = kwargs

        # Log details to file
        log_file_name = f"{module_name}_{date.strftime('%Y%m%d')}.log"
        log_file_message = f"{module_name} {function_name} {formatted_date} {time} {args_dict}"

        with open(log_file_name, 'a', encoding="utf-8") as log_file:
            log_file.write(log_file_message + "\n")

            # Call the original function
            return func( *args, **kwargs)

    return wrapper

@log_decorator
def add(x,y):
    """add two numbers"""
    print(x+y)

add(5,3)

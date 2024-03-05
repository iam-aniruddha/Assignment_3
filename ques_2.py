"""#2 Write a decorator to log the execution time for a function. """

import datetime
import time

def execution_time_decorator(func):
    """This decorator calculates the execution time of a function. """

    def wrapper(*args, **kwargs):
        """This is the wrapper function. It prints out how long a function takes to run."""
        # Record start time
        start_time = time.time()

        # Call the original function
        result = func(*args, **kwargs)

        # Record end time
        end_time = time.time()

        # Calculate execution time
        execution_time = end_time - start_time

        # Get current date and time
        date = datetime.datetime.now()
        formatted_date = date.strftime("%d-%m-%y %H:%M:%S")

        # Extract module name and function name
        module_name = func.__module__
        function_name = func.__name__

        # Log execution time to file
        log_file_name = f"{module_name}_{date.strftime('%Y%m%d')}.log"
        log_message = f"{module_name} {function_name} {formatted_date}\
          Execution Time: {execution_time:.4f} seconds\n"

        with open(log_file_name, 'a', encoding= "utf-8") as log_file:
            log_file.write(log_message)

        return result

    return wrapper

# Example usage
@execution_time_decorator
def add(x, y):
    """A simple function that adds two numbers together."""
    time.sleep(2)  # Simulating a long-running process
    return x + y

add(3, 5)

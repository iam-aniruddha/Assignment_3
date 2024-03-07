"""# 3. Write a decorator to validate arguments passed to a function based on a condition.
# e.g. Write a WAF to generate sequence of squares of all even numbers in the range of 1 to 10
# Check if the number passed as a argument is in the specified range using decorators.
 If the condition fails the function 
# should return an exception "ValueError" with an appropriate message."""

def validate_range(min_val, max_val):
    """
    Decorator that checks if the argument values are within the specified range.
    If not it raises ValueError with an appropriate message.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            """
            Checks each arg against the min/max vals; if any fail raise ValueError.
            """
            for arg in args:
                if arg < min_val or arg > max_val:
                    raise ValueError(f"Argument {arg} is not within the range [{min_val}, {max_val}]") # pylint: disable= line-too-long

            for kwarg in kwargs.values():
                if kwarg < min_val or kwarg > max_val:
                    raise ValueError(f"Argument {kwarg} is not within the range [{min_val}, {max_val}]") # pylint: disable= line-too-long

            # Call the original function
            return func(*args, **kwargs)

        return wrapper
    return decorator

# Example usage
@validate_range(1, 10)
def generate_sequence(start, end):
    """Generate the sequence of squares of all even numbers in the given range."""
    sequence = [i**2 for i in range(start, end+1) if i % 2 == 0]
    return sequence

try:
    result = generate_sequence(1, 10)
except ValueError as e:
    print(e)
else:
    print(result)

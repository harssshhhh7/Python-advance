def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} executed successfully.")
        return result
    return wrapper

@log_function_call
def add_numbs(a, b):
    return a + b
result = add_numbs(2, 3)
print(result)
def print_hello_world(description):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Hello {description.format(*args)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@print_hello_world("{}")
def function_one(string):
    pass


function_one("World !!")

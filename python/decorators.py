
def check_role_permissions(func):
    def decorator_function(*args, **kwargs):
        print("I am called......")
        return func(*args, **kwargs)
    return decorator_function

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def outerfunc(func):
    def innerfunc():
        print("inner func")
        return 0
    return innerfunc
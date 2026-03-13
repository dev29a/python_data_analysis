import functools

def jsonify_decorator(func):
    functools.wraps(func)
    def modifyOutput(*args, **kwargs):
        return {"output": func(*args, **kwargs)}
    return modifyOutput

@jsonify_decorator
def hello():
    return 'hello world'

@jsonify_decorator
def add(a, b):
    return int(a + b)    

print(hello()) 
print(add(3, 9))           
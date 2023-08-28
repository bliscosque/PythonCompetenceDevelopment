# Funcao decoradora... 
def decorate_func(func):
    def intern(*args, **kwargs):
        for arg in args: # validate args
            is_str(arg)
        res=func(*args,**kwargs)
        return res
    return intern

def is_str(param):
    if not isinstance(param,str):
        raise TypeError('param must be a str')

# decorating...
@decorate_func
def inv_str(s):
    return s[::-1]

rev=inv_str('123')
print(rev)
rev=inv_str(123) # TypeError
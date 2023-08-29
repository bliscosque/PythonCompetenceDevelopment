def decoratos_factory(a=None, b=None, c=None):
    def function_factory(func):
        def nested(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return nested
    return function_factory


@decoratos_factory(1, 2, 3)
def soma(x, y):
    return x + y


decorator = decoratos_factory()
multiply = decorator(lambda x, y: x * y)

s_ans = soma(10, 5)
m_ans = multiply(10, 5)
print(s_ans)
print(m_ans)
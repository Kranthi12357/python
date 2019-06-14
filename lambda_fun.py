x = lambda a: a+5
print(x(5))
y = lambda a,b:a*b
print(y(1,2))

def func():
    return lambda a:print(a)
fun=func()
fun(4)

def funct(p):
   print(p(5))

funct(lambda a:a+10)
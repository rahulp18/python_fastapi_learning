# FUNCTION AS ARGUMENT

def add(x,y):
    return x+y
def multiply(x,y):
    return x*y

def execute(fn,x,y):
    return fn(x,y)

print(execute(add,3,4))

# USE MAP TO SQUARE NUMBER

nums=[1,2,3,4,5]
result=list(map(lambda x:x*x,nums))

print(result)
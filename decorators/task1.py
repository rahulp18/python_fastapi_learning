# def decorator(func):
#     def wrapper(*args):
#         func(*args)
     
#     return wrapper

# @decorator
# def greet():
#     print("Hello Rahul")

# greet()

# AUTH DECORATOR

def auth(func):
    def wrapper(*args,**kwargs):
       if args:
        token=args[0]
        print(f"Auth Trace token is {token}")
          
       result= func(*args,**kwargs)
       return result
    return wrapper

@auth
def get_users(token):
    print("Welcome Rahul and Binita",token)
 
get_users()
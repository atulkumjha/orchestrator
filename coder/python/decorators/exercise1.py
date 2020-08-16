'''
# Write Decorators and apply to source-code
A Decorator is also a python function that takes a function and its arguments as input,
executes it and returns the final result.

The Decorators can also be written as a class and be applied to other functions/methods.

Basically decorators come in 2 types,

    1. Decorator with Arguments
    2. Decorator without Arguments

    Example of decorator without arguments
    **************************************

    @decorator # This decorator is not having arguments.
    def funcA(x,y):
        return True

    Example of decorator with arguments
    ************************************

    @decorator("hello",10,20) # This decorator is having arguments as "hello",10,20
    def funcA(x,y):
        return True

Sample decorator that is not having any arguments will be looking as below;
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def decorator_function(function):
    # param function denotes the function to be decorated

    def execute_function(*args,**kwargs):
        # param *args,**kwargs denotes the arguments of the function to be decorated

        # command function(*args,**kwargs) -> will execute the function to be decorated with all of its argument
        result = function(*args,**kwargs)

        # Return the result of the function after execution
        return result 

    # Return this function so that the outer function will call and execute it
    return decorator_function 

Sample decorator that is having any arguments will be looking as below;
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def decorator_function_arguments(*deco_args,**deco_kwargs):
    """
    *** NOTE :: Please be informed that *** 
    # param *deco_args,**deco_kwargs denotes the arguments of the decorator function 
    and not the function to be decorated.
    """
    
    def decorator_function(function):
        # param function denotes the function to be decorated
        
        def execute_function(*args,**kwargs):
            # param *args,**kwargs denotes the arguments of the function to be decorated

            # command function(*args,**kwargs) -> will execute the function to be decorated with all of its argument
            result = function(*args,**kwargs)

            # Return the result of the function after execution
            return result 

        # Return this function so that the outer function will call and execute it
        return execute_function 

    # Return this function so that the outer function will call and execute it
    return decorator_function 

'''

# Type 1 : Decorator without arguments. This will take function and it's args as input, execute and return output

def decorator_exec(function): # Wrapped Function
    def function_args(*args,**kwargs): # Args of the wrapped function
        
        if hasattr(function,"__name__"):
            print("Function name {} ".format(function.__name__))
        print("Args of the function are {} and {} ".format(args,kwargs))
        
        # Before executing function - you can do any pre-steps
        try:        
            # Execute the function
            #It's executed as self.function(*args,**kwargs)
            #It means the function will get executed with all of its arguments.
            result = function(*args,**kwargs)
            # After executing function - you can do any post-steps
            # Prepare final result
            return result
            print("Result of function {} is {} ".format(function.__name__,result))
        except Exception as error:
            raise error
    return function_args

'''
# Type 2 : Decorator with arguments. 
This will take function and it's args as input, it will also take arguments to the decorator
Then execute and return output
'''
def decorator_exec_with_args(*deco_args,**deco_kwargs): # Args of decorator
    def decorator_wrapped_func(function): # Wrapped Function
        def function_args(*func_args,**func_kwargs): # Args of the wrapped function

            print("Args of the decorator are {} and {} ".format(deco_args,deco_kwargs))

            if hasattr(function,"__name__"):
                print("Function name {} ".format(function.__name__))
            print("Args of the function are {} and {} ".format(func_args,func_kwargs))
    
            # Before executing function - you can do any pre-steps
            # Execute the function
            #It's executed as self.function(*func_args,**func_kwargs)
            #It means the function will get executed with all of its arguments.

            result = function(*func_args,**func_kwargs)
            # After executing function - you can do any post-steps
            # Prepare final result
            return result

        return function_args
    return decorator_wrapped_func

'''
    Test the above decorators with examples. Apply decorator and get results.
'''

# Test Type 1 decorator
@decorator_exec # This decorator is not having arguments
def test_decorator_exec(x,y,*args,**kwargs):
    maparray = []
    for i in args:
        maparray.append(i)
    maparray.extend([x,y])
    return maparray

# Test Type 2 decorator
@decorator_exec_with_args(5000,70000,range(-1,-10),mapper_range=range(1000,2000)) # This decorator is having arguments
def test_decorator_exec_with_args(x,y,*args,**kwargs):
    maparray = []
    for i in args:
        maparray.append(i)
    maparray.extend([x,y])
    return maparray

if __name__ == "__main__":
    test_decorator_exec_with_args(100,200,10,20,30,40,50,60,70,80,90,300,name='Arun',profession='Programmer')

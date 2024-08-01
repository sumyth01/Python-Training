


# Variables have a scope, which is the region of the program where the variable is accessible.

# Local Scope: Variables defined inside a function.
# Global Scope: Variables defined outside any function.



x = 10 

def func():
    #Local variable
    y = 5
    print("Inside function, x:", x)
    print("Inside function, y:", y)

    func()
    print("outside function, x:", x) 

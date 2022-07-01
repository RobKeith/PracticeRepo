# learning how to create a function
# learning docstrings
# learning how to interact with a list
# learning for loops basics
# learning an if statement
# learning how to chdck a variable type

def CustomFuncOne(a,b):
    """
    This function creates a list.
    """
    MyList = [a,b]
    for item in MyList:
        if item == 5:
            print("great")
        else:
            print(type(item))




CustomFuncOne(5,"wow")

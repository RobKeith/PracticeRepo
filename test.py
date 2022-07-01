# print("Hello World")
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

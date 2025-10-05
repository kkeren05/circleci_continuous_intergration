def my_add(a,b):
        return a + b
def my_add (a,b):
        if not isinstance(a, (int,float)) or not isinstance(b, (int,float)):
                raise TypeError ("Both inputs must be int or float.")
        return a + b
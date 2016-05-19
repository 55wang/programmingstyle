#functional programming, functions can be reused by another function
#because they are stateless

#anyone can reuse/reconstruct a new function with reduce and addit function block
#By switching AddIt with MultIt within the same reduce function, it can produce
#a new usage/function
#modular design,

MyList = [1, 2, 3, 4, 5]
def AddIt(X, Y):
    return (X + Y)

def MultIt(X, Y):
    return (X*Y)

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value

Sum = reduce(AddIt, MyList)
print(Sum)

Sum = reduce(MultIt, MyList)
print(Sum)

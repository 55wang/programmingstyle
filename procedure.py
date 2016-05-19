#procedure lies inbetween imperative and functional
#it is an improved version of imperative as it now can reuse this portion of code.
#however, the instruction, in this case ADD, cannot be changed, as it is fixed
# in this DoAdd function
def DoAdd(MyList):
    Sum = 0
    if type(MyList) is list:
        for X in MyList:
            Sum += X
    return Sum
MyList = [1, 2, 3, 4, 5]

print(DoAdd(MyList))
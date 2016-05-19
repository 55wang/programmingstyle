#the sum result is now assigned to the CreateSum obj.
#oop is more organised as the result and function belongs to the object

#good for defining entities when the program need to have a lot of entities
#with common attributes and functions.

class ChangeList:
    def __init__(self, MyList):
        if type(MyList) is list:
            self.MyList = MyList
        else:
            self.MyList =[]
    def DoAdd(self):
        self.Sum = sum(self.MyList)

CreateSum = ChangeList([1, 2, 3, 4, 5])
CreateSum.DoAdd()
print(CreateSum.Sum)
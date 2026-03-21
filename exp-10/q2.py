class addition:
    def add(self,a,b):
        return a+b
class substraction:
    def sub(self,a,b):
        return a-b
class multiplication:
    def mul(self,a,b):
        return a*b 
class division:
    def div(self,a,b):
        if b!=0:
          return a/b
        else:
          print("divide by zero is not possible")
          
class calculator(addition,substraction,multiplication,division):
    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2
data1=int(input("enter the 1st no:"))
data2=int(input("enter the 2nd no:"))
calc=calculator(data1,data2)
print("the sum is",calc.add(calc.data1,calc.data2))
print("the sub is",calc.sub(calc.data1,calc.data2))
print("the product is",calc.mul(calc.data1,calc.data2))
print("the division is",calc.div(calc.data1,calc.data2))                               
# create class
class Calulator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mult(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return 'cannot be divide by zero'
        return a/b
 
# user input    
a= int(input())
b= int(input())

# instance class
calculator = Calulator()

# test the calculator method
print('Addition: ',calculator.add(a,b))
print('Subtraction: ',calculator.sub(a,b))
print('Multiplicatin: ',calculator.mult(a,b))
print('Division: ',calculator.div(a,b))
print('Division by zero: ',calculator.div(a,0))

class calculator():
    def __init__(self ,x ,y):
        self.x = x 
        self.y = x 
  
    def add(self): 
        return self.x+ self.y 
    def subtract(self): 
        return self.x - self.y 
    def divide(self): 
        return self.x/self.y        
    def multiply(self): 
        return self.x * self.y 

x=int(input("Enter first number: "))
y=int(input("Enter second number"))

point=calculator(x,y)
print("Add : " , point.add())
print("Subtract: " , point.subtract())
print("Divide : " , point.divide())
print("Multiply : " , point.multiply()) 

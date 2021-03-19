class Rectangle():
    def __init__(self ,x ,y):
        self.x = x 
        self.y = x 
    def area(self): 
        return self.x*self.y
    def perimeter(self):
        return 2*(self.x+self.y)

print("უნდა ბეჭდავდეს მართკუთხედის სიგრძეს, სიგანეს, ფართობს და პერიმეტრს თვალისთვის ადვილად აღსაქმელ ფორმატში")

x=int(input("Enter width: "))
y=int(input("Enter Length: "))    


point=Rectangle(x,y)
print("Area: " ,  point.area())
print("Perimeter: " ,  point.perimeter())
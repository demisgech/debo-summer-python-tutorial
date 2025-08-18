
#Class => Blueprint
class Point:
    x = 0
    y = 0
    
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Drawing a point at {self.x,self.y}")
    
#Object => Instance
# point1 = Point(1,2)

# # print(point1.x)
# point1.draw()

# point2 = Point(3,4)
# # print(point2.x)
# point2.draw()


class Rectangle:
    def __init__(self,width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height
        
    
rectangle = Rectangle(4,3)
print(rectangle.get_area())

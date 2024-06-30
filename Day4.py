class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
def print_area(shape):
    print("Area:", shape.area())

rectangle = Rectangle(5, 2)
circle = Circle(4)

print_area(rectangle)
print_area(circle)


class animal:
    def speak(self):
        pass

class dog(animal):
    def speak(self):
        return "woof !"

class cat(animal):
    def speak(self):
        return "meoow !"

def make_sound(animal):
    print(animal.speak())

animals = [dog(),cat()]
for animal in animals:
    make_sound(animal)



class employee:
    def __init__(self,name):
        self.name = name

    def calculate_salary(self):
        pass

class fulltimeemployee(employee):
    def calculate_salary(self):
        return 50000
    
class parttimeemployee(employee):
    def calculate_salary(self):
        return 25000
    
employees = [fulltimeemployee('gu'),parttimeemployee('gukha')]
for employee in employees:
    print(f"{employee.name}'s salary: ", employee.calculate_salary())
    
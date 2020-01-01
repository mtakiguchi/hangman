class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    
    recs = []

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.recs.append((self.width, self.height))

    def calculate_perimeter(self):
        return (self.width + self.height) * 2

    def what_am_i(self):
        print("I am a rectangle")

class Square(Shape):
    
    square_list = []

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.square_list.append(self)

    # def __repr__(self):
    #     return "Square {} by {} by {} by {}".format(self.width,self.height,self.width,self.height)
    
    def calculate_perimeter(self):
        return (self.width + self.height) * 2

    def change_size(self, add):
        self.width += add
        self.height += add

rect = Rectangle(2,5)
print(rect.calculate_perimeter())
rect.what_am_i()
print(rect)
rect2 = Rectangle(10,4)
print(rect2)

sq = Square(3,3)
print(sq.calculate_perimeter())
print(sq)
sq.change_size(2)
print(sq.calculate_perimeter())
sq.what_am_i()
sq2 = Square(5,5)
print(sq2)
print(Square.square_list)

print(Rectangle.recs)

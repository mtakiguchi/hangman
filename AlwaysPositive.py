class AlwaysPositive:
    def __init__(self, number):
        self.n = number
    
    def __add__(self, other):
        return abs(self.n + other.n)

class AlwaysNegative:
    def __init__(self, number):
        self.n = number
    
    def __add__(self, other):
        return (-1) * abs(self.n + other.n)

x = AlwaysPositive(-200)
y = AlwaysNegative(10)

print(x + y)
print(y + x)
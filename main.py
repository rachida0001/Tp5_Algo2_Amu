import cmath
import math

class Point:
    def __init__(self, x, y=None):
        if y is None:
            self.x = x.x
            self.y = x.y
        else:
            self.x = x
            self.y = y
            
    def __getitem__(self, i):
        if i==0:
            return self.x
        elif i==1:
            return self.y
        else:
            return IndexError("Index must be 0 or 1")
    
    def __repr__(self):
        return f"({self.x},{self.y})"   
    
    def __eq__(self, point):
        return (self.x == point.x and self.y == point.y)
    
    def angle(self, p):
        delta_x = self.x - p.x
        delta_y = self.y - p.y
        return cmath.phase(complex(delta_x, delta_y)) *(180/3.14)
    
    def distance_point(self, p):
        return (math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2))
    
    def det(self,A,B):
        return ((A.x - self.x) * (B.y - self.y) - ((B.x - self.x) * (A.y - self.y)))
        
        
    
if __name__ == "__main__":
    p = Point(1,2)
    print(p.y)
    a = Point(p)
    print(a.y)
    print(p[0])
    print(p)
    print(p==a)
    c = Point(3,4)
    print(p.angle(c))
    print(p.distance_point(a))
    print(p.distance_point(c))
    A = Point(1,1)
    B = Point(2,2)
    d = Point(6,0)
    print(c.det(A,B))
    print(d.det(A,B))
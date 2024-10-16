from main import Point

class Points:
    def __init__(self, l):
        self.l = l.copy()
        
l = [Point(0,1), Point(1,0), Point(1,1)]
lp = Points(l)
l[0] = 0
print(lp.l)
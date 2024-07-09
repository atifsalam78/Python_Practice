"""
A user can create and view 2D coordinates
A user can find out the distance between 2 coordinates
A user can find the distance of a coordinate from origin
A user can check if a point lies on a given line
A user can find the distance between a given 2D point and a given line

"""


class Point:

    def __init__(self,x,y):
        self.x_cord = x
        self.y_cord = y

    def __str__(self):
        """create and view 2D coordinates"""
        return "<{},{}>".format(self.x_cord, self.y_cord)

    def EuclideanDistance(self,other):
        """distance between 2 coordinates"""
        return ((other.x_cord - self.x_cord)**2 + (other.y_cord - self.y_cord)**2)**0.5

    def distnaceFromOrigin(self):
        """distance of a coordinate from origin"""
        # return (self.x_cord**2 + self.y_cord**2)**0.5
        return self.EuclideanDistance(Point(0,0)) # We can create class object inside the class as well

class Line:
    
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        if self.A > 0 and self.B > 0 and self.C > 0:
            return "{}x + {}y + {} = 0".format(self.A,self.B,self.C)
        
        elif self.A < 0 and self.B < 0 and self.C < 0:
            return "{}x {}y {} = 0".format(self.A,self.B,self.C)
    
        elif self.A < 0 and self.B > 0 and self.C > 0:
            return "{}x + {}y + {} = 0".format(self.A,self.B,self.C)
        
        elif self.A > 0 and self.B < 0 and self.C > 0:
            return "{}x {}y + {} = 0".format(self.A,self.B,self.C)
        
        elif self.A > 0 and self.B > 0 and self.C < 0:
            return "{}x + {}y {} = 0".format(self.A,self.B,self.C)

    def point_on_line(line, point):
        """check if a point lies on a given line"""
        if line.A*point.x_cord + line.B*point.y_cord + line.C == 0:
            return "Points lies on the line"    
        else:
            return "Points not lies on the line"
        
    def shortest_distance(line,point):
        """the distance between a given 2D point and a given line"""        
        return abs(line.A*point.x_cord + line.B*point.y_cord + line.C) / (line.A**2 + line.B**2)**0.5

# p1 = Point(2,2)
# p2 = Point(1,1)
# print(p1.EuclideanDistance(p2))
# print(p1.distnaceFromOrigin())

# l1 = Line(3,3,3)
# print(l1)
# l1 = Line(1,1,-2)
# p1 = Point(1,1)
# print(l1)
# print(p1)
# print(l1.point_on_line(p1))

l1 = Line(1,1,-2)
p1 = Point(1,10)

print(l1.shortest_distance(p1))
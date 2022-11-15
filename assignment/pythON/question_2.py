class validity_check:
    def __init__(self, triangle, rectangle):
        self.triangle= triangle
        self.rectangle= rectangle
        
    def triangle_check(self):
        x=self.triangle[0]
        y=self.triangle[1]
        z=self.triangle[2]
        if len(self.triangle)==3:
            if x+y>z and y+z>x and z+x>y:
                return "Valid Triangle"
            else:
                return "Invalid Triangle"
    def rectangle_check(self):
        if self.rectangle[0]==self.rectangle[2] or self.rectangle[1]==self.rectangle[3]:
            return "Valid Rectangle"
        else:
            return "Invalid Rectangle"
        
triangle_sides= input().split(" ")
rectangle_sides=input().split(" ")
validity= validity_check(triangle_sides, rectangle_sides)
print(validity.triangle_check())
print(validity.rectangle_check())
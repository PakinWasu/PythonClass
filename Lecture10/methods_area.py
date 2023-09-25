class calculate_area:

    def rectangle_area(self,w,h):
        return w*h
    
    @classmethod
    def triangle_area(cls,b,h):
        return 0.5*b*h
    
    @staticmethod
    def cricle_area(r):
        return 3.14*r*r
    
cal = calculate_area()
cal_rec = cal.rectangle_area(4,5)
cal_tri = cal.triangle_area(4,5)
cal_circle = cal.cricle_area(5)

print('Rectangle Area = ',cal_rec)
print('Triangle Area = ',cal_tri)
print('Circle Area = ',cal_circle)

# print('Rectangle Area = ',calculate_area.rectangle_area(5,6))
print('Triangle Area = ',calculate_area.triangle_area(5,6))
print('Circle Area = ',calculate_area.cricle_area(5))
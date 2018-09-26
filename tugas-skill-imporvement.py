def area_triangle(a,b): #to define area_triangle, a ,and b
    return a * b /2 #to make the formula to count the area and return it to the top
a = "base"
b = "height"
print (area_triangle(5,12)) #to print the area of the triangle which has base(5) and height(12)
                            #so we count the area = 5 * 12 /2 = 30, then output = 30.0
def perimeter_triangle(a,b,c): #to define perimeter triangle, a, b, and c
    return a + b + c    # to make the formula to count the perimeter of triangle and return it
a = "base"
b = "height"
c = "slide"
print (perimeter_triangle(5,12,13)) #to print the perimeter which has base(5), height (12), and slide(13)
                                    #since the formula is a +b +c, so we count 5 + 12 + 13 = 30, then output : 30
for i in range (0,13): #to make the visual triangle
    print ("@" * i)
print ("\n")
def area_square(a,b) :#to define area square, a, and b
    return a * b #to make the formula to county the area of square and return it
a = "side1"
b = "side2"
print (area_square(5,5)) #to print the area of square which has sidea(5) and sideb(5)
                        #since the formula is a * b, so we  count 5 * 5 = 25, then output : 25
def perimeter_square(a,b) : #to define the perimeter square , a , and b
    return (a + b) * 2 #to make the formula to count the perimeter square and return it
a = "side1"
b = "side2"
print (perimeter_square(5,5)) #to print the perimeter square which has sidea(5) and sideb(5)
                            #since the formula is (a+b) *2, so we count (5+5)*2 = 20, then output : 20
for i in range(0,6):
    print ( "@" * 12)

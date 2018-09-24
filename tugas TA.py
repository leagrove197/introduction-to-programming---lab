height = input("insert height here:") # in here we can type the height for the triangle, since the TA told us to input the height into 5, then we must type 5 here
height = int(height)
#No.1
for i in range(1,(height + 1)): #since the height is 5, then the range is from 1 to 6, so you will get 5 "*"
    print("*" * i) #the program will print 1 "*" in the first line, then print 2 "*" in the second line and 5 "*" in the last line because the range is 1 until 5
#No.2
for i in range(1,(height +1)):
    print (" " * (height - i) + "*" * i)
#No.3
for i in range(1,(height +1)):
    print ("*" * (height - i + 1) + " " * i )
#No.4
for i in range(1,(height + 1)):
    print(" " * i + "*" * (height - i + 1))
#No.5
a = 1
for i in range(1,(height + 1)):
    print(" " * (height - i)+ "*" * a) #this triangle is like a pyramid
    a += 2
#No.6    
a = 1
for i in range(1,(height + 1)):
    print(" " * (height - i)+ "*" * a) #for the diamond, we need to make 2 triangle, first 1 is pyramid and the below one is upside down pyramid but start with less "*" than the top one
    a += 2


b = height - 3
for i in range(1,(height + 1)):
    print(" " * (i ) + "*" * (height + b))
    b -= 2

height = input("insert height here:") #since the TA told us to input the height into 5, then we must type 5 here
height = int(height)
#No.1
for i in range(1,(height + 1)):
    print("*" * i)
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
    print(" " * (height - i)+ "*" * a)
    a += 2
#No.6    
a = 1
for i in range(1,(height + 1)):
    print(" " * (height - i)+ "*" * a)
    a += 2


b = height - 3
for i in range(1,(height + 1)):
    print(" " * (i ) + "*" * (height + b))
    b -= 2

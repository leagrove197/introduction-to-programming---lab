height = input("insert height here:")
height = int(height)
for i in range(1,(height + 1)):
    print("*" * i)

for i in range(1,(height +1)):
    print (" " * (height - i) + "*" * i)

for i in range(1,(height +1)):
    print ("*" * (height - i + 1) + " " * i )




for i in range(1,(height + 1)):
    print(" " * i + "*" * (height - i + 1))

a = 1
for i in range(1,(height + 1)):
    print(" " * (height - i)+ "*" * a)
    a += 2
a = 1
for i in range(1,(height + 1)):
    print(" " * (height - i)+ "*" * a)
    a += 2


b = height - 3
for i in range(1,(height + 1)):
    print(" " * (i ) + "*" * (height + b))
    b -= 2

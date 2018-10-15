print("WELCOME TO L's HOTEL ***** (5stars)\n        How May I Help You?")

class Hotel():
    def __init__(self,type):    #define all variables you wanna use later
        self.room1price = 100
        self.room2price = 100
        self.room3price = 100
        self.room4price = 100
        self.room5price = 100
        self.room6price = 1000
        self.room7price = 1000
        self.room8price = 1000
        self.room1list = []
        self.room2list = []
        self.room3list = []
        self.room4list = []
        self.room5list = []
        self.room6list = []
        self.room7list = []
        self.room8list = []
        self.type = type
    def check_room1(self):
        roomnum1 = int(len(self.room1list))     #variable roomnum1  = total of room1list
        if roomnum1 > 0:                            #if the total of room1list is bigger than 0
            print ("this room is occupied")             #then print those words
        elif roomnum1 == 0:                         #if the totallist of room1list is 0, which is mean the room is empty, no one has ever checked in to that room
            print ("this room is empty")            #print that
    def check_room2(self):
        roomnum2 = int(len(self.room2list))
        if roomnum2 > 0:
            print ("this room is occupied")
        elif roomnum2 == 0:
            print ("this room is empty")
    def check_room3(self):
        roomnum3 = int(len(self.room3list))
        if roomnum3 > 0:
            print ("this room is occupied")
        elif roomnum3 == 0:
            print ("this room is empty")
    def check_room4(self):
        roomnum4 = int(len(self.room4list))
        if roomnum4 > 0:
            print ("this room is occupied")
        elif roomnum4== 0:
            print ("this room is empty")
    def check_room5(self):
        roomnum5 = int(len(self.room5list))
        if roomnum5 > 0:
            print ("this room is occupied")
        elif roomnum5 == 0:
            print ("this room is empty")
    def check_room6(self):
        roomnum6 = int(len(self.room6list))
        if roomnum6 > 0:
            print ("this room is occupied")
        elif roomnum6 == 0:
            print ("this room is empty")
    def check_room7(self):
        roomnum7 = int(len(self.room7list))
        if roomnum7 > 0:
            print ("this room is occupied")
        elif roomnum7 == 0:
            print ("this room is empty")
    def check_room8(self):
        roomnum8 = int(len(self.room8list))
        if roomnum8 > 0:
            print ("this room is occupied")
        elif roomnum8 == 0:
            print ("this room is empty")

    def revenue(self):
        room1 = int(len(self.room1list))        #to check to total list of the room
        room2 = int(len(self.room2list))
        room3 = int(len(self.room3list))        #you put the total len list in room1,room2..room8 so you can calculate it later easily
        room4 = int(len(self.room4list))
        room5 = int(len(self.room5list))
        room6 = int(len(self.room6list))
        room7 = int(len(self.room7list))
        room8 = int(len(self.room8list))
        revenue =  room1 * self.room1price + room2 * self.room2price + room3 * self.room3price + room4 * self.room4price + room5 * self.room5price + room6 * self.room6price + room7 * self.room7price + room8 * self.room8price
        print ("Total Revenue : $", revenue, "\n")  #then you calculate the total of the list * price, and +  it with other room price, so you get the total revenue
class Room(Hotel):
    def room1(self):
        self.room1list.append(self.type)            #this is how to get the list of the room1
        print("\nPrice : $", self.room1price, "\n") #after you append the list, you print the price that you have defined on top
    def room2(self):
        self.room2list.append(self.type)
        print("\nPrice : $", self.room2price, "\n")
    def room3(self):
        self.room3list.append(self.type)
        print("\nPrice : $", self.room3price, "\n")
    def room4(self):
        self.room4list.append(self.type)
        print("\nPrice : $", self.room4price, "\n")
    def room5(self):
        self.room5list.append(self.type)
        print("\nPrice : $", self.room5price, "\n")
    def room6(self):
        self.room6list.append(self.type)
        print("\nPrice : $", self.room6price, "\n")
    def room7(self):
        self.room7list.append(self.type)
        print("\nPrice : $", self.room7price, "\n")
    def room8(self):
        self.room8list.append(self.type)
        print("\nPrice : $", self.room8price, "\n")

    def outroom1(self):
        int(len(self.room1list)) - 1    #you minus the list by 1, so when ppl check out, the list will be zero, so the room wil be empty
        print ("GOOD BYE")
    def outroom2(self):
        int(len(self.room2list)) - 1
        print ("GOOD BYE")
    def outroom3(self):
        int(len(self.room3list)) - 1
        print ("GOOD BYE")
    def outroom4(self):
        int(len(self.room4list)) - 1
        print ("GOOD BYE")
    def outroom5(self):
        int(len(self.room5list)) - 1
        print ("GOOD BYE")
    def outroom6(self):
        int(len(self.room6list)) - 1
        print ("GOOD BYE")
    def outroom7(self):
        int(len(self.room7list)) - 1
        print ("GOOD BYE")
    def outroom8(self):
        int(len(self.room8list)) - 1
        print ("GOOD BYE")





h = Room("room")        #call the class Room


inhotel = True  #make variable true
while inhotel:  #and loop
    print("1.check in\n2.check out\n3.check room\n4.Revenue\n5.Category of Rooms\n6.DONE WITH THIS")
    choice = int(input("mau ngapain ha?"))  #this is where you choose what u gonna do
    if choice == 1:
        print ("choose room:room1(a)\n\t\t\troom2(b)\n\t\t\troom3(c)\n\t\t\troom4(d)\n\t\t\troom5(e)\n\t\t\troom6(f)\n\t\t\troom7(g)\n\t\t\troom8(h)")
        choice = input("choose room :a/b/c/d/e/f/g/h : ")
        if choice == "a":       #if you want to check in, all the room will show up and u get to choose 1
            h.room1()
        if choice == "b":
            h.room2()
        if choice == "c":
            h.room3()
        if choice == "d":
            h.room4()
        if choice == "e":
            h.room5()
        if choice == "f":
            h.room6()
        if choice == "g":
            h.room7()
        if choice == "h":
            h.room8()       #call the def of the room you wanna choose
    if choice == 2:
        print ("choose room:room1(a)\n\t\t\troom2(b)\n\t\t\troom3(c)\n\t\t\troom4(d)\n\t\t\troom5(e)\n\t\t\troom6(f)\n\t\t\troom7(g)\n\t\t\troom8(h)")
        choose = input("from what room :")  #you must tell from what room are you, to inform that your room list will be minus by 1 so it will be empty after you check out
        if choose == "a":
            h.outroom1()
        if choose == "b":
            h.outroom2()
        if choose == "c":
            h.outroom3()
        if choose == "d":
            h.outroom4()
        if choose == "e":
            h.outroom5()
        if choose == "f":
            h.outroom6()
        if choose == "g":
            h.outroom7()
        if choose == "h":
            h.outroom8()





    if choice == 3:
        print ("choose room:room1(a)\n\t\t\troom2(b)\n\t\t\troom3(c)\n\t\t\troom4(d)\n\t\t\troom5(e)\n\t\t\troom6(f)\n\t\t\troom7(g)\n\t\t\troom8(h)")
        choice = input("choose room :a/b/c/d/e/f/g/h : ")
        if choice == "a":       #you can choose which room you wanna check, and it will tell you whether the room is occupied or not
            h.check_room1()
        if choice == "b":
            h.check_room2()
        if choice == "c":
            h.check_room3()
        if choice == "d":
            h.check_room4()
        if choice == "e":
            h.check_room5()
        if choice == "f":
            h.check_room6()
        if choice == "g":
            h.check_room7()
        if choice == "h":
            h.check_room8()
    if choice == 4:
        h.revenue() #this will show you the total revenue the hotel get
    if choice == 5:
        print ("\n\nroom 1 - 5 : Lowbudget\nroom 6 - 8 : Sultan\n\n")   #to inform you the Category of Rooms
    if choice == 6:
        print ("dadahhh")
        inhotel = False #break the loop














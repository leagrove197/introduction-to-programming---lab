print ("================================================================================" 
       "\n\t\t\t\t\t\t\tToll Payment Systems" 
       "\n\t\t\t\t\t\t\tPT Jasa Marga, Tbk."
      "\n================================================================================") #print the Toll Payment Systems PT Jasa Marga,Tbk. in exact same output as the assignment example


class Tol():   #create class tol
    def __init__(self,type):    #define init the type
        self.priceCar = 6000    #make self price for car which is 6000 Rupiahs
        self.priceBus = 8000    #make self price for bus which is 8000 Rupiahs
        self.priceTruck = 10000 #make self price for truck which is 10000 Rupiah
        self.type = type        #to make the self type which we put it in the init

class Transportation(Tol): #create the Transportation class and inherit the tol clas inside the Transportation class

    def car_in(self):  #define car_in
        print("\nFee :",self.priceCar,"\n") #it will show you the price everytime you choose to get the car in

    def bus_in(self):  #define bus_in
        print("\nFee :",self.priceBus,"\n")#it will show you the price everytime you choose to get the bus in

    def truck_in(self):#define truck_in
        print("\nFee :",self.priceTruck,"\n")#it will show you the price everytime you choose to get the Truck in

a = Transportation("Transportation")    #call the class Transportation

while True :    #make a while true loop to loop the program

        print("Category of Transportation:")
        print("1. \tCar\t\t(RP. 6000)")
        print("2. \tBus\t\t(RP. 8000)")
        print("3. \tTruck\t(RP. 9000)")
        print("4. \tStop Program")              #print all of this for you to choose
        choice=int(input("Enter choice: ")) #choose here, and your choice will be convert into integer
        if choice == 1:     #if your choice is 1
            a.car_in()     #the program will summon car_in def
        if choice == 2:     #if your choice is 2
            a.bus_in()      #the program will summon bus_in def
        if choice == 3:     #if your choice is 3
            a.truck_in()    #the program will summon truck_in def
        if choice == 4:     #if your choice is 4
            print("Good Bye")      #it will print "Good Bye" and stop the loop
            break

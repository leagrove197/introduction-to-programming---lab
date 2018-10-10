print ("================================================================================" 
       "\n\t\t\t\t\t\t\tToll Payment Systems" 
       "\n\t\t\t\t\t\t\tPT Jasa Marga, Tbk."
      "\n================================================================================") #print the Toll Payment Systems PT Jasa Marga,Tbk. in exact same output as the assignment example

def printMenu():    #define print Menu
    while True:     #make while loop
        print("Which Toll Gate ? :")
        print("1. Tol Meruya")
        print("2. Pondok Aren")
        print("3. Check Grand Total Price")
        print("4. Stop Program")            #print all choice you want to choose
        choice=int(input("Enter Choice:"))  #print all of this for you to choose choose here, and your choice will be convert into integer
        if choice == 1:               #if you choose 1, it will print define print1
            print1()
        if choice == 2:                 #if you choose 2, it will print define print2
            print2()
        if choice == 3:                 #if you choose 3, it will call checkTotalPrice define
            a.checkTotalPrice()
        if choice == 4:             #if you choose 4, it will print "Good Bye" and exit the loop
            print("Good Bye")
            break


def print1():          #define print1
    while True :        #make loop for tol Meruya
        print("Location Gate : Meruya")
        print("Category of Vehicle :")
        print("1. \tCar\t\t(RP 6000)")
        print("2. \tBus\t\t(RP 8000)")
        print("3. \tTruck\t(RP 9000)")
        print("4. \tTotal Price")
        print("5. \tChange Gate Location")
        print("6. \tStop Program")          #print all choice you want to choose
        choice=int(input("Enter choice: ")) #print all of this for you to choose choose here, and your choice will be convert into integer
        if choice == 1:     #if you choose 1, it will call Car_in define
            a.Car_in()
        if choice == 2:     #if you choose 2, it will call Bus_in define
            a.Bus_in()
        if choice == 3:     #if you choose 3, it will call Truck_in define
            a.Truck_in()
        if choice == 4:     #if you choose 4, it will call checkPrice define
            a.checkPrice()
        if choice == 5:     #if you choose 5, it will call printMenu define (on top of this)
            printMenu()
        if choice == 6:     #if you choose 6, it will print "Good Bye" and exit the loop
            print("Good Bye")
            break

def print2():       #define print1
    while True :        #make loop for tol Pondok Aren
        print("Location Gate : Pondok Aren")
        print("Category of Vehicle :")
        print("1. \tCar\t\t(RP 18000)")
        print("2. \tBus\t\t(RP 20000)")
        print("3. \tTruck\t(RP 25000)")
        print("4. \tTotal Price")
        print("5. \tChange Gate Location")
        print("6. \tStop Program")           #print all choice you want to choose
        choice=int(input("Enter choice: ")) #print all of this for you to choose choose here, and your choice will be convert into integer
        if choice == 1:     #if you choose 1, it will call Car_in define
            a.Car2_in()
        if choice == 2:     #if you choose 2, it will call Bus_in define
            a.Bus2_in()
        if choice == 3:     #if you choose 3, it will call Truck_in define
            a.Truck2_in()
        if choice == 4:     #if you choose 4, it will call checkPrice define
            a.checkPrice2()
        if choice == 5:     #if you choose 5, it will call printMenu define (on top of this)
            printMenu()
        if choice == 6:     #if you choose 6, it will print "Good Bye" and exit the loop
            print("Good Bye")
            break

class Tol():                    #make class Tol
    def __init__(self,type):    #define init the type
        self.priceCar = 6000#make self price for car which is 6000 Rupiahs
        self.priceBus = 8000    #make self price for bus which is 8000 Rupiahs
        self.priceTruck = 10000 #make self price for truck which is 10000 Rupiahs
        self.priceCar2 = 18000  #make self price for car which is 18000 Rupiahs
        self.priceBus2 = 20000  #make self price for bus which is 20000 Rupiahs
        self.priceTruck2 = 25000    #make self price for truck which is 250000 Rupiahs
        self.carList = []   #make self list for car
        self.busList = []   #make self list for bus
        self.truckList = [] #make self list for truck
        self.carList2 = []  #make self list for car2
        self.busList2 = []  #make self list for bus2
        self.truckList2 = []    #make self list for truck2
        self.type = type    #make self list for type

    def checkPrice(self):   #define checkPrice (for checking the total revenue)
        print("---------------------")
        print("Car\t\tBus\t\tTruck")
        print("---------------------")  #print the car \tab bus \tab truck
        carNum = int(len(self.carList)) #calculate the total of car that went in the tol
        busNum = int(len(self.busList)) #calculate the total of bus that went in the tol
        truckNum = int(len(self.truckList)) #calculate the total of truck that went in the tol
        print ("",carNum ,"\t\t", busNum , "\t\t " , truckNum)
        print("---------------------\n")        #print out the calculationin carNum, busNum, and truckNum
        if int(len(self.carList)) == 0 and int(len(self.busList)) == 0 and int(len(self.truckList)) == 0 :  #if len of the transportation is 0, or no transport has entered the tol,
            print("Total Revenue : " ,"RP.0")                                                                   #it print out total price 0 Rupiahs
        else :
            carNum = int(len(self.carList)) #calculate the total of car that went in the tol
            busNum = int(len(self.busList)) #calculate the total of bus that went in the tol
            truckNum = int(len(self.truckList))#calculate the total of truck that went in the tol
            price = carNum * self.priceCar + busNum * self.priceBus + truckNum * self.priceTruck    #calculate the total price
            print("Total Revenue : " ,"RP." ,price,"\n")    #print out the total price
            return price    #to save the total price so we can plus it with price2 in Pondok Aren tol

    def checkPrice2(self):      #define checkPrice (for checking the total revenue)
        print("---------------------")
        print("Car\t\tBus\t\tTruck")
        print("---------------------")      #print the car \tab bus \tab truck
        carNum2 = int(len(self.carList2))   #calculate the total of car2 that went in the tol
        busNum2 = int(len(self.busList2))   #calculate the total of bus2 that went in the tol
        truckNum2 = int(len(self.truckList2))   #calculate the total of truck2 that went in the tol
        print ("",carNum2 ,"\t\t", busNum2 , "\t\t " , truckNum2)
        print("---------------------\n")             #print out the calculationin carNum, busNum, and truckNum
        if int(len(self.carList2)) == 0 and int(len(self.busList2)) == 0 and int(len(self.truckList2)) == 0 : #if len of the transportation is 0, or no transport has entered the tol,
            print("Total Revenue : " ,"RP.0")                                                                       #it print out total price 0 Rupiahs
        else :
            carNum = int(len(self.carList2))    #calculate the total of car2 that went in the tol
            busNum = int(len(self.busList2))    #calculate the total of bus2 that went in the tol
            truckNum = int(len(self.truckList2))    #calculate the total of truck2 that went in the tol
            price2 = carNum * self.priceCar2 + busNum * self.priceBus2 + truckNum * self.priceTruck2     #calculate the total price
            print("Total Revenue : " ,"RP." ,price2,"\n")    #print out the total price
            return price2                           #to save the total price2 so we can plus it with price in Meruya tol

    def checkTotalPrice(self):      #define checkTotalPrice to calculate the total price, price tol meruya + price tol Pondok Aren
        if int(len(self.carList2)) == 0 and int(len(self.busList2)) == 0 and int(len(self.truckList2)) == 0 and int(len(self.carList)) == 0 and int(len(self.busList)) == 0 and int(len(self.truckList)) == 0:
            print("\nTotal Revenue : " ,"RP.0\n")   #if len of the transportation is 0, or no transport has entered the tol,it print out total price 0 Rupiahs
        else :
            totalPrice = a.checkPrice() + a.checkPrice2()   #calculate the total price of both tol
            print("\nTotal Revenue : " ,totalPrice,"\n")    #print out the total price

class Transportation(Tol):          #create the Transportation class and inherit the tol clas inside the Transportation class

    def Car_in(self):            #define car_in
        self.carList.append(self.type)  #to count how many times you type the car choice, so it will count many cars that went in
        print("\nFee :",self.priceCar,"\n")#it will show you the price everytime you choose to get the car in

    def Bus_in(self):
        self.busList.append(self.type)  #to count how many times you type the bus choice, so it will count many buses that went in
        print("\nFee :",self.priceBus,"\n") #it will show you the price everytime you choose to get the bus in

    def Truck_in(self):
        self.truckList.append(self.type)    #to count how many times you type the truck choice, so it will count many trucks that went in
        print("\nFee :",self.priceTruck,"\n")   #it will show you the price everytime you choose to get the Truck in


    def Car2_in(self):           #define car2_in
        self.carList2.append(self.type) #to count how many times you type the car2 choice, so it will count many cars that went in
        print("\nFee :",self.priceCar2,"\n")#it will show you the price everytime you choose to get the car2 in
    def Bus2_in(self):
        self.busList2.append(self.type) #to count how many times you type the bus2 choice, so it will count many buses that went in
        print("\nFee :",self.priceBus2,"\n")    #it will show you the price everytime you choose to get the bus2 in
    def Truck2_in(self):
        self.truckList2.append(self.type)   #to count how many times you type the truck2 choice, so it will count many trucks that went in
        print("\nFee :",self.priceTruck2,"\n")  #it will show you the price everytime you choose to get the Truck in
a = Transportation("Transportation")    #call the class Transportation

printMenu() #to summon the printMenu

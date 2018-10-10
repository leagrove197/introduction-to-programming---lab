print ("================================================================================" 
       "\n\t\t\t\t\t\t\tToll Payment Systems" 
       "\n\t\t\t\t\t\t\tPT Jasa Marga, Tbk."
      "\n================================================================================")#print the Toll Payment Systems PT Jasa Marga,Tbk. in exact same output as the assignment example


class Tol():#create class tol
    def __init__(self,type):    #define init the type
        self.priceCar = 6000    #make self price for car which is 6000 Rupiahs
        self.priceBus = 8000    #make self price for bus which is 8000 Rupiahs
        self.priceTruck = 10000 #make self price for truck which is 10000 Rupiahs
        self.carList = []       #make self list for car
        self.busList = []       #make self list for bus
        self.truckList = [] #make self list for truck
        self.type = type    #to make the self type which we put it in the init

    def TotalTransport(self):       #define Total Transport to count how many transportation that went in the tol
        print("---------------------")
        print("Car\t\tBus\t\tTruck")
        print("---------------------")  #print the car \tab bus \tab truck
        carNum = int(len(self.carList)) #calculate the total of car that went in the tol
        busNum = int(len(self.busList)) #calculate the total of bus that went in the tol
        truckNum = int(len(self.truckList)) #calculate the total of truck that went in the tol
        print ("",carNum ,"\t\t", busNum , "\t\t " , truckNum)
        print("---------------------")                          #print out the calculationin carNum, busNum, and truckNum

    def checkPrice(self):       #define checkPrice to count how much money the tol get after all of the transportation went in the tol
        if int(len(self.carList)) == 0 and int(len(self.busList)) == 0 and int(len(self.truckList)) == 0 :  #if len of the transportation is 0, or no transport has entered the tol,
            print("Total Revenue: " ,"RP 0")                                                                      #it print out total price 0 Rupiahs
        else :
            carNum = int(len(self.carList)) #calculate the total of car that went in the tol
            busNum = int(len(self.busList)) #calculate the total of bus that went in the tol
            truckNum = int(len(self.truckList))#calculate the total of truck that went in the tol
            totalprice = carNum * self.priceCar + busNum * self.priceBus + truckNum * self.priceTruck   #calculate the total price
            rounded_totalprice = int(round(totalprice)) #to round the total price
            price_str = "{:,}".format(rounded_totalprice)   #add , every 3 number, for example 1000000 become 1,000,000
            print("\nTotal Revenue: " ,"RP" ,price_str,"\n")    #print out the total price

class Transportation(Tol):      #create the Transportation class and inherit the tol clas inside the Transportation class

    def car_in(self):   #define car_in
        self.carList.append(self.type)  #to count how many times you type the car choice, so it will count many cars that went in
        print("\nFee :",self.priceCar,"\n") #it will show you the price everytime you choose to get the car in

    def bus_in(self):
        self.busList.append(self.type)#to count how many times you type the bus choice, so it will count many buses that went in
        print("\nFee :",self.priceBus,"\n")#it will show you the price everytime you choose to get the bus in

    def truck_in(self):
        self.truckList.append(self.type)#to count how many times you type the truck choice, so it will count many trucks that went in
        print("\nFee :",self.priceTruck,"\n")#it will show you the price everytime you choose to get the Truck in

a = Transportation("Transportation")    #call the class Transportation

while True :

        print("Category of Transportation:")
        print("1. \tCar\t\t(RP. 6000)")
        print("2. \tBus\t\t(RP. 8000)")
        print("3. \tTruck\t(RP. 9000)")
        print("4. \tTotalTransport")
        print("5. \tTotal Price")           #print all of this for you to choose
        print("6. \tStop Program")
        choice=int(input("Enter choice: "))#print all of this for you to choose choose here, and your choice will be convert into integer
        if choice == 1: #if your choice is 1
            a.car_in()  #the program will summon car_in def
        if choice == 2: #if your choice is 2
            a.bus_in()  #the program will summon bus_in def
        if choice == 3: #if your choice is 3
            a.truck_in()    #the program will summon truck_in def
        if choice == 4: #if your choice is 4
            a.TotalTransport()     #the program will summon TotalTransport def
        if choice == 5: #if your choice is 5
            a.checkPrice()  #the program will summon checkPrice def
        if choice == 6:     #if your choice is 6
            print("Good Bye")  #it will print "Good Bye" and stop the loop
            break

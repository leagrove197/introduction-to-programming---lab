account = []   #make list of account and balance that we will be using in code below
balance = []
class Account: #make class for Account because we wanna create the account first before using the ATM
    def new_acc(self):              #define new_acc by using class
        global c             #to globalize c so it can be use in code below
        firstname = input("your first name :") #to type your firstname in the input
        lastname = input("your last name :") #to type your lastname in the input
        c=Customer(firstname,lastname) #to summon the customer class (firstname and lastname)
        c.regist()                  #to summon the regist define by using class method
class Customer:                      #make another class for the customer to do what they want to do with the bank
    def __init__(self, firstname, lastname): #use class and object so we can type our firstname and lastname
        self.firstname = firstname
        self.lastname = lastname
    def regist(self):   #define regist which we will be using to register
        global account #globalize account
        global balance    #globalize balance
        balance.append(0)     #we add 0 to the balance which means we have 0 money in our bank
        account.append(self.firstname + " " + self.lastname) #we add firstname and lastname to the account. so that when we type our name, our name will appear in our account profile
        print ("congraluations! you have been registered\n")
    def deposit(self):  #define deposit which we will be using to deposit
        global account  #globalize account
        global balance  #globalize balance
        q1 = int(input("which account : "))     #to ask the first question and make q1 variable
        q2 = int(input ("how much :"))          #to ask the 2nd question and make q2 variable
        balance[q1] += q2         #to calculate the deposit which means everytime we enter number in q2, it will be added to q1 using additive operator
        print ("\n")                    #so we deposit the money in q2 and it will go to your balance (q1)
    #we print "\n" to make enter space
    def withdraw(self):             #define withdraw which we will be using to withdraw
        global account  #globalize account
        global balance  #globalize balance
        q1 = int(input("which account : ")) #to ask the first question and make q1 variable
        q2 = int(input ("how much :"))      #to ask the 2nd question and make q2 variable
        balance[q1] -= q2                    #to calculate the withdraw which means everytime we enter number in q2, q1 will be decreasing by the number we enter in q2
        print ("\n")
    def transfer(self):     #to define transfer which we will be using to transfer
        global account  #globalize account
        global balance  #globalize balance
        q1 = int(input ("from which account :"))#to ask the first question and make q1 variable
        q2 = int(input ("to which account :")) #to ask the 2nd question and make q2 variable
        q3 = int(input("how much :")) #to ask the 3rd question and make q3 variable
        balance[q2] += q3       #to calculate the transfer which means everytime we enter number in q3, q2 will be added by that number using additive operator
        balance[q1] -= q3       #everytime we enter number in q3, the q1 balance will be decreasing the same amount of q3 (q1 - q3)
    def delete(self):   #define delete which we will be using to delete account
        global account  #globalize account
        global balance  #globalize balance
        q1 = int(input("which account you want to Delete :"))   #to ask 1st question
                #which account you want to delete, because you can have more than 1 account and you can choose which account you want to delete
        q2 = input ("are you sure? \t :")   #to ask 2nd question and make q2 variable
        q2=q2.lower()   #to lowercase whatever you type in q2
        if q2 == "yes": #if you type yes, the account you wanna delete will be deleted
            del account[q1]
            del balance[q1]
        elif q2 =="no":             #if you type no, the account won't be deleted
            print ("Okay\n")
        else :
            print ("invalid\n")     #if you don't type yes or no, it will print invalid
choose = 1      #make variable choose which is an integer, choose = 1
while choose != 0: #it means like, if choose is not 0, then it will print :
    print ("0 Exit")
    print ("1. Create New Account")
    print ("2. See Your Account Profile")
    print ("3 deposit")
    print ("4 withdraw")
    print ("5 transfer")
    print ("6 delete account")
    choose = int(input("choose :")) #we can type the number to tell the ATM what we want to do

    if choose == 1: #if you type 1 in the input, then it will summon the regist define and class account
        a= Account() #so this is where you enter your name and register
        a.new_acc()
    elif choose == 2:   #if you type 2 in the input, then it show you the [account] that you have made in choose 1
        for i in range (len(account)):
            print ("\nAccount Number : ", i, "\nName : " ,account[i], "\nBallance : Rp." , balance[i] ,"\n")
                #if you print like this, it will show your profile account

    elif choose == 3:  #if you type 3 in the input, then it will summon the deposit define
        c.deposit()

    elif choose == 4:#if you type 4 in the input, then it will summon the withdraw define
        c.withdraw()

    elif choose == 5:#if you type 5 in the input, then it will summon the transfer define
        c.transfer()

    elif choose ==6:#if you type 6 in the input, then it will summon the delete define
        c.delete()

    elif choose == 0:#if you type 0 in the input, it will exit because we are in the while choose !=0: loop
        print ("Good Bye")

    else :
        print ("INVALID\n") #if you type other than number in above, it will print invalid






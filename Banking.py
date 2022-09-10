import pickle  # converts any kind of python objects(list,dict etc) into byte stream (byte binary codde)
import os
import pathlib  # used for easy path setting


class Account:
    accNo = 0
    name = ''
    deposit = 0
    type = ''

    def createAccount(self):
        self.accNo = int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
        print("\n\n\nAccount Created")

    def showAccount(self):
        print("Account Number : ", self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account", self.type)
        print("Balance : ", self.deposit)

    def modifyAccount(self):
        print("Account Number : ", self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        self.deposit -= amount

    def report(self):
        print(self.accNo, " ", self.name, " ", self.type, " ", self.deposit)

    def getAccountNo(self):
        return self.accNo

    def getAcccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit


# methods outside of class


def intro():
    print("\t\t\t\t***********************************************")
    print("\t\t\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t***********************************************")
    print("\t\t\t\t\t\t\t\tBY TEJAREDDY POLADI")
    input("press any key to enter into bank console")


def writeAccount():
    obj_account = Account()  # obj_account is an object created for Accounts class
    obj_account.createAccount()  # calling createAccounts Method

    writeAccountsFile(obj_account)
    # after the execution of writeAccountsFile method this line will be called


def writeAccountsFile(account):
    file = pathlib.Path("customerinfo.data")
    if file.exists():
        infile = open('customerinfo.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('customerinfo.data')
    else:
        oldlist = [account]
    outfile = open('newaccounts.data', 'wb')  # wb=write binary (this statement creates the file)
    pickle.dump(oldlist, outfile)  # converts obj file to byte binary code
    outfile.close()
    os.rename('newaccounts.data', 'customerinfo.data')  # renamed newaccounts.data to customerinfo.data


def displayAll():
    file = pathlib.Path("customerinfo.data")
    if file.exists():  # if any data exists in file returns True
        infile = open('customerinfo.data', 'rb')  # rb=readbinary (justs read binary file)

        mylist = pickle.load(infile)  # converts byte format(pickled) to object format(unpickled)
        for item in mylist:
            print(item.accNo, " ", item.name, " ", item.type, " ", item.deposit)

            # adding the input we give in accountNo,name,type,deposit lists to the byte binary file
        infile.close()
    else:
        print("No records to display")


def displaySp(num):
    file = pathlib.Path("customerinfo.data")
    if file.exists():
        infile = open('customerinfo.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.accNo == num:  # we will pass the input num in the end of the code
                print("Your account Balance is = ", item.deposit)
                found = True
    else:
        print("No records to Search")
    if not found:  # if not found==(not true)
        print("No existing record with this number")


def depositAndWithdraw(num1, num2):
    file = pathlib.Path("customerinfo.data")
    if file.exists():
        infile = open('customerinfo.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('customerinfo.data')
        for item in mylist:
            if item.accNo == num1:
                if num2 == 1:
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updted")
                elif num2 == 2:
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                    else:
                        print("You cannot withdraw larger amount")

    else:
        print("No records to Search")
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'customerinfo.data')


def deleteAccount(num):
    file = pathlib.Path("customerinfo.data")
    if file.exists():
        infile = open('customerinfo.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.accNo != num:
                newlist.append(item)
        os.remove('customerinfo.data')
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'customerinfo.data')


def modifyAccount(num):
    file = pathlib.Path("customerinfo.data")
    if file.exists():
        infile = open('customerinfo.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('customerinfo.data')
        for item in oldlist:
            if item.accNo == num:
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))

        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'customerinfo.data')


# start of the program
ch = ''
num = 0
intro()

while ch != 8:
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    ch = input(("\tSelect Your Option (1-8) :"))
    print("\n")

    if ch == '1':
        writeAccount()
        print("\n")
    elif ch == '2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
        print("\n")
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
        print("\n")
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
        print("\n")
    elif ch == '5':
        displayAll()
        print("\n")
    elif ch == '6':
        num = int(input("\tEnter The account No. : "))
        deleteAccount(num)
        print("\n")
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(num)
        print("\n")
    elif ch == '8':
        print("\tThanks for using bank managemnt system")
        break
    else:
        print("Invalid choice")
        print("\n")

    # ch = input("Enter your choice : ")













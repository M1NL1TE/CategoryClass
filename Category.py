import validation

class Category:

    categories = {'Food': 0, 'Clothing': 0, 'Car': 0}
    def __init__(self):
       self.Category = ""
       self.Amount = 0

    def budget(self):
        catChoice = int(input("Select a budget category: (1) Food (2) Clothing (3) Car (4) Other\n"))

        if catChoice == 1:
            self.Category = "Food"
            balanceAmount = input("How much do you want to use for the budget?\n$")

            self.setBalance(balanceAmount)

            self.budgetOperations()
        
        elif catChoice == 2:
            self.Category = "Clothing"
            balanceAmount = input("How much do you want to use for the budget?\n$")

            self.setBalance(balanceAmount)

            self.budgetOperations()
        
        elif catChoice == 3:
            self.Category = "Car"
            balanceAmount = input("How much do you want to use for the budget?\n$")

            self.setBalance(balanceAmount)
            self.budgetOperations()
        
        elif catChoice == 4:
            self.Category = input("Type in the name of this budget's category: ")
            self.CustCat = self.Category
            self.categories[self.Category] = 0
            self.budgetOperations()
        
        else:
            print("Invalid input, try again\n")
            self.budget()

    def budgetOperations(self):
        
        selectedOption = int(input("What would you like to do? (1) deposit (2) withdraw (3) Transfer (4) Check balance (5) Switch active account (6) Exit\n"))

        
        if(selectedOption == 1):
            self.deposit()
        elif(selectedOption == 2):
            self.withdraw()
        elif(selectedOption == 3):
            self.transfer()
        elif(selectedOption == 4):
            self.checkBalance(self.Category)
        elif(selectedOption == 5):
            self.budget()
        elif(selectedOption == 6):
            exit()
        else:
            print("Invalid option selected")
            self.budgetOperations()


    # def setAmount(self):
    #     self.Amount = int(input("Enter your budget amount: "))

    def deposit(self):
        print("====DEPOSIT====\n")
        currentBalance = self.getBalance(self.Category)
        print("Your balance is %s\n" % "${:,.2f}".format(currentBalance))
        depositAmount = input("Enter deposit amount: ")

        is_valid_amount = validation.money_validation(depositAmount)

        if is_valid_amount:

            depositAmount = int(depositAmount)
            self.Amount += depositAmount
            self.budgetOperations()
        else:
            print("Something went wrong\n")
            self.deposit()
    
    def withdraw(self):
        print("====WITHDRAW====\n")
        currentBalance = self.getBalance(self.Category)

        if (currentBalance == 0):
            print("insufficient funds\n(You should make a deposit first).\n")
            self.withdraw()
        print("Your balance is %s\n" % "${:,.2f}".format(currentBalance))
        withdrawAmount = input("Enter withdraw amount: ")

        is_valid_amount = validation.money_validation(withdrawAmount)

        if is_valid_amount:
            withdrawAmount = int(withdrawAmount)
            while withdrawAmount > currentBalance:
                print("Insuffient funds, you only have %s left in your account. Enter new amount\n" % "${:,.2f}".format(currentBalance))
                 # Formats currentBalance to currency
                withdrawAmount = int(input())
            self.Amount -= withdrawAmount
            self.budgetOperations()
        else:
            print("Something went wrong\n")
            self.withdraw()

    def getBalance(self, Category):
        for key in self.categories:
            if key == Category:
                return self.categories[key]
            else:
                return False

    def checkBalance(self, Category):
        was_successful = False
        for key in self.categories:
            if key == Category:
                print("Your balance is %s\n" % "${:,.2f}".format(self.categories[key]))
                was_successful = True
                self.budgetOperations()
        if not was_successful:
            print("Something went wrong\n")
            self.budgetOperations()
                


    def setBalance(self, Amount):

        is_valid_balance = validation.money_validation(Amount)
        was_successful = False

        if is_valid_balance:
            Amount = int(Amount)
            self.Amount = Amount
            for key in self.categories:
                if key == self.Category:
                    was_successful = True
                    self.categories[key] = Amount
            
            if not was_successful:
                print("Something went wrong\n")
                
        else:
            print("Something went wrong\n")
            self.budget()

    def transfer(self):
        
        #This transfer method will allow input for an amount to transfer
        print("Select the account you would like to transfer from:\n")
        accountFromSelection = int(input("(1) Food (2) Clothing (3) Car (4) %s\n" % self.Category))
        accountToSelection = int(input("Now select the account you want to transfer to (same options as above)"))

        if ((accountFromSelection != accountToSelection) and (accountFromSelection > 0 and accountFromSelection < 5) and (accountToSelection > 0 and accountToSelection < 5)):
            transferAmount = input("How much do you want to transfer?\n")
            is_valid_amount = validation.money_validation(transferAmount)

            if is_valid_amount:
                if accountFromSelection == 1:
                    catName = "Food"
                elif accountFromSelection == 2:
                    catName = "Clothing"
                elif accountFromSelection == 3:
                    catName = "Car"
                elif accountFromSelection == 4:
                    catName = self.CustCat

                if accountToSelection == 1:
                    catName = "Food"
                elif accountToSelection == 2:
                    catName = "Clothing"
                elif accountToSelection == 3:
                    catName = "Car"
                elif accountToSelection == 4:
                    catName = self.CustCat

                transferAmount = int(transferAmount)

                #iterate through dictionary and subtract the transfer amount
                #iterate through dictionary a second time and add transfer amount to "To" category





                self.budgetOperations()



def init():
    cat = Category()

    cat.budget()
    # cat.setAmount()


init()
class Category:

    #categories = {'Food': 0, 'Clothing': 0, 'Car': 0}
    def __init__(self):
       self.Category = ""
       self.Amount = 0

    def setCategory(self):
        catChoice = int(input("Select a budget category (1) Food (2) Clothing (3) Car (4) Other\n"))

        if catChoice == 1:
            self.Category = "Food"
        
        elif catChoice == 2:
            self.Category = "Clothing"
        
        elif catChoice == 3:
            self.Category = "Car"
        
        elif catChoice == 4:
            self.Category = input("Type in the name of this budget's category: ")
        
        else:
            print("Invalid input, try again\n")
            self.setCategory()

    def setAmount(self):
        self.Amount = int(input("Enter your budget amount: "))

    def deposit(self):
        pass


def init():
    cat = Category()

    cat.setCategory()
    cat.setAmount()


init()
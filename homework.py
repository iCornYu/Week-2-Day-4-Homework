#Excerise 1:

class Shopcartclass():
    def __init__(self):
        pass
    def add1(self,item):
        if item in self.__dict__:
            addinput = input(f"How many more {item}s do you want? (Enter a number)")
            try:
                self.__dict__[item] += int(addinput)
            except ValueError:
                print(f"{addinput} is not a valid number. Please try again.")
        else:
            addinput = input(f"How many {item}s do you want? (Enter a number) ")
            try:
                self.__dict__[item] = int(addinput)
            except ValueError:
                print(f"{addinput} is not a valid number. Please try again.")
        print(self.__dict__)
    def delete1(self,item):
        if item in self.__dict__:
            deleteinput = input(f"How many {item}s would you like to delete? (Enter a number)")
            try:
                self.__dict__[item] -= int(deleteinput)
                if self.__dict__[item] <= 0:
                    del self.__dict__[item]
                    print(f"All {item}s has been deleted from the shopping cart.")
                print(self.__dict__)
            except ValueError:
                print(f"{deleteinput} is not a valid number. Please try again.")
        else:
            print(f'You do not have {item} in your shopping cart. Please try again.')
    def show1(self):
        print(self.__dict__)
    def clear1(self):
        clearinput = input("Are you sure you want to clear the list? (Yes/No)")
        if clearinput.lower().strip() == "yes":
            self.__dict__.clear()
            print(self.__dict__)
            print("Your list has been cleared.")
        else:
            print("Returning to main menu.")
            
            
            
def shopcart():
    shoppingcart = Shopcartclass()
    while True:
        question = input("What would you like to do? Type 'Show/Add/Delete/Clear/Quit.'")
        if question.lower().strip() == "quit":
            break
        elif question.lower().strip() == "add":
            additem = input("Type the item you would like to add. Type 'quit' to return to main menu.")
            if additem.lower().strip() == "quit":
                continue
            else:
                additemstrip = additem.strip().title()
                shoppingcart.add1(additemstrip)
        elif question.lower().strip() == "delete":
            deleteitem = input("Type the item you would like to delete. Type 'quit' to return to main menu")
            if deleteitem.lower().strip() == "quit":
                continue
            else:
                deleteitemstrip = deleteitem.strip().title()
                shoppingcart.remove1(deleteitemstrip)
        elif question.lower().strip() == "show":
            shoppingcart.show1()
        elif question.lower().strip() == "clear":
            shoppingcart.clear1()
            
        else:
            print("Invalid input. Please try again.")
            
                
shopcart()             

#Exercise 2:
class Pythonprintget():
    def __init__(self):
        self.string1 = ""
    def get_string(self):
        self.string1 = input()
    
    def print_string(self):
        print(self.string1.upper())

string1 = Pythonprintget()
string1.get_string()
string1.print_string()
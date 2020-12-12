class contact_menu:
    opt = 0
    def __init__ (self, opt):
        self.opt = opt
        print("*******Contact Book********")
    # Menu function


    def menu(self): 
            print("Choose an option from the following list:")
            print("1.Add a new contact")
            print("2.Remove an existing contact")
            print("3.Delete all contacts")
            print("4.Search for a contact")
            print("5.Display all contact")
            print("6.Exit Contact Book")
            self.opt = int(input("Enter an option:"))
            return self.opt
# Single Inheritance        
class allfunct(contact_menu):
    def __init__(self):
        self.contbook = contbook
    def add_contact(self):
        book = []
        for i in range(0, 4):
            if i == 0:
                book.append(str(input("Name:")))
            if i == 1:
                book.append(str(input("Address:")))
            if i == 2:
                book.append(int(input("Contact Number:")))
            if i == 3:
                book.append(str(input("Email:")))
            if i == 4:
                book.append(str(input("(Family/Friends/Work/Others):")))
        self.contbook.append(book)
        return self.contbook

    def display_all(self):
        if not self.contbook:
            print("\nContact book is empty")
        else:
            for i in range(len(contbook)):
                print(self.contbook[i])

    def delete_all(self):
        return self.contbook.clear()

    def delete(self):
        name = str(input("Enter the name of person to delete from the book:"))
        temp = 0
        for i in range(len(self.contbook)):
            if name == self.contbook[i][0]:
                temp += 1
                print("The contact details of ", contbook[i][0], "is removed")
                self.contbook.pop(i)
                return self.contbook
        if temp == 0:
                print("Entered name is not found")
                return self.contbook

    def search(self):
        print("1.Name")
        print("2.Address")
        print("3.Number")
        print("4.Email")
        print("5.Category")
        optn = int(input("Enter search criteria"))
        temp = []
        if optn == 1:
            option = str(input("Enter the name"))
            for i in range(len(self.contbook)):
                if option == self.contbook[i][0]:
                    temp.append(self.contbook[i])
        elif optn == 2:
            option = str(input("Enter the Address"))
            for i in range(len(contbook)):
                if option == self.contbook[i][1]:
                    temp.append(self.contbook[i])
        elif optn == 3:
            option = int(input("Enter the number"))
            for i in range(len(self.contbook)):
                if option == int(self.contbook[i][2]):
                    temp.append(self.contbook[i])
        elif optn == 4:
            option = str(input("Enter the email"))
            for i in range(len(self.contbook)):
                if option == self.contbook[i][3]:
                    temp.append(self.contbook[i])
        elif optn == 5:
            option = str(input("Enter the category"))
            for i in range(len(self.contbook)):
                if option == self.contbook[i][4]:
                    temp.append(self.contbook[i])
        else:
            print("Invalid input")
        print(temp)

def primaryphone_book():
    phone_book = []
    rows = int(input("Enter intial number of contacts in contact book"))
    cols = 5
    for i in range(rows):
        temp_list = []
        for j in range(cols):
            if j == 0:
                temp_list.append(str(input("Name:")))
            if j == 1:
                temp_list.append(str(input("Address:")))
            if j == 2:
                temp_list.append(int(input("Contact Number:")))
            if j == 3:
                temp_list.append(str(input("Email:")))
            if j == 4:
                temp_list.append(str(input("(Family/Friends/Work/Others):")))
        phone_book.append(temp_list)
    return phone_book
contbook = primaryphone_book()
cont1 = allfunct(contbook)
while cont1.opt < 6:
    cont1.menu()
    cont1.opt
    if cont1.opt == 1:
        contbook = cont1.add_contact(contbook)
    elif cont1.opt == 2:
        contbook = cont1.delete(contbook)
    elif cont1.opt == 3:
        contbook = cont1.delete_all(contbook)
    elif cont1.opt == 4:
        print(cont1.search(contbook))
    elif cont1.opt == 5:
        print(cont1.display_all(contbook))
    else:
        print("Enter correct option")

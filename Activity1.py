class contact_menu:

    def __init__(self):
        self.opt = 0
        print("*******Contact Book********")

    def menu(self):
            print("Choose an option from the following list:")
            print("1.Add a new contact")
            print("2.Remove an existing contact")
            print("3.Delete all contacts")
            print("4.Search for a contact")
            print("5.Display all contact")
            print("6.Exit Contact Book")
            self.opt = int(input("Enter an option:"))


class allfunct:
    def add_contact(self, contbook):
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
            contbook.append(book)
        return contbook

    def display_all(self, contbook):
        if not contbook:
            print("\nContact book is empty")
        else:
            for i in range(len(contbook)):
                print(contbook[i])

    def delete_all(self, contbook):
        return contbook.clear()

    def delete(self, contbook):
        name = str(input("Enter the name of person to delete from the book:"))
        temp = 0
        for i in range(len(contbook)):
            if name == contbook[i][0]:
                temp += 1
                print("The contact details of ", contbook[i][0], "is removed")
                contbook.pop(i)
                return contbook
        if temp == 0:
                print("Entered name is not found")
                return contbook

    def search(self, contbook):
        print("1.Name")
        print("2.Address")
        print("3.Number")
        print("4.Email")
        print("5.Category")
        opt = int(input("Enter search criteria"))
        temp = []
        if opt == 1:
            option = str(input("Enter the name"))
            for i in range(len(contbook)):
                if option == contbook[i][0]:
                    temp.append(contbook[i])
        elif opt == 2:
            option = str(input("Enter the Address"))
            for i in range(len(contbook)):
                if option == contbook[i][1]:
                    temp.append(contbook[i])
        elif opt == 3:
            option = int(input("Enter the number"))
            for i in range(len(contbook)):
                if option == int(contbook[i][2]):
                    temp.append(contbook[i])
        elif opt == 4:
            option = str(input("Enter the email"))
            for i in range(len(contbook)):
                if option == contbook[i][3]:
                    temp.append(contbook[i])
        elif opt == 5:
            option = str(input("Enter the category"))
            for i in range(len(contbook)):
                if option == contbook[i][4]:
                    temp.append(contbook[i])
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
contbook = primaryphone_book
cont1 = contact_menu()
cont1.menu()
cont1.opt
if cont1.opt == 1:
    contbook = cont1.add_contact(contbook)
if cont1.opt == 2:
    contbook = cont1.delete(contbook)
if opt == 3:
    contbook = cont1.delete_all(contbook)
if opt == 4:
    print(cont1.search(contbook))
if opt == 5:
    cont1.display_all(contbook)

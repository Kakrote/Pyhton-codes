import time as t
class main_library:
    def __init__(self,name_of_library):
        # self.n=no_books
        self.name=name_of_library
        pass
    def add_book(self):
        n=int(input("Enter the number of books you want to enter:- "))
        f=open("lib.txt","+a")
        print("Enter the name of the books")
        for i in range(n):
            books=f.write(input()+"\n")
        f.close()
    def lend_book(self):
        current_time = t.asctime(t.localtime(t.time()))
        book = input("Enter the name of the book: ")

        found = False

        with open("lib.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if book in line:
                    with open("lend.txt", "a") as f1:
                        f1.write(f"{book}\t{current_time}\n")
                    print("Successful")
                    found = True
                    break

            if not found:
                print("Book not found! Sorry")
    def return_book():
        pass
    def all_books_avilable(slef):
        f=open("lib.txt","+r")
        data=f.read()
        print(data)
        f.close()
def menu():
    # n=int(input("Enter the no of books avilable in the liblary  "))
    lib=main_library("Anshul's Collections")
    while True:
        print(f"Welcom to the {lib.name}\n")
        print("1-display all the books\t\t2-Add new book\n3-lend a book\t\t4-return a book\n5-exit")
        op=int(input("Enter the options "))
        if op==1:
            lib.all_books_avilable()
        elif op==2:
            lib.add_book()
        elif op==3:
            lib.lend_book()
        elif op==4:
            lib.return_book()
        elif op==5:
            print("Thank you for visiting \n")
            break
        else: 
            print("wrong input ")
            break
menu()
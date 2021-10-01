

class Library:
    def __init__(self,booklist,name):
        self.booklist = booklist
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have following books in our Library:{self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-book database has been updated.You can take the book now.")  
        else:
            print(f"The book is already used by {self.lendDict[book]}")  

    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been added to the list.")      

    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been added to the book list.")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    lab = Library(['C++ basic','Python','Harry Potter','Java'],'MasterLibrary')
    
    while(True):
        print(f'Welcome to {lab.name}.Enter your choice to continue.')
        print('1.Display Books')
        print('2.Lend a Book')
        print('3.Add a Book')
        print('4.Return a Book')

        user_choice = int(input())

        if user_choice == 1:
           lab.displayBooks()

        elif user_choice == 2:
           book = input('Enter name of book you want to lend :')
           user = input('Enter your name :')
           lab.lendBook(user,book)
        
        elif user_choice == 3:
            book = input('Enter name of book you want to add :')
            lab.addBook(book)

        elif user_choice == 4:            
            book = input('Enter name of book you want to return :')
            lab.returnBook(book)

        else:
            print('Not a valid option.')   

        print('Press q to quit and c to contiune')  
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):  
          user_choice2 = input()
          if user_choice2 == 'q':
            exit()

          elif user_choice2 == 'c':
            continue    


            



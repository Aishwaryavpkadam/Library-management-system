class Library:
    """"
    This class named as library keeps records of books of The Great Library.
    It has total four modules: 'Display Books', 'Lend Books', 'Add Books', 'Return Books'
    
    """
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def display(self):
        print(f"We have the following books available in {self.name} library! Happy Reading!")
        for book in self.booklist:
            print(book)


    def lend(self,user,book):
        if book not in self.lendDict:
            self.lendDict.update({book:user})
            print("The book has been updated in our database. You can take the book now.")
        else:
            print(f"This is already been borrowed by {self.lendDict[book]}")
            print("So sorry! Browse through other books.")

    def add_book(self,book):
        self.booklist.append(book)
        print("The book has been added succesfully! Thank you and have a nice day!")

    def return_book(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':

    books = ['To Kill a Mockingbird by Harper Lee','The Great Gatsby by F Scott Fitzgerald','Things Fall Apart by Chinua Achebe'
    ,'Moby-Dick by Herman Melville','The Color Purple by Alice Walker','Catch-22 by Joseph Heller','Atlas Shrugged by Ayn Rand'
    ,'The Lord of the Rings by J.R.R. Tolkien','Harry Potter and the Philosopher Stone by J.K. Rowling'
    ,'Diary of a Wimpy Kid: Old School by Jeff Kinney','The BFG by Roald Dahl'
    ,'Harry Potter and the Chamber of Secrets by J.K. Rowling','Harry Potter and the prisoner of Azkaban by J.K. Rowling'
    ,'Diary of a Wimpy Kid: Double Down by Jeff Kinney','Awful Auntie by David Walliams','Diary of a Wimpy Kid: by Hard Luck Jeff Kinney'
    ,'Wonder by R.J. Palacio','James and the Giant Peach by Roald Dahl','Ratburger by David Walliams','Matilda by Roald Dahl' ]
    hogwarts = Library(books , "The Great Library")
    while(True):
        print(f"Welcome to {hogwarts.name}. Please enter your choice to continue.")
        print("1. Display all the books in the library.")
        print("2. Lend a book from the library.")
        print("3. Add a book to the library.")
        print("4. Return a book.")

        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option. ")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            hogwarts.display()

        elif user_choice == 2:
            book = input("Enter the name of the book you wish to borrow: ")
            user = input("Please enter your name: ")
            hogwarts.lend(user,book)

        elif user_choice == 3:
            book = input("Enter the name of the book you wish to add: ")
            hogwarts.add_book(book)
            print("Thank you so much for the book!")

        elif user_choice == 4:
            book = input("Enter the name of the book you wish to return : ")
            hogwarts.return_book(book)
        else:
            print("Your choice is not valid.")
        print("If you want to quit then press q and if you want to continue then press c")

        user_choice2 = ""
        while (user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                print("Hope you enjoyed browsing through the library!!")
                exit()

            elif user_choice2 == "c":
                continue








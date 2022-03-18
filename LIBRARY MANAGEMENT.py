import pandas as pd
import matplotlib.pyplot as plt
from datetime import date


print("-----------------------WELCOME TO NATIONAL DIGITAL LIBRARY ASSOCIATION-----------------------")

def AddNewBook() :
    Bookid = int(input("Enter a book id :-  "))
    Title = input("Enter book title :-  ")
    Author = input("Enter author of the book :- ")
    Publisher = input("Enter book publisher :-  ")
    Edition = input("Enter edition of book :-  ")
    Cost = input("Enter cost of the book :-  ")
    Category = input("Enter category of book :-  ")
    bdf = pd.read_csv(r"C:\Users\Sikta\Desktop\available books.csv")
    n = bdf["Bookid"].count ()
    bdf.at[n] = [Bookid, Title, Author, Publisher, Edition, Cost, Category]
    bdf.to_csv(r"C:\Users\Sikta\Desktop\available books.csv",index = False)
    print("Book added successful")
    print(bdf)


def SearchBook() :
    Title = input("Enter a book name :-  ")
    bdf = pd.read_csv(r"C:\Users\Sikta\Desktop\available books.csv")
    df = bdf.loc[bdf["Title"]==Title]
    if df.empty:
        print("No book found with given code")
    else:
        print("Book details are:- ")
        print(df)


def DeleteBook() :
    Bookid = float(input("Enter a book id :- "))
    bdf = pd.read_csv(r"C:\Users\Sikta\Desktop\available books.csv")
    bdf = bdf.drop(bdf[bdf["Bookid"]==Bookid].index)
    bdf.to_csv(r"C:\Users\Sikta\Desktop\available books.csv",index = False)
    print("Book Deleted Successfully")
    print(bdf)


def ShowBooks() :
    bdf = pd.read_csv(r"C:\Users\Sikta\Desktop\available books.csv")
    print(bdf)


def AddNewMember() :
    mid = int(input("Enter a member id :-  "))
    mname = input("Enter member name :-  ")
    Phoneno = int(input("Enter phone number :-  "))
    numberofbooksissued = 0
    mdf = pd.read_csv(r"C:\Users\Sikta\Desktop\members.csv")
    n = mdf["mid"].count()
    mdf.at[n] = [mid, mname, Phoneno, numberofbooksissued]
    mdf.to_csv(r"C:\Users\Sikta\Desktop\members.csv",index = False)
    print("New Member Added Succesfully")
    print(mdf)


def SearchMember() :
    mname = input("Enter a member name :-  ")
    bdf = pd.read_csv(r"C:\Users\Sikta\Desktop\members.csv")
    df = bdf.loc[bdf["mname"]== mname] 
    if df.empty:
        print("No member found with given name")
    else:
        print("Members details are:-  ")
        print(df)


def DeleteMember() :
    mid = float(input("Enter a member id :-  "))
    bdf = pd.read_csv(r"C:\Users\Sikta\Desktop\members.csv")
    bdf = bdf.drop(bdf[bdf["mid"]== mid].index)
    bdf.to_csv(r"C:\Users\Sikta\Desktop\members.csv",index = False)
    print("Member Deleted Succesfully")
    print(bdf)


def ShowMembers() :
    bdf = pd.read_csv(r"C:\Users\Sikta\Desktop\members.csv")
    print(bdf)


def IssueBooks() :
    Book_name = input("Enter book name :-  ")
    bdf = pd.read_csv(r"C:\Users\Sikta\Desktop\issuebooks.csv")
    bdf = bdf.loc[bdf["Title"]== Book_name]
    if bdf.empty:
        print("No Book Found in the library")
        return

    
    Member_name = input("Enter member name :-  ")
    mdf = pd.read_csv(r"C:\Users\Sikta\Desktop\issuebooks.csv")
    mdf = mdf.loc[mdf["Member_name"]== Member_name]
    if mdf.empty:
        print("No Such Member Found")
        return


    Dateofissue = int(input("Enter of date issue :-  "))
    Numberofbookissued = int(input("Number of books issued :-  "))
    bdf = pd.read_csv(r"C:\Users\Sikta\Desktop\issuebooks.csv")
    n = bdf["Book_name"].count()
    bdf.at[n] = [Book_name, Member_name, date.today(), Numberofbookissued,""]
    bdf.to_csv(r"C:\Users\Sikta\Desktop\issuebooks.csv",index = False)
    print("Book Issued Successfully")
    print(bdf)


def ReturnBooks() :
    Member_name = input("Enter member name :-  ")
    Book_name = input("Enter book name :-  ")
    idf = pd.read_csv(r"C:\Users\Sikta\Desktop\issuebooks.csv")
    idf = idf.loc[idf["Book_name"]== Book_name]
    if idf.empty:
        print("The Book is not issued in records")
    else:
        idf = idf.loc[idf["Member_name"]== Member_name]
        if idf.empty:
            print("The book is not issued to the member")
        else:
            print("Book can be returned")
            ans = input("Are you sure you want to return the book : ")
            if ans.lower() == "yes":
                idf = pd.read_csv(r"C:\Users\Sikta\Desktop\issuebooks.csv")
                idf = idf.drop(idf[idf["Book_name"]== Book_name].index)
                idf.to_csv(r"C:\Users\Sikta\Desktop\issuebooks.csv",index = False)
                print("Book Returned Successfully")
            else:
                print("Return operation cancelled")


def ShowIssuedBooks() :
    idf = pd.read_csv(r"C:\Users\Sikta\Desktop\issuebooks.csv")
    print(idf)


def DeleteIssuedBooks() :
    Book_name = input("Enter book name :-  ")
    bdf = pd.read_csv(r"C:\Users\Sikta\Desktop\issuebooks.csv")
    bdf = bdf.drop(bdf[bdf["Book_name"]== Book_name].index)
    bdf.to_csv(r"C:\Users\Sikta\Desktop\issuebooks.csv",index = False)
    print("Deleted Issued Book Successfully")
    print(bdf)


def ShowCharts() :
    print("Press 1 - Books and their Cost")
    print("Press 2 - Number of Books issued by member")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        df = pd.read_csv(r"C:\Users\Sikta\Desktop\available books.csv")
        df = df [["Title","Cost"]]
        df.plot("Title","Cost",kind= 'bar')
        plt.xlabel('Title------->')
        plt.ylabel('Cost------->')
        plt.show()

    if ch == 2:
        df = pd.read_csv(r"C:\Users\Sikta\Desktop\issuebooks.csv")
        df = df[["Numberofbooksissued","Member_name"]]
        df.plot(kind='bar', color = "red")
        plt.show()


def Login() :
    uname = input("Enter Username : ")
    pwd = input("Enter Password : ")
    df = pd.read_csv(r"C:\Users\Sikta\Desktop\users.csv")
    df = df.loc[df["username"] == uname]
    if df.empty:
        print("Invalid Username given")
        return False 
    else:
        df = df.loc[df["password"] == pwd]
        if df.empty:
            print("Invalid Password")
            return False
        else:
            print("Username and Password matched successfully")
            return True


def showMenu() :
    print("----------------------------------------------------------------------------")
    print("                  NATIONAL DIGITAL LIBRARY ASSOCIATION                      ")
    print("----------------------------------------------------------------------------")
    print("Press 1 - Add a New Book")
    print("Press 2 - Search for a Book")
    print("Press 3 - Delete a Book")
    print("Press 4 - Show All Books")
    print("Press 5 - Add a New Member")
    print("Press 6 - Search for a Member")
    print("Press 7 - Delete a Member")
    print("Press 8 - Show All Members")
    print("Press 9 - Issue a Book")
    print("Press 10 - Return a Book")
    print("Press 11 - Show All Issued Books")
    print("Press 12 - Delete a Issued Book")
    print("Press 13 - To view Charts")
    print("Press 14 - To Exit")
    choice = int(input("Enter your choice : "))
    return choice
if Login() :
    while True:
        ch = showMenu()
        if ch == 1:
            AddNewBook()
        elif ch == 2:
            SearchBook()
        elif ch == 3:
            DeleteBook()
        elif ch == 4:
            ShowBooks()
        elif ch == 5:
            AddNewMember()
        elif ch == 6:
            SearchMember()
        elif ch == 7:
            DeleteMember()
        elif ch == 8:
            ShowMembers()
        elif ch == 9:
            IssueBooks()
        elif ch == 10:
            ReturnBooks()
        elif ch == 11:
            ShowIssuedBooks()
        elif ch == 12:
            DeleteIssuedBooks()
        elif ch == 13:
            ShowCharts()
        
        elif ch == 14:
            break
        else:
            print("Invalid OPeration Selected")

print("THANK YOU FOR VISTING THE LIBRARY")

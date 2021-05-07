from __future__ import print_function
import os   #os module imported
import time   #time module imported
import front_page   
import login    #login imported
import book_detail_input
import Search_book
import Show_all_book
import check_stock   ###3
import buy_book
import about
front_page.front_page()
login_tell=False
while not login_tell:    # loop regarding the logins
    login_tell=login.login()
choice=0
while choice!=8:
    while True:    #loop for the user choice
        choose=raw_input(""" Enter option to continue:-->
1.Enter new book details.--
2.Show all books.--
3.Search for Book--.
4.Buy books---
5.Update Stock of any book using ISBN of the book--
6.Change user password--
7.About
8.Exit!!!  
""")    #try block used...
        try:
            int_choose=int(choose)
            if int_choose in range(9):
                choice=int_choose
                break
            else:
                print ("OPPSS!!!>>Enter digit between 1 to 8")
            
        except:    #except block begins
            print ("""OPPPSS!!!! Wrong input!!!
    PLEASE Enter a valid value between 1 and 8...!""")
            choose=input(""" Enter option to continue:-->
1.Enter new book details.>>
2.Show all  the Books.>>
3.Search for Books.>>
4.Buy books>>
5.Update stock of any book using ISBN of the given book>>
6.Change user password>>
7.About
8>Exit
""")   
    if choice==1:
        print ("Enter PASSWORD to add book>>>")
        login_tell=False
        while not login_tell:
            login_tell=login.login()
        bookstore=open("book details.txt","a+")
        book_detail_input.inputbook(bookstore)
        bookstore.close()
    elif choice==2:
        bookstore=open("book details.txt","r")
        Show_all_book.show_book(bookstore)  #showing all book details
        bookstore.close()
    elif choice==3:
        bookstore=open("book details.txt","r")
        while True:     #loop to ask for generation of query again..
            Search_book.search_book().booksearch(bookstore)
            print ("Do you want to generate again the search query(y/n!!!)")
            choice=raw_input()
            if choice.capitalize()=="Y":
                continue
            else:
                break
        bookstore.close()
    elif choice==4:    #condition for book buying.
        bookstore=open("book details.txt","r")
        print ("Hello!!! Welcome to purchase book..")
        buy_book.search_query(bookstore)
        cart=buy_book.search_and_add_book(bookstore)
        buy_book.display_cart(cart)
        buy_book.edit_cart(cart)
        buy_book.price_list(cart,bookstore)
        bookstore.close()
        bookstore=open("book details.txt","a+")
        buy_book.pur_update_stock(cart,bookstore)
    elif choice==5:
        login_tell=False    # enter the password for updating the stocks
        while not login_tell:
            print ("Enter PASSWORD to update stock!!!!")
            login_tell=login.login()
        ISBN=(raw_input("ENTER ISBN OF BOOK('TYPE-->I0000')-->>"))                    
        while len(ISBN)!=5 :   #checking for the valid isbn
            ISBN=raw_input(" <PLEASE ENTER CORRECT ISBN OF THE BOOK-->")
        new_stock=input("<<<Enter New Stock Of Book>>")
        check_stock.update_stock(ISBN,new_stock)
    elif choice==6:
        login.editpassword()   #again for editing the password
    elif choice==7:
        about.about()
        raw_input()
    elif choice==8:   # messaging for using the program
        print("****Thank you for using amazzing book store****")
        print ("""                                         \|||/                                            
             .-.________                 (o o)                  ________.-.                    
         ----/ \_)_______)  +-oooO--------(_)--------------+  (_______(_/ \----               
         (    ()___)          |     Please Visit Us At:     |       (___()     )                  
              ()__)           |                             |        (__()                        
       ----\___()_)           |     AMAZZING BOOK STORE     |        (_()___/----                
                            +---------------Ooo------------+                                  
""")
        raw_input()
        break   #breaking statement....

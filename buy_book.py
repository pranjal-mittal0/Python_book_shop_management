from __future__ import print_function
#print ("Hello!!! Welcome to purchase book")
import Search_book   #search_book imported
import check_stock    #check stock imported
import book_detail_input
def search_query(file_handler):  #search_query begins
    while True:
        Search_book.search_book().booksearch(file_handler)
        print ("***Do you want to generate again the search query(y/n)***")
        choice=raw_input()
        if choice.capitalize()=="Y":
            continue
        else:
            break

def search_and_add_book(f):    #search_and_add_book function begin
    cart={}
    while True:
        ISBN=(raw_input("ENTER ISBN OF BOOK FROM  ABOVE SEARCH RESULT('TYPE-->I0000')-->>"))                    
        while len(ISBN)!=5 :
            ISBN=raw_input(" <<<PLEASE ENTER CORRECT ISBN OF THE BOOK-->")
        ISBN=ISBN.capitalize()
        required_stock=input("--Enter the amount of book to buy--")
        if check_stock.check_stock(ISBN,required_stock,f):
            print ("Adding the book to cart....")   #book added to cart
            cart[ISBN]=required_stock
            print ("Item added:")
            print ("Do you want to shop more.?(Y/n)")
            choice=raw_input()
            if choice.capitalize()=="Y":  #capitalize function used
                continue
            else:
                break
        else:
            continue
    return cart
def display_cart(cart):
    print ("So you have :",len(cart),"book to buy.And they are:")
    for book in cart:
        print ("ISBN:-->",book,"Amount:-->",cart[book])
def edit_cart(cart):  #edit_cart function begins
    f1=open("book details.txt","a+")
    while True:
        print ("Do u want to edit your cart..?(y/n)")
        choice=raw_input().capitalize()
        if choice=="Y":
            print ("""1.Remove book.
2.Add book.
3.Change book required amount.""")
            choice1=input()
            if choice1==1:
                ISBN=raw_input("Enter the ISBN of book you want to delete...")
                cart.pop(ISBN , 'The given Book is not present in your cart>>')#command not working ...if passed -ent book then no responce...
                display_cart(cart)
            elif choice1==2 or choice1==3:
                print ("Do you want to search book?(y/n)")
                choice2=raw_input().capitalize()  #asking user choices
                if choice2=="Y":
                    search_query(f1)
                else:
                    search_and_add_book(f1)
                display_cart(cart)
            else:
                continue
        else:
            print ("So your final cart is:")
            for book in cart:
                print ("ISBN:-->",book,"Amount:-->",cart[book])
            break
def price_list(cart,file_handler):
    if len(cart)==0:
        print ("No book in the cart is Present,Hence the Net price is 0.0 Rs.>>")
        return None
    want_book=cart.keys()
    price=0
    file_handler.seek(0,0)
    store=file_handler.readlines()
    print ("The final details of book(s) in cart is/are as follows:")
    for book in store:
        bookdetails=book.split(',')
        for req_ISBN in range(len(want_book)):
            if bookdetails[0]==want_book[req_ISBN]:
                price+=int(bookdetails[4])*int(cart[want_book[req_ISBN]])
                print("ISBN-->",bookdetails[0],"   TITLE-->",bookdetails[1],"  AUTHOR-->",bookdetails[2],"    PUBLISHER-->",bookdetails[3],"  CATEGORY-->",bookdetails[5],"   PRICE-->",bookdetails[4]
                      )
    print('....\n....\n....\n....\n',"THE GRAND TOTAL IS :",price)
    return price

def pur_update_stock(cart,file_read):   #update stock function begins
    bought_book=cart.keys()
    file_read.seek(0,0)   #seek function used
    store=file_read.readlines()
    file_read.close()
    for book in store:     
        bookdetails=book.split(',')
        for bought_ISBN in range(len(bought_book)):
            if bookdetails[0]==bought_book[bought_ISBN]:
                new_stock=str(int(bookdetails[6])-int(cart[bookdetails[0]]))
                check_stock.update_stock(bookdetails[0],new_stock)


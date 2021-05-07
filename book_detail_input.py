# {{PROGRAM FOR BOOK SHOP.}}
#{{{ PROGRAMMERS-- PRANJAL,PRAKHAR,AMAAN,SANIDHYA}}}

# PROGRAM BEGINS.....>>>>

from __future__ import print_function
def checkbook(ISBN,TITLE,file_handler):   # 1ST FUNCTION BEGIN
    file_handler.seek(0,0)
    store=file_handler.readlines()                
    for book in store:
        bookdetails=book.split(',')
        check_ISBN=bookdetails[0]==ISBN.capitalize()
        check_TITLE=bookdetails[1].upper()==TITLE.upper()
        if  check_ISBN: #problem bookdetails[0]==ISBN.capitalize()or bookdetails[1].upper()==TITLE.upper() of this is that if 1 st is true then no further evaluation happen i.e 2nd condn not evaluated.therefore we use nested loop
                               #IF BOOK IS PRESENT IT WILL RETURN TRUE(BOOLEAN OUTPUT,VALUE=1)
            print ("The given ISBN already exixts in database. Please try another...")
            return True
        elif check_TITLE:
            print ("The given TITLE already exists...Please try another")
            return True
        elif bookdetails[0]!=ISBN.capitalize() and bookdetails[1].upper()!=TITLE.upper() :                                           
            tell=False  #IF BOOK  IS NOT PRESENT IT WILL RETURN FALSE(BOOLEAN VALUE=0)
    return tell

# DESCRIPTION OF THE FUNCTION USED ARE AS FOLLOWS....
  # 1.tell -- it tells about current position of file pointer.. 
  # 2.seek -- it points the file pointer on the desired location..



# 2ND FUNCTION
     
def inputbook(file_handler):   # INPUTBOOK FUNCTION BEGINS,  
    while True:                # BELOW DEMANDS THE DETAILS OF THE BOOK                               

        print ("PLEASE ENTER THE BOOK DETAILS....>>")                   

        ISBN=(raw_input("ENTER ISBN OF BOOK('TYPE-->I0000')-->>"))                    
        while len(ISBN)!=5 :
          ISBN=raw_input(" <PLEASE ENTER CORRECT ISBN OF THE BOOK-->")        

        TITLE=(raw_input("ENTER THE TITLE OF BOOK-->>"))
        while len(TITLE)==0 :
          TITLE=raw_input(" PLEASE ENTER CORRECT TITLE OF THE BOOK-->")

        if checkbook(ISBN,TITLE,file_handler):       #ASK TO CHECKBOOK THAT WHETHER THE ENTERED DETAILS ARE                    

            #print ("THE BOOK WITH SAME TITLE OR ISBN IS ALREADY PRESENT!!!")     #ALREADY PRESENT OR NOT.             

            print ("PLEASE ENTER AGAIN THE BOOK DETAILS-->>")                 

        else:                        
            break                       

    ISBN=ISBN.capitalize()
    Author=raw_input("<PLEASE ENTER AUTHOR NAME OF THE BOOK-->")  #INPUTING AUTHOR NAME. 
    
    while Author.isalpha()!=1:
        Author=raw_input(" PLEASE ENTER CORRECT AUTHOR NAME OF THE BOOK-->")
    Price=(raw_input("ENTER THE PRICE OF THE BOOK--"))                    #ENTERING PRICE OF BOOK.                   
    Price_tell=True
    while Price_tell:
        try:
            int_Price=int(Price)
            while int_Price==0:
                print ("Price of book can not be zero!!")
                Price=(raw_input("ENTER THE CORRECT PRICE OF THE BOOK--"))
                int_Price=int(Price)

        except:
            print ("Input a valid value::")
            Price=(raw_input("ENTER THE CORRECT PRICE OF THE BOOK--"))                       

        else:
            Price_tell=False
    Publisher=(raw_input("ENTER THE PUBLISHER NAME OF THE BOOK-->"))    # INPUT THE BOOK PUBLISHER NAME.                                      
    while Publisher.isalpha()!=1 :
        Publisher=raw_input("ENTER THE PUBLISHER'S CORRECT NAME OF THE BOOK-->")
    
    No_of_stock=(raw_input("ENTER THE STOCKS OF THE BOOK-->"))          #ENTERING THE STOCKS OF BOOK.
    No_of_stock_tell=True
    while No_of_stock_tell :
        try:
            int_No_of_stock=int(No_of_stock)
            while int_No_of_stock<10:
                print ("THE STOCK CAN NOT BE LESS THAN 10!!!")
                No_of_stock=(raw_input("ENTER THE CORRECT STOCKS OF THE BOOK-->"))
                int_No_of_stock=int(No_of_stock)
        except:
            print ("Input a valid value")
            No_of_stock=(raw_input("ENTER THE CORRECT STOCKS OF THE BOOK-->"))
        else:
            No_of_stock_tell=False

    Category=(raw_input("ENTER THE CATEGORIES OF THE BOOK>>"))      # ENTERING CATEGORY TYPE BOOK NEEDED.
    while Category.isalpha()!=1 :
        Category=raw_input("<ENTER THE  Categories OF THE BOOK>")
    print(ISBN,TITLE,Author,Publisher,Price,Category,No_of_stock,sep=',',end='\n',file=file_handler)

    file_handler.flush()    #EMPTY ALL BUFFER MEMORY SO THAT NEW DATA CAN BE ADDED INTO FILE.    
                          

# variable description
# 1.author-- it inputs the author name,, it should be string type value..
# 2.price -- it inputs the price of the book,, it should be integer type
# 3.subject--it inputs the category of the book,, STRING type..


       
#______-----_______-----MAIN-----____-----_____



# VARIABLE DESCIPTION
 #1.choose-- it is a string type, used for further books needed..

from __future__ import print_function
import book_detail_input    
import os    #os module imported
def check_stock(ISBN,required_stock,file_handler):   #check_stock function begins
    file_handler.seek(0,0)    #seek function used which places  pointer at specified location.
    store=file_handler.readlines()  
    for book in store:   # for loop till store as its range.
        bookdetails=book.split(',')
        if bookdetails[0]==ISBN:      #if condition for checking books in stock or not...
            if int(bookdetails[6].rstrip("\n"))>=required_stock:
                return True
            else:
                print ("SORRY!!! THE REQUIRED BOOK IS OUT OF STOCK..")  #printing message book not found
                return False
                
def update_stock(ISBN,new_stock):   #update_stock function begins
    file_handler=open("book details.txt","a+")  #book details.txt opened in append module.
    temp=open("temp.txt",'w+')   #temp.txt file also opened
    file_handler.seek(0,0)  #seek function used
    store=file_handler.readlines()
    tell=True
    for book in store:
        bookdetails=book.split(',')
        if bookdetails[0]==ISBN:   #condition check
            print (bookdetails[0],bookdetails[1],bookdetails[2],bookdetails[3],bookdetails[4]
                   ,bookdetails[5],str(new_stock),sep=',',end='\n',file=temp)
            file_handler.flush()  #flush -forces data to store before file execution..
            tell=False
        else:
            print (bookdetails[0],bookdetails[1],bookdetails[2],bookdetails[3],bookdetails[4]
                   ,bookdetails[5],bookdetails[6],sep=',',end="",file=temp)
            file_handler.flush()
    if tell==True:
        print ("OPPPSS!!!!The provided ISBN no. is not valid")   #THE ISBN WAS NOT FINE.
        print ("Do you want to enter new BOOK data(Y/N)") 
        choice=raw_input()   #CHOICE INPUTTING
        if choice.capitalize()=='Y':
            file_handler.seek(0,2)   #SEEKING FILE POINTER AT SPECIFIED LOCATION..
            book_detail_input.inputbook(file_handler)
    elif tell==False:
        file_handler.close()
        temp.close()
        os.remove("book details.txt")   #remove function used to remove a file
        os.rename("temp.txt","book details.txt")   #rename used to rename a given file.
        #print ("The data is sucessfully updated....")   #Data updated....

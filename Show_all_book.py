from __future__ import print_function
def show_book(file_handler):
    file_handler.seek(0,0)   #seek function put the location of the file pointer as required.                         
    store=file_handler.readlines()                  
    for book in store:                            
        bookdetails=book.split(',')
        print ("ISBN-->",bookdetails[0],"   TITLE-->",bookdetails[1],"  AUTHOR-->",bookdetails[2],"    PUBLISHER-->",bookdetails[3],"   PRICE-->",bookdetails[4]
                ,"  CATEGORY-->",bookdetails[5],"    AMOUNT IN STOCK-->",bookdetails[6],sep="")

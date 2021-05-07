from __future__ import print_function
class search_book():
    def __init__(self):
        pass
    def input_choice(self):
        while True:
            choose=raw_input('''
want to search book by
1-->Title
2-->Author
3-->ISBN
4-->Publisher
5-->Category
6-->Price
7-->Exit
PLEASE ENTER YOUR CHOICE-->
''')
            try:
                int_choose=int(choose)
                if int_choose in range(8):
                    return int_choose
                else:
                    print ("OPPSS!!!>>Enter digit between 1 to 7")
        
            except:
                print ("""OPPPSS!!!! Wrong input!!!
PLEASE Enter a valid value between 1 and 7...""")
                choose=input('''
want to search book by
1-->Title
2-->Author name
3-->ISBN no
4-->Publisher name
5-->Category of the book
6-->Price of book
7-->Exit 
PLEASE ENTER YOUR CHOICE-->
''')
        
    def booksearch(self,file_handler):     #booksearch function begins....
        print ("Welcome to search module:")
        while True:
            choose=self.input_choice() 
            if choose == 1:      #if condition statement..
                Title=raw_input("<<Enter Title of book>>")     # input title for searching book    
                file_handler.seek(0,0)   #seek function put the location of the file pointer as required.                         
                store=file_handler.readlines()                  
                for book in store:                            
                    bookdetails=book.split(',')      #split function used..       
                    if bookdetails[1].upper()==Title.upper():                  #condition check for finding entered detail.               
                        print ("UR book is found")                     
                        print ("ISBN-->",bookdetails[0],'\n',
                               "Title-->",bookdetails[1],'\n',
                               "Author-->",bookdetails[2],'\n',
                               "Publisher-->",bookdetails[3],'\n',
                               "Price-->",bookdetails[4],'\n',
                               "Category-->",bookdetails[5],'\n',
                               "No in stock-->",bookdetails[6],'\n')
                        raw_input("PRESS ENTER TO CONTINUE")
            elif choose == 2:
                Author=raw_input("Enter Author of book---")   #enter author name.
                file_handler.seek(0,0)  #AGAIN SEEK FUNCTION USED...                          
                store=file_handler.readlines()       #SEEK-it specifies the position of file pointer.          
                for book in store:                         # for loop begins for store..     
                    bookdetails=book.split(',')                
                    if bookdetails[2].upper()==Author.upper():      # condition check for match founding                    
                        print ("UR book is found")                           
                        print ("ISBN-->",bookdetails[0],'\n',
                                "Title-->",bookdetails[1],'\n',
                                "Author-->",bookdetails[2],'\n',      # PRINTING STATEMENTS!!!!!!
                                "Publisher-->",bookdetails[3],'\n',
                                "Price-->",bookdetails[4],'\n',
                                "Category-->",bookdetails[5],'\n',
                                "No in stock-->",bookdetails[6],'\n')
                        raw_input("PRESS ENTER TO CONTINUE...")
            elif choose == 3:      # CONDITION CHECK STATEMENT.
                ISBN=raw_input("Enter ISBN of book") # ENTER ISBN FOR SEARCHING THROUGH ISBN..
                file_handler.seek(0,0)   #pointing file pointer at begining with forward move of pointer..
                store=file_handler.readlines()                  
                for book in store:                             
                    bookdetails=book.split(',')                 
                    if bookdetails[0]==ISBN.upper():                                 
                        print ("your book is found")                        
                        print ("ISBN-->",bookdetails[0],'\n',
                                "Title-->",bookdetails[1],'\n',
                                "Author-->",bookdetails[2],'\n',
                                "Publisher-->",bookdetails[3],'\n',     #printing statements giving all details since
                              # match found     
                                "Price-->",bookdetails[4],'\n',
                                "Category-->",bookdetails[5],'\n',
                                "No in stock-->",bookdetails[6],'\n')
                        raw_input("PRESS ENTER TO CONTINUE>>>")
            elif choose == 4:
                Publisher=raw_input("Enter Publisher of book--")     #ENTER PUBLISHER FOR SEARCHING BY PUBLISHER NAME
                file_handler.seek(0,0)                            
                store=file_handler.readlines()                
                for book in store:                            
                    bookdetails=book.split(',')               #split() is used..
                    if bookdetails[3].upper()==Publisher.upper():                                 
                        print ("YOUR BOOK IS FOUND!!")                          
                        print ("ISBN-->",bookdetails[0],'\n',
                                "Title-->",bookdetails[1],'\n',
                                "Author-->",bookdetails[2],'\n',
                                "Publisher-->",bookdetails[3],'\n',
                                "Price-->",bookdetails[4],'\n',
                                "Category-->",bookdetails[5],'\n',
                                "No in stock-->",bookdetails[6],'\n')          #PRINTING STATEMENT...
                        raw_input("PRESS ENTER TO CONTINUE>>")
            elif choose == 5:
                Category=raw_input("Enter Category of book>>")
                file_handler.seek(0,0)                            
                store=file_handler.readlines()                 
                for book in store:                          # for loop with store as limit..  
                    bookdetails=book.split(',')                
                    if bookdetails[5].upper()==Category.upper():    # statement for match(category wise)         
                        print ("YOUR book is found")                        
                        print ("ISBN-->",bookdetails[0],'\n',
                                "Title-->",bookdetails[1],'\n',
                                "Author-->",bookdetails[2],'\n',
                                "Publisher-->",bookdetails[3],'\n',
                                "Price-->",bookdetails[4],'\n',
                                "Category-->",bookdetails[5],'\n',
                                "No in stock-->",bookdetails[6],'\n')
                        raw_input("PRESS ENTER TO CONTINUE")
            elif choose == 6:
                print("Please enter price range>>")
                upper_limit=input("Enter Upper limit of price range(inclusive)--")    #####
                lower_limit=input("Enter lower limit of price range(inclusive)--")      #DECIDING THE PRICE LIMITS
                file_handler.seek(0,0)                           
                store=file_handler.readlines()            
                for book in store:                              
                    bookdetails=book.split(',')            
                    if int(bookdetails[4]) in range(upper_limit,lower_limit + 1): # conditional statement ranging b/w                                  
                        print ("UR book is found")                          #upper and lower limit..
                        print ("ISBN-->",bookdetails[0],'\n',
                                "Title-->",bookdetails[1],'\n',
                                "Author-->",bookdetails[2],'\n',
                                "Publisher-->",bookdetails[3],'\n',
                                "Price-->",bookdetails[4],'\n',
                                "Category-->",bookdetails[5],'\n',
                                "No in stock-->",bookdetails[6],'\n')
                        raw_input("PRESS ENTER TO CONTINUE---")
            elif choose==7:
                break
        
      

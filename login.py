import time   #time module imported
import os   #os module imported
def login():   #login function begins
    fpass=open("password.txt")    # file name "password.txt" opened. 
    password=fpass.read()
    trialpassword=raw_input("enter password to continue>>>")  #enter password to enter
    if(password==trialpassword):   #condition check matching password.
        print("Analysing entered password>>>")
        print ("PLEASE WAIT....")
        time.sleep(5)    #delays the given program for 5 sec
        print("Access Granted")
        print("Thank you for the confirmation")
        fpass.close()   #closing the file named password.txt
        return True
    elif (password!=trialpassword):   #again matching the conditions
        print("ANALYSING ENTERED PASSWORD>>>")
        print ("PLEASE WAIT")
        time.sleep(3)    #delaying... the program
        print("ACCESS DENIED!!!")
        fpass.close()
        return False
        

def editpassword():    #editpassword function begins.
    fpass=open("password.txt") #password.txt file opened.
    oldpassword=fpass.read()
    print ("Enter old password to continue-->")
    old_password_check=raw_input()
    if oldpassword==old_password_check:
        fpass.seek(0,0)
        newpassword=raw_input("Enter new password--->")#enter the new password
        temp=open("temp.txt",'w+')
        temp.write(newpassword)   #writing the new password on the file.
        fpass.close()  #file closed
        os.remove("password.txt")   #removing the password.txt file
        temp.close()   #closing the temp file
        os.rename("temp.txt","password.txt")#renamed the temp.txt by password.txt 

        return True
    else:
        print ("Enter correct password..!!Wrong password entered--->")
        fpass.close()
        return False
                          


#####LOGIN MODULE ENDS>>>>>
    
            

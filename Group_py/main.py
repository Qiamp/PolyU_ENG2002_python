from account import User_Login
from caculation import ratNum
import os
while True:
    account_result=User_Login('','',0)    #Instantiate the login class
    selcet=input('\na) log in \nb) sign up \nc)exit \nPlease select the operation you want:')

    if selcet=='a':   #First level menu
        account_result.login()  #call the login function
        if account_result.flag==1:  #Enter the program when the login status is 1
            while True:
                ratNum_result=ratNum(0,0,0,0,0)   #Instantiate the ratNum class
                selcet=input('\na) Perform multiplication calculations \nb) perform power calculations \nc)exit \nPlease select the operation you want:')   #Secondary Menu
                if selcet=='a':
                    ratNum_result.product() #call the product function
                elif selcet=='b':
                    ratNum_result.power()   #call the power function
                elif selcet=='c':
                    print("Program Exit")
                    os._exit(1)
                
    elif selcet=='b':
        account_result.signup()    #call the signup function
    elif selcet=='c':
        print("Program Exit")
        os._exit(1) 
import os
class User_Login:
    def __init__(self,username,password,flag):
        self.username=username
        self.password=password
        self.flag=flag

    def login(self):
        self.flag=0  #Initialize the login status
        while self.flag==0:
            read=open('user.txt') #Read user information
            all_0=read.read()
            all_1=all_0.replace('\n',' ')    # replaces the newline character in the document with the space ' '
            all_2= all_1.split(' ')
            wrongtime=0   #Initialize the Number of failures
            self.username=input('\nInput your username:') 
            for line in all_2:   #Traverse the user information in the database is traversed
                all_3=line.split(':')
                if all_3[0]==self.username:  #Correct username
                    self.password=input('\nInput your password:')
                    if self.password == all_3[1]:
                        self.flag=1   #The login status changes from 1 to 0, indicating that the user logs in successfully
                        break
                    else:
                        print('wrong password')
                        wrongtime+=1  #Number of failures plus one
                        if wrongtime==2:  #If the password is entered more than three times, the program will exit automatically
                            self.flag=0
                            print('System exit')
                            os._exit(1)
                if all_2.index(line) == len(all_2)-1:    #Check whether all user information has been traversed. If no user information is found, the user does not exist
                    print("\nWrong usernmae")
                    selcet=input('\na) log in \nb) sign up \nc)exit \nPlease select the operation you want:')
                    if selcet=='a':   #Enter the login link
                        break
                    elif selcet=='b':  #Register again
                        temp=User_Login('','',0)
                        temp.signup()
                        print('\nPlease log in again')
                        break
                    elif selcet=='c':  #exit
                        os._exit(1)



                

    def signup(self):
        self.username=input('Input your username:')
        self.password=input('Input your password:')
        file=open('user.txt',mode='a')
        file.write('\n'+self.username+':'+self.password)
        file.close()      
        

            


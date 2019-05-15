import datetime
t=datetime.datetime.today()
from Modules_Packages.aadhar_project import readbank as rb 
def login(bank):
    sentence1="WELCOME TO {0} BANKING LOGIN SYSTEM"
    sentence2=sentence1.format(bank)
    print(sentence2 + '                ' + str(t))
    print("------------------------------------------------------------------------")
    id=input("enter your customer id: ")
    pwd=input("enter your password: ")
    rb.bank(id,pwd,bank).readbankdb()
    return
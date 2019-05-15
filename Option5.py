from Modules_Packages.aadhar_project import bank as b 
def func():
    print("CHOOSE FROM BELOW SET OF BANKS FOR E-VERIFY ")
    opt=int(input("1.HDFC 2.ICICI 3.SYND "))
    if opt==1:
        b.login('HDFC') 
    elif opt==2:
        b.login('ICICI')
    elif opt==3:
        b.login('SYNDICATE')
    else:
        print("option not valid")
    return

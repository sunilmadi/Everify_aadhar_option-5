from pymongo import MongoClient
from Modules_Packages.aadhar_project import otpcheck as otpt,smsekyc as skyc,emailekyc as ekyc
class bank:
    def __init__(self,id,pwd,bank):
        self.id=id
        self.pwd=pwd
        self.bank=bank
    def readbankdb(self):
        flagpwd='N'
        client=MongoClient('localhost',27017)
        db=client['AADHAR']
        HDFC=db['HDFC ']
        result=HDFC.find_one({'CUSTID':self.id})
        if result is None:
            print("CUSTOMER ID NOT IN BANK DATABASE.CHECK WITH YOUR RESPECTIVE BANK/BRANCH")
        else:
            for i,j in result.items():
                if i=="DETAILS" and j['PWD']==self.pwd:
                    print("User login successful")
                    flagpwd='Y'
                    paadhari=input("ENTER YOUR AADHAR NUMBER REGISTERED WITH BANK :")
                    if int(paadhari)== int(j['AADHAR']) and j['EKYC']=='N' and j['BANK']==self.bank:
                        eky=self.ekyc(int(paadhari),HDFC)
                    else:
                        print("INVALID AADHAR NUMBER OR E-KYC ALREADY COMPLETED FOR THIS OR MISMATCH IN REGISTERED BANK.CHECK WITH YOUR RESPECTIVE BANK/BRANCH OFFLINE TO CORRECT THE DETAILS")
            if flagpwd!='Y':
                print("Incorrect password entered")
        return
    def ekyc(self,aadharnum,HDFC):
        rt=otpt.otpcheck()
        if rt==1:
            result=HDFC.update_one({'CUSTID':self.id},{'$set':{'DETAILS.EKYC':'Y'}})
            skyc.sendsms(aadharnum,self.bank)
            email1=input("enter your email :")
            ekyc.emailfunc(email1,aadharnum,self.bank)               
        else:
            print("invalid OTP or time out")
        return



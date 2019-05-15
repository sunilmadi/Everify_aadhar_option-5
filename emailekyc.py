from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import datetime as dt
from reportlab.pdfgen import canvas
def emailfunc(email,aadhar,bank):
    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        username="sunil.kumarmadikesari@gmail.com"
        password="littlerock"
        server.login(username,password)
        msg=MIMEMultipart()
        msg['From']=username
        msg['To']=email
        msg['Subject']="WELCOME TO AADHAR SYSTEM- E-VERIFICATION"
        body1="Your e-verification is complete for aadhar number : '{0}' by {1} bank at {2}"
        body=body1.format(aadhar,bank,dt.datetime.today())
        msg.attach(MIMEText(body))
        file_name=str('aadhar_')+ str(aadhar)  + '.pdf'
        path="E:/Project/Modules_Packages/aadhar_project/PDF/{0}"
        path1=path.format(file_name)
        c=canvas.Canvas(path1)
        c.drawCentredString(400,600,"AADHAR INDIA LIMITED")
        c.drawCentredString(310,350,body)
        c.drawCentredString(330,300,"E-Verified by bank: ")
        c.drawCentredString(450,300,bank)
        c.save()
        with open(path1,"rb") as f:
            part=MIMEApplication(f.read())
            part.add_header('Content-Disposition', 'attachment', filename=file_name)
            msg.attach(part)
            f.close()
        server.sendmail(msg['From'], msg['To'], msg.as_string())
    except:
        print("Email connection interupted.But you e-verification processing is complete without email notification.")
    finally:
        print("Your e-verification processing is complete.")
    

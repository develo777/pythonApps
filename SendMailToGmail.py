import os
import smtplib

titulo="titulo mensaje"
isEnvidado=False
db_user='charlydeveloper@gmail.com'
db_pass=os.getenv('DB_Karloz')


with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(db_user,db_pass)

    subject ='grab dinner this week'
    body ='test desde python'

    msg=f'subject: {subject}\n\n{body}'

    smtp.sendmail(db_user,'cesquen@barredamoller.com',msg)


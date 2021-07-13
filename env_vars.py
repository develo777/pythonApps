import os 
import smtplib
from  datetime import date, datetime
db_user='charlydeveloper@gmail.com'
db_pass=os.environ.get('DB_Karloz')


today=date.today()
print(today)
now =datetime.now()
print(now.strftime("%H%M%S"))
#print(db_user)
#print(db_pass)
"""This module will send me an email when someone wants to contact me
        to this email: skyproject.au@gmail.com"""
import smtplib
import datetime as dt

## datetime##

now = dt.datetime.now()
day = now.today()
qe=now.weekday()

my_email = 'franciscoeliasm@yahoo.com'
password = 'effqekbwkunhjbfe'
class SendEmail():
        def send(self, name, email, telephone, message):
                with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                        connection.starttls()
                        connection.login(user=my_email, password=password)
                        connection.sendmail(
                        from_addr=my_email,
                        to_addrs='skyproject.au@gmail.com',
                        msg=f'Subject: Job email from{name} \n\n Email from: {name}, the {day} at {now}\n messsage: {message},\n email: {email},'
                            f'\n telephone: {telephone}')

import smtplib
import datetime

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from debug.debug import log_error

from .accesses import MAIL, PASSWORD

# 0 -> новый пользователь
# 1 -> новая заявка


@log_error
def send(subject, username, user_id, body):
    login = MAIL
    password = PASSWORD

    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = login

    if subject == 0:
        msg['Subject'] = f'{username} новый пользователь ВК бота'
        body = body
    elif subject == 1:
        msg['Subject'] = f'{username} оставил заявку у ВК бота'
        body = body

    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.set_debuglevel(True) #вывод в консоль отчета
    server.starttls()
    date = datetime.datetime.today()
    server.login(login, password)
    print("Отправка письма...")
    server.send_message(msg)
    server.quit()
    print('\x1b[6;30;42m' + 'Email successfully sent' + '\x1b[0m')

import smtplib, ssl
import ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = 'dev.tiwary5821@gmail.com'
    password = "ohcmvrauwpgbirdi"

    receiver = 'dev.tiwary0014@gmail.com'
    my_context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
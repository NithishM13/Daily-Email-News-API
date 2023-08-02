import smtplib
import ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "nithishm1326@gmail.com"
    password = "auyftmodqfrvlxwu"

    context = ssl.create_default_context()

    receiver = "nithishm1326@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
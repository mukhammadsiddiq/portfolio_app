import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "ibrohimovmuhammad2020@gmail.com"
password = "iqddeeefrnzeziux"

receiver = "ibrohimovmuhammad2020@gmail.com"
context = ssl.create_default_context()

message = """
Hi!
"""


with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)


import smtplib
import os
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from datetime import datetime

GMAIL_PASSWORD = os.environ["GMAIL_PASSWORD"]


def send_mail(send_from, send_to, subject, text, files=None, username=None, password=None,
              server="127.0.0.1"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


def main():
    current_date = datetime.now().date()

    send_from = "vijay.sai005@gmail.com"
    send_to = ["vijay.sai005@yahoo.com"]
    subject = "Regd: Notification for Expense Update | {}".format(current_date)

    message = "\nHi Vijay,\n\nRefer link " \
              "http://localhost:5050/data to " \
              "insert/update data related to today's expenses. \n\nDate: {}" \
              "\n\nRegards \n" \
              "Vijayasai S".format(current_date)
    files = []
    username = send_from
    password = GMAIL_PASSWORD
    send_mail(send_from=send_from, send_to=send_to, subject=subject,
              text=message, files=files, username=username,
              password=password, server="smtp.gmail.com:587")
    return


if __name__ == "__main__":
    main()
import smtplib
import os
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from datetime import datetime
from SendSMS import send_sms


GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD", "V1j@y@$@1")


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
    current_month = current_date.strftime("%B")

    send_from = "vijay.sai005@yahoo.com"
    send_to = ["vijay.sai005@gmail.com"]
    subject = "Regd: Monthly Expense Analysis - {}".format(current_month)

    message = "\nHi Vijay, \n\nPlease find the attached file for {} month expense analysis. \n\nRefer link " \
              "http://35.200.253.224:5000/data to " \
              "insert/update data. \n\nDate: {}" \
              "\n\nRegards \n" \
              "Vijayasai S".format(current_month, current_date)

    files = ["/tmp/log.txt"]
    # files = []
    username = send_from
    password = GMAIL_PASSWORD

    send_mail(send_from=send_from, send_to=send_to, subject=subject,
              text=message, files=files, username=username,
              password=password, server="smtp.mail.yahoo.com:587")

    push_message = "\nHi Vijay, \n\nPlease check email for {} month expense analysis. \n\nRefer link " \
              "http://35.200.253.224:5000/data to " \
              "insert/update data. \n\nDate: {}" \
              "\n\nRegards \n" \
              "Vijayasai S".format(current_month, current_date)

    send_sms(push_message)
    return


if __name__ == "__main__":
    main()
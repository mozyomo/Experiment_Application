import smtplib

def main():
    smtp_host = "smtp.gmail.com"
    smtp_port = 465
    username = "motoki619@gmail.com"
    password = "amhlkqyytekqfclx" #後で変更
    from_address = "motoki619@gmail.com"
    to_address = "motoki619@gmail.com"
    subject = "test_subject"
    body = "mail_content"
    message = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (from_address, to_address, subject, body))

    smtp = smtplib.SMTP_SSL(smtp_host, smtp_port)
    smtp.login(username, password)
    result = smtp.sendmail(from_address, to_address, message)
    print(result)

if __name__ == "__main__" :
    main()
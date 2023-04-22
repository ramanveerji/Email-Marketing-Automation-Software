import smtplib  # to deal with gmail mails


def Email_send_function(to, subject, message, uname, pasw):
    # print(to,subject,message,uname,pasw)
    s = smtplib.SMTP("smtp.gmail.com", 587)  # create session for gmail
    s.starttls()  # transport layer
    s.login(uname, pasw)
    msg = f"Subject: {subject}\n\n{message}"
    s.sendmail(uname, to, msg)
    x = s.ehlo()
    return "s" if x[0] == 250 else "f"

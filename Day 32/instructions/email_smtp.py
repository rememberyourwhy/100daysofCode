from email.message import EmailMessage
import ssl
import smtplib
# declare my_email, password

# assign connection = smtplib.smtp("smtp.gmail.com")
# starttls()
# login (username, password)
# sendmail (from_addr, to_addrs, msg)
# close connection


# email, password, receiver_password
# subject
# content
# create email message object (em)
# assign em["From"], em["To"], em["Subject"]
# em.set_content

# ssl.create_default_context
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp
    # smtp.login(email, password)
    # smtp.sendmail(email, receiver, em.as_string())

# ---------------------- CONSTANTS --------------------- #
email_sender = "phuc16052001@gmail.com"
email_password = "xmgkhwzsfppxkysp"
email_receiver = "phucsetup1@yahoo.com"

# ---------------------- MESSAGE ----------------------- #
subject = "Hello pt"
content = "How are you today?"

# ---------------------- em Object --------------------- #
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(content)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

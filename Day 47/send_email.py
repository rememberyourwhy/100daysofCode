import smtplib
from email.message import EmailMessage
import ssl


def send_mail(subject, content):
    # person_info datatype
    # {
    #     "Person_name": row.person_name,
    #     "Email": row.email,
    #     "Year": row.year,
    #     "Month": row.month,
    #     "Day": row.day
    # }
    # ---------------------- CONSTANTS --------------------- #
    email_sender = "phuc16052001@gmail.com"
    # noinspection SpellCheckingInspection
    email_password = "ixhuavoiwftuyaas"
    email_receiver = "phucsetup1@yahoo.com"

    # ---------------------- MESSAGE ----------------------- #
    # subject =
    # content =
    # %PRINT_CHECK
    # print(content)
    # print(person_name)
    # print(email_sender)
    # print(email_receiver)

    # ---------------------- em Object --------------------- #
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(content)

    # ----------------------- SMTP ------------------------- #
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())



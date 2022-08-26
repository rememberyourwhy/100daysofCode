import smtplib
import ssl
from email.message import EmailMessage
import random
import datetime as dt
import sys
import pandas

# --------------------- Extra Hard Starting Project --------------------- #

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
# Let's pretend there are multiple ppl that has the same birthday


# ------------------- DATETIME -------------------- #
# now = dt.datetime.now()
# month = now.month
# day = now.day
# list_of_birthday_people = birthday_dict.get(f"{month} {day}")
# if list_of_birthday_people is None:
#     sys.exit("No one's birthday today")


# ------------------- DATA STRUCTURE --------------- #
# we have two data:
# first one is {key=f"{month} {day}, value=[list of people that has birthday in that key day]
# second one is a list of dictionaries, each dictionary has this format:
# {"Name":name, "Email":email, "Year":year, "Month":month, "Day":day}
def first_data_structure():
    birthday_data = pandas.read_csv("birthdays.csv")
    birthday_dict = {}
    for index, row in birthday_data.iterrows():
        key = f"{row.month} {row.day}"
        new_person = row.person_name
        if key in birthday_dict:
            birthday_dict[key].append(new_person)
        else:
            birthday_dict[key] = [new_person]
    return birthday_dict


#
# def send_mail(person_info):
#     # ------------------- EMAIL_SMTP function ------------------ #
#     # ---------------------- CONSTANTS --------------------- #
#     email_sender = "phuc16052001@gmail.com"
#     email_password = "xmgkhwzsfppxkysp"
#     email_receiver = "phucsetup1@yahoo.com"
#
#     # ---------------------- MESSAGE ----------------------- #
#     message = random.choice(all_lines_dict)
#     subject = message["Origin"]
#     content = message["Quotes"]
#
#     # ---------------------- em Object --------------------- #
#     em = EmailMessage()
#     em["From"] = email_sender
#     em["To"] = email_receiver
#     em["Subject"] = subject
#     em.set_content(content)
#
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
#         smtp.login(email_sender, email_password)
#         smtp.sendmail(email_sender, email_receiver, em.as_string())
#
#
#
#

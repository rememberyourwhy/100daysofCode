from email.message import EmailMessage
import ssl
import smtplib
import datetime as dt
import sys
import random


# ------------------- DATETIME -------------------- #
now = dt.datetime.now()
day =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
now_weekday = day[now.weekday()]
if now_weekday != "Friday":
    sys.exit("Not Friday")

# ------------------- QUOTES ---------------------- #

file_name = "quotes.txt"

# use list comprehension,
# for each element of the list, rstrip them "\n" and read from file
with open(file_name, mode="r") as file:
    all_lines = [line.strip("\n") for line in file]
all_lines_dict = {}
index = 0
for line in all_lines:
    line_split = line.split(" - ")
    all_lines_dict[index] = {}
    all_lines_dict[index]["Quotes"] = line_split[0]
    all_lines_dict[index]["Origin"] = line_split[1]
    index += 1


# ------------------- EMAIL_SMTP ------------------ #
# ---------------------- CONSTANTS --------------------- #
email_sender = "phuc16052001@gmail.com"
email_password = "xmgkhwzsfppxkysp"
email_receiver = "phucsetup1@yahoo.com"

# ---------------------- MESSAGE ----------------------- #
message = random.choice(all_lines_dict)
subject = message["Origin"]
content = message["Quotes"]

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




import smtplib
import ssl
from email.message import EmailMessage
import random
import datetime as dt
import sys
import pandas
import os

# ---------------------------------- MAIN CONSTANTS ----------- #
# noinspection SpellCheckingInspection
DIRECTORY_AB_PATH = r"C:\Users\Administrator\PycharmProjects\100daysofCode\Day 32\birthday_messages\letter_templates"

# --------------------- Extra Hard Starting Project --------------------- #

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
# Let's pretend there are multiple ppl that has the same birthday

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


def second_data_structure():
    birthday_data = pandas.read_csv("birthdays.csv")
    birthday_dict = {}
    for index, row in birthday_data.iterrows():
        key = row.person_name
        birthday_dict[key] = {
            "Person_name": row.person_name,
            "Email": row.email,
            "Year": row.year,
            "Month": row.month,
            "Day": row.day
        }
    return birthday_dict


def get_all_files():
    dir_path = DIRECTORY_AB_PATH

    result = []

    for file in os.listdir(dir_path):
        if file.endswith('.txt'):
            result.append(file)
    return result


def get_a_random_letter_template(name, letter_templates):
    random_number = random.randint(0, len(letter_templates) - 1)
    letter_dir = letter_templates[random_number]
    with open(DIRECTORY_AB_PATH+"\\"+letter_dir, mode="r") as letter_file:
        letter_formatted = letter_file.read().replace("[NAME]", name)
    return letter_formatted


# ------------------- EMAIL_SMTP function ------------------ #
def send_mail(person_info):
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
    email_receiver = person_info["Email"]

    # ---------------------- MESSAGE ----------------------- #
    person_name = person_info["Person_name"]
    subject = f"To + {person_name}"
    content = get_a_random_letter_template(person_name, get_all_files())
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


# ------------------- DATETIME -------------------- #
now = dt.datetime.now()
month = now.month
day = now.day

# ------------------- MAIN ------------------------ #
data1 = first_data_structure()
data2 = second_data_structure()
list_of_birthday_people = data1.get(f"{month} {day}")
if list_of_birthday_people is None:
    sys.exit("No one's birthday today")
for birthday_person in list_of_birthday_people:
    birthday_data2 = data2[birthday_person]
    send_mail(birthday_data2)

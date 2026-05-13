import datetime as dt
import pandas as pd
import random
import smtplib
import os

# Read hidden secrets securely from GitHub
my_email = os.environ.get("MY_EMAIL")
my_pass = os.environ.get("MY_PASSWORD")

# 1. Check if today matches a birthday
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

# FIX 1: Changed local file path to relative path for GitHub
birth_data = pd.read_csv("birthdays.csv")

# Create dictionary from birthday data
birthday_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in birth_data.iterrows()
}

# FIX 2: Changed local folder paths to relative paths for GitHub template folder
letters = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]
choose_random_letter = random.choice(letters)

# 2. Process and send the email if there is a match
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    with open(choose_random_letter, mode="r") as letter:
        content = letter.read()
        final_letter = content.replace("[NAME]", birthday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        
        # FIX 3: Changed hardcoded to_addrs to use the person's email from the CSV automatically
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday {birthday_person['name']}\n\n{final_letter}"
        )

##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
LETTER = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
SMTP_LINK = "smtp.mail.yahoo.com"
EMAIL = "udemytest19@yahoo.com"
PASSWORD = "qhpdwjcubqktvgno"

birthday = pandas.read_csv("birthdays.csv")
all_details = birthday.to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day
for detail in all_details:
    if month == detail["month"] and day == detail["day"]:
        with open(f"./letter_templates/{random.choice(LETTER)}") as letter_file:
            letter_content = letter_file.read()
            new_content = letter_content.replace("[NAME]", f"{detail['name']}")
            print(new_content)
            with smtplib.SMTP(SMTP_LINK) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=detail["email"],
                    msg=f"Subject:Birthday Wishes!!\n\n{new_content}"
                )

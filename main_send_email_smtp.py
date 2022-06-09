import smtplib
import datetime as dt
from random import choice


MY_EMAIL = "udemytest19@yahoo.com"
PASSWORD = "qhpdwjcubqktvgno"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="udemytest94@gmail.com",
            msg=f"Subject:Monday Motivation\n\n {quote}"
        )

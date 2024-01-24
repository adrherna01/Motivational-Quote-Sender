# import smtplib
#
# my_email = "pruebamuster@gmail.com"
# password = "byrlaqnrzyxozrjg"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
# 	connection.starttls()
# 	connection.login(user=my_email, password=password)
# 	connection.sendmail(
# 		from_addr=my_email,
# 		to_addrs="adrianhdt.2001@gmail.com",
# 		msg="Subject:Hello\n\nThis is the body of my gmail"
# 	)

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()

import datetime as dt
import smtplib
import random

# Extracting random quote to be sent
with open("quotes.txt", "r") as data:
	text_in_lines = data.readlines()
	quote_to_send = random.choice(text_in_lines)

# Setting up connection
my_email = "pruebamuster@gmail.com"
password = "byrlaqnrzyxozrjg"

receiver = "adrianhdt.2001@gmail.com"
day_to_send = 0  # Monday
today = dt.datetime.now()

if today.weekday() == day_to_send:
	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(user=my_email, password=password)
		connection.sendmail(
			from_addr=my_email,
			to_addrs=receiver,
			msg="Subject:Motivation\n\n" + quote_to_send
		)

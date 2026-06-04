from datetime import datetime
import pandas
import random
import smtplib
import os
import pytz
from email.mime.text import MIMEText   # ✅ import MIMEText

# Secrets from GitHub Actions
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD =os.environ.get("MY_PASSWORD")

# Timezone handling
ist = pytz.timezone("Asia/Kolkata")
today = datetime.now(ist)
today_tuple = (today.month, today.day)

# Read birthdays
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (_, row) in data.iterrows()}

if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]

    # ✅ Pick one of your three letter files randomly
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path, encoding="utf-8") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person["name"])  # replace placeholder

    # ✅ Build MIMEText email
    msg = MIMEText(contents, "plain", "utf-8")
    msg["Subject"] = "Happy Birthday 🎂!"
    msg["From"] = MY_EMAIL
    msg["To"] = person["email"]

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.send_message(msg)   # ✅ send MIMEText
        print(f"✅ Email sent successfully to {person['name']} ({person['email']})")
    except Exception as e:
        print(f"❌ Email failed: {e}")
else:
    print("ℹ️ No birthdays today.")

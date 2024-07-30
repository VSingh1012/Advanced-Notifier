import customtkinter as ctk
import datetime as dt
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import smtplib, ssl
from email.message import EmailMessage
import time


class BackendWorker:

    def __init__(self, win, file: str):
        self.win = win
        self.file = file

    def update_file(self, filepath: str):
        self.file = filepath

    def __call__(self):

        def send_email_reminder(client_name, client_date, warranty_num):

            YOUR_GOOGLE_EMAIL = 'myexcelbot@gmail.com'  # The email you setup to send the email using app password
            YOUR_GOOGLE_EMAIL_APP_PASSWORD = 'wlif huof ivqq qyfg'  # The app password you generated

            smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtpserver.ehlo()
            smtpserver.login(YOUR_GOOGLE_EMAIL, YOUR_GOOGLE_EMAIL_APP_PASSWORD)

            # Test send mail
            sent_from = YOUR_GOOGLE_EMAIL
            sent_to = "smitasomne@gmail.com"  #  Send it to self (as test)
            message = f"Please alert your client so and take action as soon as possible! \n\nTheir date of service was {client_date} and it is nearing the end of their {warranty_num} year warranty!"
            subject = f"Your client, {client_name}, has a warranty that is near expiration!"

            email = EmailMessage()
            email['From'] = sent_from
            email['To'] = sent_to
            email['Subject'] = subject
            email.set_content(message)

            smtpserver.sendmail(sent_from, sent_to, email.as_string())

            # Close the connection
            smtpserver.close()

        # Back end process where data is searched and sorted in 1 or 3 year warranty based on "REPAIR" or "FITTING" status
        # of the ear equipment

        todays_date = dt.date.today()

        # todays_date = str(dt.datetime(2024, 8, 13)).split(' ')[0]

        # file = filedialog.askopenfilename()

        # Creating an instance of the dataframe for the use in the function and the new instance of the Editing Window constructor
        df = pd.read_csv(self.file)

        warranty_year_values = [0] * len(df)

        new_service_years = [0] * len(df)

        new_days = [0] * len(df)

        new_months = [0] * len(df)

        new_dates = [None] * len(df)

        all_columns = list(df.columns)

        status_rows = list(df.iloc[:len(df), all_columns.index("Status")])

        dos_rows = list(df.iloc[:len(df), all_columns.index("DOS")])

        # print(dos_rows)

        name_rows = list(df.iloc[:len(df), all_columns.index("Patient")])

        for x in range(len(status_rows)):
            if (status_rows[x].upper() == "REPAIR"):
                warranty_year_values[x] = 1
            else:
                warranty_year_values[x] = 3

            # Arranging the dates based on their location in the DOS row values

            split_dates = str(dos_rows[x]).split('/')

            # print(split_dates[1])

            new_days[x] = int(split_dates[1])

            if (int(split_dates[0]) == 1):
                new_months[x] = 11
            elif (int(split_dates[0]) == 2):

                new_months[x] = 12
            else:
                new_months[x] = int(split_dates[0]) - 2

            # New year based on determined warranty value of either 1 or 3

            new_service_years[x] = int(
                split_dates[2]) + warranty_year_values[x]
            new_date = dt.datetime(new_service_years[x], new_months[x],
                                   new_days[x])
            formatted_date = new_date.strftime("%Y-%m-%d").split(' ')[0]

            new_dates[x] = formatted_date
            # print(formatted_date)

        for i in range(len(new_dates)):

            if todays_date == new_dates[i]:
                print(
                    f"Today is {todays_date}, and the date of reminder is {new_dates[i]}, and the client is {name_rows[i]}"
                )
                time.sleep(0.5)
                send_email_reminder(name_rows[i], dos_rows[i],
                                    warranty_year_values[i])
                print("Email reminder is sent!")
            else:
                continue

        # Calling the frontend to create new window after backend processes have finished
        from Frontend import CSVWin

        new_window = CSVWin(self.win, df, self.file)

        new_window.__call__()

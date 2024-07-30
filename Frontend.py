import customtkinter as ctk 
import datetime as dt
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from Backend import BackendWorker
import time
from tkinter import messagebox



class CSVWin: 

    def __init__(self, win, df, filename):
        self.win = win
        self.df = df
        self.filename = filename

    def __call__(self): 

        # Function that is called when the save button is pressed, will create a new file or add a row to the existing files of the csv.

        def update_csv():
            DOS = DOS_input.get()
            PATIENT = patient_input.get()
            MFR = MFR_input.get()
            MODEL = model_input.get()
            NUMBER = number_input.get()
            STATUS = status_input.get()

            DOS_input.delete(0, tk.END)
            patient_input.delete(0, tk.END)
            MFR_input.delete(0, tk.END)
            model_input.delete(0, tk.END)

            new_data = {
                "DOS": DOS, 
                "Patient" : PATIENT, 
                "Mfr" : MFR, 
                "Model" : MODEL, 
                "No." : NUMBER,
                "Status" : STATUS
            }

            self.df.loc[len(self.df)] = new_data
            self.df.reset_index(drop=True)

            # print(self.df)

            self.df.to_csv('new_csv.csv')

            edit_win.withdraw()

            backend_processor = BackendWorker(edit_win, self.filename)
            backend_processor.__call__()

        self.win.withdraw()


        edit_win = ctk.CTkToplevel(self.win)
        edit_win.geometry('800x400')
        edit_win.resizable(True, True)
        edit_win.title('Editing Screen')

        # Beginning of front-end related tasks and code

        # Setting up the page layout and GUI

        frame1 = ctk.CTkScrollableFrame(master=edit_win, scrollbar_button_color="orange")
        frame1.pack(fill="both", expand=True)

        frame2 = ctk.CTkFrame(master=frame1, fg_color='orange', height=200, corner_radius=0)
        frame2.pack(fill='both', expand=True)

        title_label = ctk.CTkLabel(master=frame2, text_color="White", text="Edit CSV file Page", font=("Cascadia Mono", 25))
        title_label.pack(padx=10, pady=2)

        description_label = ctk.CTkLabel(master=frame1, text_color="orange", text="You can edit the CSV file directly from here, by adding rows of information one patient at a time!", font=("Bahnschrift SemiBold SemiConden", 16))
        description_label.pack(padx=10, pady=4)

        # Set up of the CSV editing widgets (textboxes, labels, etc.)

        DOS_label = ctk.CTkLabel(master=frame1, text_color="orange", text="DOS (Date of Service)", font=("Bahnschrift SemiBold SemiConden", 16))
        DOS_label.pack(padx=10, pady=6)
        DOS_input = ctk.CTkEntry(master=frame1, width=150, border_width=3, border_color='#8d6121', text_color='orange')
        DOS_input.pack(padx=10, pady=6.25)

        patient_label = ctk.CTkLabel(master=frame1, text_color="orange", text="Patient Name", font=("Bahnschrift SemiBold SemiConden", 16))
        patient_label.pack(padx=10, pady=7.25)
        patient_input = ctk.CTkEntry(master=frame1, width=150, border_width=3, border_color='#8d6121', text_color='orange')
        patient_input.pack(padx=10, pady=7.5)

        MFR_label = ctk.CTkLabel(master=frame1, text_color="orange", text="MFR Name", font=("Bahnschrift SemiBold SemiConden", 16))
        MFR_label.pack(padx=10, pady=8.5)
        MFR_input = ctk.CTkEntry(master=frame1, width=150, border_width=3, border_color='#8d6121', text_color='orange')
        MFR_input.pack(padx=10, pady=8.75)

        model_label = ctk.CTkLabel(master=frame1, text_color="orange", text="Model Name", font=("Bahnschrift SemiBold SemiConden", 16))
        model_label.pack(padx=10, pady=9.75)
        model_input = ctk.CTkEntry(master=frame1, width=150, border_width=3, border_color='#8d6121', text_color='orange')
        model_input.pack(padx=10, pady=10)

        number_label =  ctk.CTkLabel(master=frame1, text_color="orange", text="Number", font=("Bahnschrift SemiBold SemiConden", 16))
        number_label.pack(padx=10, pady=11)
        number_input = ctk.CTkOptionMenu(master=frame1, width=150, text_color='white', button_hover_color='#c49f3b', dropdown_hover_color='#c49f3b', dropdown_fg_color="orange", fg_color = "orange", button_color='orange', dropdown_font=("Bahnschrift SemiBold SemiConden", 14), values=["1", "2"])
        number_input.pack(padx=10, pady=11.25)

        status_label = ctk.CTkLabel(master=frame1, text_color="orange", text="Status", font=("Bahnschrift SemiBold SemiConden", 16))
        status_label.pack(padx=10, pady=12.25)
        status_input = ctk.CTkOptionMenu(master=frame1, width=150, text_color='white', button_hover_color = '#c49f3b', dropdown_hover_color='#c49f3b', dropdown_fg_color="orange", fg_color='orange', button_color='orange', dropdown_font=("Bahnschrift SemiBold SemiConden", 15), values=["Fitting", "Repair"])
        status_input.pack(padx=10, pady=12.5)

        add_button = ctk.CTkButton(master=frame1, fg_color="orange", text_color='white', width=120, hover_color='#c49f3b', border_width=3, border_color='#8d6121', height=45, text="Add new row", command=update_csv)
        add_button.pack(padx=10, pady=13.5)

        disclaimer_label = ctk.CTkLabel(master=frame1, text="", text_color="orange", font=("Bahnschrift SemiBold SemiConden", 15))
        disclaimer_label.pack(padx=10, pady=14)

import customtkinter as ctk 
from tkinter import filedialog
from Backend import BackendWorker
import datetime as dt
import pandas as pd
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkfont
import schedule

# Code to open file dialog

# color theme: #00FFFF
# Fonts: Times New Roman (titles should be 25 and regular headings should be 20, text should be 12-15)


def open_file(): 
    file = filedialog.askopenfilename()

    if (file == ''):
        start_button.pack_forget()
    else: 
        start_button.pack(padx=10, pady=27)
        file_used_label.pack(side=tk.BOTTOM)
        reader.update_file(file)



window = ctk.CTk()


window.geometry('800x400')

window.title('Main Screen')

ctk.set_appearance_mode("dark")

window.resizable(True, True)



frame = ctk.CTkFrame(master=window, width=400, height=800, fg_color="orange")

frame.pack(side=tk.RIGHT)

logo_img = ctk.CTkImage(Image.open("C:/Users/Vikraant/Downloads/excellogo.png"), size=(300, 200))

img_label = ctk.CTkLabel(master=frame, image=logo_img, text=' ', width=400, height=800)

img_label.pack()

title_label = ctk.CTkLabel(master=window, text="EXCEL AUDIOLODY NOTIFIER", text_color="orange", font=("Bahnschrift SemiBold SemiConden", 25))

title_label.pack(padx=10, pady=10)

file_used_label = ctk.CTkLabel(master=frame, text="", text_color='white', font=('Bahnschrift SemiBold SemiConden', 12))

file_used_label.pack_forget()

# Setting up the object for the child windows of the main window declared above


reader = BackendWorker(window, '')

csv_button = ctk.CTkButton(master=window, text="Press to Open File", border_width=3, border_color='#8d6121', width=50, height=40, text_color="white", font= ('Bahnschrift SemiBold SemiConden', 16), fg_color='orange', hover_color='#c49f3b', command=open_file)

csv_button.pack(padx=10, pady=25)

start_button = ctk.CTkButton(master=window, text="Start", fg_color='orange', border_width=3, border_color='#8d6121', hover_color='#c49f3b', text_color='white', font=('Bahnschrift SemiBold SemiConden', 16), command=reader.__call__)

start_button.pack_forget()




window.mainloop()





# Schedules the program to run every single day at 12 PM EST, to ensure that the days are being kept track of and program runs diligently

# schedule.every().day.at('12:00').do(main.__call__)

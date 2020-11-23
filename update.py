import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

import sqlite3
from sqlite3 import Error

TEXT_FONT = "poppins"
TEXT_FONT_SIZE = 9

# Constant options for the option menu elements
ParishList = [
    "Kingston",
    "Hanover",
    "Clarendon",
    "Manchester",
    "Trelawny",
    "Portland",
    "St. Andrew",
    "St. Catherine",
    "St. James",
    "St. Ann",
    "St. Mary",
    "St. Thomas",
    "St. Elizabeth",
]


class UpdateUI(tk.Frame):
    """
    Host all functions related to the main user interface
    """

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Update Expert System')
        master.resizable(0, 0)

        # INITIALIZE FRAMES
        self.header_frame = tk.Frame(self.master)
        self.section_1_frame = tk.LabelFrame(
            self.master, text="Parish", font=(TEXT_FONT, 11))
        self.section_2_frame = tk.LabelFrame(
            self.master, text="Current Cases in Parish", font=(TEXT_FONT, 11))
        self.section_3_frame = tk.LabelFrame(
            self.master, text="Total Cases in Island", font=(TEXT_FONT, 11))
        self.section_4_frame = tk.Frame(self.master)

        self.header_frame.configure(bg="#fff")
        self.section_4_frame.configure(bg="#333")

        self.header_frame.pack(fill=tk.X, ipady=10, side=tk.TOP)
        self.section_1_frame.pack(
            fill=tk.X, padx=10, pady=5, ipadx=10, ipady=10)
        self.section_2_frame.pack(
            fill=tk.X, padx=10, pady=5, ipadx=10, ipady=10)
        self.section_3_frame.pack(
            fill=tk.X, padx=10, pady=5, ipadx=10, ipady=10)
        self.section_4_frame.pack(fill=tk.X, ipadx=10, side=tk.BOTTOM)

        self.__create_ui()

    def __create_ui(self):
        """
        Generates the application user interface
        """
        self.__insert_logo_image()

        # partish input
        # store input value
        self.parish = tk.StringVar()
        self.parish.set(ParishList[0])
        # input element
        tk.Label(self.section_1_frame, text="Parish", font=(TEXT_FONT, TEXT_FONT_SIZE)).grid(
            row=1, column=0, padx=10, sticky=tk.W)
        self.parish_options = tk.OptionMenu(
            self.section_1_frame, self.parish, *ParishList)
        self.parish_options.config(width=20, bg="#fff", relief=tk.GROOVE,
                                   activebackground='#fff')

        # parish cases into input
        self.parish_cases = tk.StringVar()
        tk.Label(self.section_2_frame, text="Number of Cases in Parish", font=(
            TEXT_FONT, TEXT_FONT_SIZE)).grid(row=0, column=0, padx=10, sticky=tk.W)
        tk.Entry(self.section_2_frame, textvariable=self.parish_cases, relief=tk.GROOVE, font=(
            TEXT_FONT, TEXT_FONT_SIZE)).grid(row=1, column=0, padx=10, sticky=tk.W)

        # parish cases into input
        self.country_cases = tk.StringVar()
        tk.Label(self.section_3_frame, text="Number of Cases in Country", font=(
            TEXT_FONT, TEXT_FONT_SIZE)).grid(row=0, column=0, padx=10, sticky=tk.W)
        tk.Entry(self.section_3_frame, textvariable=self.country_cases, relief=tk.GROOVE, font=(
            TEXT_FONT, TEXT_FONT_SIZE)).grid(row=1, column=0, padx=10, sticky=tk.W)

        tk.Button(self.section_4_frame, text="Submit", height=2, width=10, bg="#FFB52F", fg="#fff", activebackground='#e5625e',
                  relief=tk.FLAT, command=self.getInfo).grid(row=0, column=0, sticky=tk.W, pady=15, padx=10)
        tk.Label(self.section_4_frame, text='ℹ Whenever you are done please press this button', font=(
            TEXT_FONT, TEXT_FONT_SIZE), padx=5, bg="#333", fg="#fff").grid(row=0, column=1, sticky=tk.W)

        self.parish_options.grid(row=2, column=0, sticky=tk.W, padx=10)

    def __input_validation(self):
        """
        Validate user input on UI
        """
        if not(self.parish_cases.get() == ''):
            try:
                int(self.parish_cases.get())
            except:
                messagebox.showinfo("Invalid input value",
                                    "The value you entered for number of parish cases is invalid")
                return False
        else:
            messagebox.showinfo("You missed a field",
                                "Number of Parish Cases field is required")
            return False

        if not(self.country_cases.get() == ''):
            try:
                int(self.country_cases.get())
            except:
                messagebox.showinfo("Invalid input value",
                                    "The value you entered for number of country is invalid")
                return False
        else:
            messagebox.showinfo("You missed a field",
                                "Number of Country Cases field is required")
            return False

        return True

    def getInfo(self):
        """
        Submit all values to covid expert system
        """
        if not(self.__input_validation()):
            return

        form_values = self.__input_form_values()
        parish = form_values["parish_val"]
        parish_case = form_values["parish_cases"]
        country_case = form_values["country_cases"]

        calc_chance = float(parish_case)/float(country_case)
        if "st." in parish:
            parish = parish.split(" ")
            parish[0] = "saint"
            parish = "_".join(parish)
        messagebox.showinfo(
            "Results", "Parish information updated successfully")

        self.open_db_connection()
        self.update_database(calc_chance, parish.lower())

    def update_database(self, chance, parish):
        try:
            update_parish_query = f"UPDATE parishes SET chance={chance} WHERE parish='{parish}'"
            cursorObj = self.con.cursor()
            cursorObj.execute(update_parish_query)
            self.con.commit()
        except:
            print("Error occured updating database")

    def open_db_connection(self):
        try:
            self.con = sqlite3.connect("covidAi.db")
            print("[Connection established]")
        except Error:
            print(Error)

    def __input_form_values(self):
        parish_val = self.parish.get()
        parish_case_val = self.parish_cases.get()
        country_case_val = self.country_cases.get()

        return {
            "parish_val": parish_val,
            "parish_cases": parish_case_val,
            "country_cases": country_case_val,
        }

    def __insert_logo_image(self):
        """
        Insert the application logo into the main ui
        """
        # TODO Logo not displaying
        # IMAGES
        self.logo = ImageTk.PhotoImage(Image.open("assets\\LOGO.png"))
        tk.Label(self.header_frame, image=self.logo, bg="#fff").pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = UpdateUI(master=root)
    app.mainloop()

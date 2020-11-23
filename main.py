from patient_data_store import PatientDataStore
from user_input_ui import UserInputUI
import tkinter as tk
from PIL import ImageTk, Image


import sqlite3
from sqlite3 import Error

covid_cases_parish = [
    ('kingston', 0.3616),
    ('hanover', 0.0207),
    ('trelawny', 0.0278),
    ('clarendon', 0.0677),
    ('manchester', 0.084),
    ('portland', 0.008),
    ('saint_ann', 0.0459),
    ('saint_mary', 0.0264),
    ('saint_james', 0.1647),
    ('saint_elizabeth', 0.0353),
    ('saint_catherine', 0.1563),
    ('saint_thomas', 0.0188),
    ('saint_andrew', 0.3616)
]


class MainUI (tk.Frame):
    """
    The applicatins main user interface
    """

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Covid AI Expert System')
        master.configure(bg="#fff")
        master.geometry("700x350")
        master.resizable(0, 0)

        self.header_frame = tk.Frame(self.master)
        self.header_frame.configure(bg="#fff")
        self.header_frame.pack(fill=tk.X, ipady=10, side=tk.TOP)

        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.configure(bg="#fff")
        self.menu_frame.pack(fill=tk.X, ipady=10, side=tk.TOP)

        self.disclaimer_frame = tk.Frame(self.master)
        self.disclaimer_frame.configure(bg="#333")
        self.disclaimer_frame.pack(
            fill=tk.X, ipady=10, side=tk.BOTTOM)

        tk.Button(self.menu_frame, text="Get tested", height=2, width=10, bg="#067924", fg="#fff", activebackground='#e5625e',
                  relief=tk.FLAT, command=self.get_tested).pack(pady=5)
        tk.Button(self.menu_frame, text="View Pateints", height=2, width=20, bg="#067924", fg="#fff", activebackground='#e5625e',
                  relief=tk.FLAT).pack(pady=5)
        tk.Button(self.menu_frame, text="Update knowledge Base", height=2, width=30, bg="#067924", fg="#fff", activebackground='#e5625e',
                  relief=tk.FLAT).pack(pady=5)

        tk.Label(self.disclaimer_frame, text="The diagnosis here is generated based on statistics from research into COVID-19.", font=(
            "poppints", 10), bg="#333", fg="#fff").pack()
        tk.Label(self.disclaimer_frame, text="We urge you to still take a test regardless of your result here.", font=(
            "poppints", 10), bg="#333", fg="#fff").pack()

        self.__insert_logo_image()

    def get_tested(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = UserInputUI(self.newWindow)

    def __insert_logo_image(self):
        """
        Insert the application logo into the main ui
        """
        # TODO Logo not displaying
        # IMAGES
        self.logo = ImageTk.PhotoImage(Image.open("assets\\LOGO.png"))
        tk.Label(self.header_frame, image=self.logo, bg="#fff").pack()

    def __create_main_ui(self):
        pass


def create_parish_table(con):
    """
    Creates table with statistical information for each parish
    """
    parish_table = "CREATE TABLE IF NOT EXISTS parishes(id integer PRIMARY KEY, parish text, chance integer)"
    cursorObj = con.cursor()
    cursorObj.execute(parish_table)
    con.commit()


def open_db_connection():
    try:
        con = sqlite3.connect("covidAi.db")
        print("[Connection established]")
        return con
    except Error:
        print(Error)


def parish_statistics_seeder(con):
    for (parish, case) in covid_cases_parish:
        parish_info = f"INSERT INTO parishes(parish, chance) VALUES ('{parish}', {case})"
        cursorObj = con.cursor()
        cursorObj.execute(parish_info)
        con.commit()


def parish_table_empty(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM parishes")
    rows = list(cursorObj.fetchall())
    if (len(rows) == 0):
        return True
    return False


def main():
    # create instance of patient data store
    PatientDataStore()
    connection = open_db_connection()

    create_parish_table(connection)
    if (parish_table_empty(connection)):
        parish_statistics_seeder(connection)

    root = tk.Tk()
    app = MainUI(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()

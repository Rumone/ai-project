from patient_data_store import PatientDataStore
from user_input_ui import UserInputUI
import tkinter as tk
from PIL import ImageTk, Image


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


def main():

    # create instance of patient data store
    PatientDataStore()

    root = tk.Tk()
    app = MainUI(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()

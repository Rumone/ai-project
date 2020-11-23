import tkinter as tk
from covid_ai_bridge import CovidAIBrigde
from tkinter import messagebox
from PIL import ImageTk, Image
from patient_data_store import PatientDataStore

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

# Constants for choice menu
ChoiceList = [
    "Yes",
    "No",
    "Sometimes",
]


class UserInputUI(tk.Frame):
    """
    Host all functions related to the main user interface
    """

    def __init__(self, master):
        """
        Initialize the main ui component
        Parameter
            master: master ui component
        """
        super().__init__(master)
        self.master = master
        master.title('Covid AI Expert System')
        master.resizable(0, 0)
        # INITIALIZE FRAMES
        self.header_frame = tk.Frame(self.master)
        self.section_1_frame = tk.LabelFrame(
            self.master, text="What should I call you?", font=(TEXT_FONT, 11))
        self.section_2_frame = tk.LabelFrame(
            self.master, text="Where did you come from?", font=(TEXT_FONT, 11))
        self.section_3_frame = tk.LabelFrame(
            self.master, text="What have you been up to?", font=(TEXT_FONT, 11))
        self.section_4_frame = tk.LabelFrame(
            self.master, text="What symptoms do you have?", font=(TEXT_FONT, 11))
        self.section_5_frame = tk.Frame(self.master)
        self.section_6_frame = tk.Frame(self.master)

        self.header_frame.configure(bg="#fff")
        self.section_6_frame.configure(bg="#333")

        self.header_frame.pack(fill=tk.X, ipady=10, side=tk.TOP)
        self.section_1_frame.pack(
            fill=tk.X, padx=10, pady=5, ipadx=10, ipady=10)
        self.section_2_frame.pack(
            fill=tk.X, padx=10, pady=5, ipadx=10, ipady=10)
        self.section_3_frame.pack(
            fill=tk.X, padx=10, pady=5, ipadx=10, ipady=10)
        self.section_4_frame.pack(
            fill=tk.X, padx=10, pady=5, ipadx=10, ipady=10)
        self.section_5_frame.pack(
            fill=tk.X, padx=10, pady=5, ipadx=10, ipady=10)
        self.section_6_frame.pack(fill=tk.X, ipadx=10, side=tk.BOTTOM)

        self.__create_ui()

    def __create_ui(self):
        """
        Generates the application user interface
        """
        self.__insert_logo_image()
        # accept first name into input
        self.first_name = tk.StringVar()
        tk.Label(self.section_1_frame, text="First Name", font=(
            TEXT_FONT, TEXT_FONT_SIZE)).grid(row=0, column=0, padx=10, sticky=tk.W)
        tk.Entry(self.section_1_frame, textvariable=self.first_name, relief=tk.GROOVE, font=(
            TEXT_FONT, TEXT_FONT_SIZE)).grid(row=1, column=0, padx=10, sticky=tk.W)
        # accept last name into input
        self.last_name = tk.StringVar()
        tk.Label(self.section_1_frame, text="Last Name", font=(
            TEXT_FONT, TEXT_FONT_SIZE)).grid(row=0, column=2, padx=10, sticky=tk.W)
        tk.Entry(self.section_1_frame, textvariable=self.last_name, relief=tk.GROOVE, bd=1, font=(
            TEXT_FONT, TEXT_FONT_SIZE)).grid(row=1, column=2, padx=10, sticky=tk.W)

        # partish input
        # store input value
        self.parish = tk.StringVar()
        self.parish.set(ParishList[0])
        # input element
        tk.Label(self.section_2_frame, text="Parish", font=(TEXT_FONT, TEXT_FONT_SIZE)).grid(
            row=1, column=0, padx=10, sticky=tk.W)
        self.parish_options = tk.OptionMenu(
            self.section_2_frame, self.parish, *ParishList)
        self.parish_options.config(width=20, bg="#fff", relief=tk.GROOVE,
                                   activebackground='#fff')

        # Questions about what the patient was up to
        # store input value
        self.wears_mask = tk.StringVar()
        self.wears_mask.set(ChoiceList[0])
        tk.Label(self.section_3_frame, text='Do you wear a mask?', font=(
            TEXT_FONT, TEXT_FONT_SIZE), padx=5).grid(row=1, column=2, sticky=tk.W)
        self.wears_mask_options = tk.OptionMenu(
            self.section_3_frame, self.wears_mask, *ChoiceList)
        self.wears_mask_options.config(
            bg="#fff", relief=tk.GROOVE, activebackground='#fff')

        self.travel = tk.StringVar()
        self.travel.set(ChoiceList[0])
        tk.Label(self.section_3_frame, text='Do you travel alot?', font=(
            TEXT_FONT, TEXT_FONT_SIZE), padx=5).grid(row=2, column=2, sticky=tk.W)
        self.travel_options = tk.OptionMenu(
            self.section_3_frame, self.travel, *ChoiceList)
        self.travel_options.config(
            bg="#fff", relief=tk.GROOVE, activebackground='#fff')

        self.sanitize = tk.StringVar()
        self.sanitize.set(ChoiceList[0])
        tk.Label(self.section_3_frame, text='Do you wash your hands and sanitize?', font=(
            TEXT_FONT, TEXT_FONT_SIZE), padx=5).grid(row=3, column=2, sticky=tk.W)
        self.sanitize_options = tk.OptionMenu(
            self.section_3_frame, self.sanitize, *ChoiceList)
        self.sanitize_options.config(
            bg="#fff", relief=tk.GROOVE, activebackground='#fff')

        self.party = tk.StringVar()
        self.party.set(ChoiceList[0])
        tk.Label(self.section_3_frame, text='Do you go to parties?', font=(
            TEXT_FONT, TEXT_FONT_SIZE), padx=5).grid(row=4, column=2, sticky=tk.W)
        self.party_options = tk.OptionMenu(
            self.section_3_frame, self.party, *ChoiceList)
        self.party_options.config(
            bg="#fff", relief=tk.GROOVE, activebackground='#fff')

        self.symptom1 = tk.IntVar()
        self.symptom2 = tk.IntVar()
        self.symptom3 = tk.IntVar()
        self.symptom4 = tk.IntVar()
        self.symptom5 = tk.IntVar()
        self.symptom6 = tk.IntVar()
        self.symptom7 = tk.IntVar()
        self.symptom8 = tk.IntVar()
        self.symptom9 = tk.IntVar()
        self.symptom10 = tk.IntVar()
        self.symptom11 = tk.IntVar()

        tk.Checkbutton(self.section_4_frame, variable=self.symptom1, onvalue=1, offvalue=0,
                       text="Fever or chills").grid(row=0, column=0, sticky=tk.W)
        tk.Checkbutton(self.section_4_frame, variable=self.symptom2, onvalue=1,
                       offvalue=0, text="Cough").grid(row=1, column=0, sticky=tk.W)
        tk.Checkbutton(self.section_4_frame, variable=self.symptom3, onvalue=1, offvalue=0,
                       text="Shortness of breath or difficulty breathing").grid(row=2, column=0, sticky=tk.W)
        tk.Checkbutton(self.section_4_frame, variable=self.symptom4, onvalue=1, offvalue=0,
                       text="New loss of taste or smell").grid(row=3, column=0, sticky=tk.W)

        tk.Checkbutton(self.section_4_frame, variable=self.symptom5, onvalue=1,
                       offvalue=0, text="Fatigue").grid(row=0, column=1, sticky=tk.W)
        tk.Checkbutton(self.section_4_frame, variable=self.symptom6, onvalue=1, offvalue=0,
                       text="Muscle or body aches").grid(row=1, column=1, sticky=tk.W)
        tk.Checkbutton(self.section_4_frame, variable=self.symptom7, onvalue=1,
                       offvalue=0, text="Headache").grid(row=2, column=1, sticky=tk.W)
        tk.Checkbutton(self.section_4_frame, variable=self.symptom8, onvalue=1,
                       offvalue=0, text="Sore throat").grid(row=3, column=1, sticky=tk.W)

        tk.Checkbutton(self.section_4_frame, variable=self.symptom9, onvalue=1, offvalue=0,
                       text="Congestion or runny nose").grid(row=0, column=2, sticky=tk.W)
        tk.Checkbutton(self.section_4_frame, variable=self.symptom10, onvalue=1, offvalue=0,
                       text="Nausea or vomiting").grid(row=1, column=2, sticky=tk.W)
        tk.Checkbutton(self.section_4_frame, variable=self.symptom11, onvalue=1,
                       offvalue=0, text="Diarrhea").grid(row=2, column=2, sticky=tk.W)

        self.temp = tk.StringVar()
        tk.Label(self.section_5_frame, text="What is your temperature?", font=(
            TEXT_FONT, TEXT_FONT_SIZE)).grid(row=0, column=0, padx=10, sticky=tk.W)
        tk.Entry(self.section_5_frame, textvariable=self.temp, relief=tk.GROOVE, font=(
            TEXT_FONT, TEXT_FONT_SIZE)).grid(row=1, column=0, padx=10, sticky=tk.W)

        tk.Button(self.section_6_frame, text="Submit", height=2, width=10, bg="#FFB52F", fg="#fff", activebackground='#e5625e',
                  relief=tk.FLAT, command=self.__submit_values).grid(row=0, column=0, sticky=tk.W, pady=15, padx=10)
        tk.Label(self.section_6_frame, text='ℹ Whenever you are done please press this button', font=(
            TEXT_FONT, TEXT_FONT_SIZE), padx=5, bg="#333", fg="#fff").grid(row=0, column=1, sticky=tk.W)

        self.parish_options.grid(row=2, column=0, sticky=tk.W, padx=10)
        self.wears_mask_options.grid(row=1, column=3, sticky=tk.W)
        self.travel_options.grid(row=2, column=3, sticky=tk.W)
        self.sanitize_options.grid(row=3, column=3, sticky=tk.W)
        self.party_options.grid(row=4, column=3, sticky=tk.W)

    def __input_validation(self):
        """
        Validate user input on UI
        """
        if (self.first_name.get() == '' or self.last_name.get() == ''):
            messagebox.showinfo("You missed a field",
                                "The first and last name field is required")
            return False
        if not(self.temp.get() == ''):
            try:
                int(self.temp.get())
            except:
                messagebox.showinfo("Invalid temperature value",
                                    "The value you entered for your temperature is invalid")
                return False
        else:
            messagebox.showinfo("You missed a field",
                                "Temperature field is required")
            return False

        return True

    def __submit_values(self):
        """
        Submit all values to covid expert system
        """
        if not(self.__input_validation()):
            return

        # messagebox.showinfo("Pending", "I am processing your information")
        form_values = self.__input_form_values()
        covid_ai = CovidAIBrigde(form_values["patient_name"])
        covid_ai.update_knowledgebase()
        covid_ai.store_patient_activities(
            form_values["wears_mask"], form_values["travels"], form_values["sanitizes"], form_values["parties"])
        covid_ai.store_temperature(form_values["temp"])
        covid_ai.store_symptoms(form_values["symptoms"])
        covid_ai.store_home_parish(form_values['current_parish'])

        diagnosis = covid_ai.diagnose()['X']

        diagnosis_accuracy = diagnosis * 100
        if (diagnosis_accuracy >= 50 and diagnosis_accuracy <= 75):
            messagebox.showinfo(
                "Results", "You may test positive for COVID 19, please take a real test if you can")
        elif (diagnosis_accuracy > 75):
            messagebox.showinfo(
                "Results", "Based on your answers I think you positive for COVID 19, please take a real test immediately for confirmation")
        else:
            messagebox.showinfo(
                "Results", "I have no reason to believe you have COVID-19, however, I recommend you still take a real test")

        covid_ai.memory_wipe()

        patient = PatientDataStore.getInstance()
        patient.store_patient(
            form_values["patient_name"], form_values['current_parish'], form_values["temp"], diagnosis_accuracy)
        patient.get_patients()

    def __input_form_values(self):
        patient_name = self.first_name.get() + " " + self.last_name.get()
        parish_val = self.parish.get()
        wears_mask_val = self.wears_mask.get()
        travel_val = self.travel.get()
        sanitize_val = self.sanitize.get()
        party_val = self.party.get()
        temp_val = self.temp.get()
        symptoms = []
        # deal with symptoms
        if (self.symptom1.get() == 1):
            symptoms.append("Fever or chills")
        if (self.symptom2.get() == 1):
            symptoms.append("Cough")
        if (self.symptom3.get() == 1):
            symptoms.append("Shortness of breath or difficulty breathing")
        if (self.symptom4.get() == 1):
            symptoms.append("New loss of taste or smell")
        if (self.symptom5.get() == 1):
            symptoms.append("Fatigue")
        if (self.symptom6.get() == 1):
            symptoms.append("Muscle or body aches")
        if (self.symptom7.get() == 1):
            symptoms.append("Headache")
        if (self.symptom8.get() == 1):
            symptoms.append("Sore throat")
        if (self.symptom9.get() == 1):
            symptoms.append("Congestion or runny nose")
        if (self.symptom10.get() == 1):
            symptoms.append("Nausea or vomiting")
        if (self.symptom11.get() == 1):
            symptoms.append("Diarrhea")

        return {
            "patient_name": patient_name,
            "current_parish": parish_val,
            "wears_mask": wears_mask_val,
            "travels": travel_val,
            "sanitizes": sanitize_val,
            "parties": party_val,
            "temp": temp_val,
            "symptoms": symptoms
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
    app = UserInputUI(master=root)
    app.mainloop()

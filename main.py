from tkinter import *
from tkinter import messagebox
from covid_ai_bridge import CovidAIBrigde

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Basic functionality


def validation():
    if (first_name.get() == '' or last_name.get() == ''):
        messagebox.showinfo("You missed a field",
                            "The first and last name field is required")
        return False
    if not(temp.get() == ''):
        try:
            int(temp.get())
        except:
            messagebox.showinfo("Invalid temperature value",
                                "The value you entered for your temperature is invalid")
            return False
    else:
        messagebox.showinfo("You missed a field",
                            "Temperature field is required")
        return False

    return True


def getFormValues():
    patient_name = first_name.get() + " " + last_name.get()
    parish_val = parish.get()
    wears_mask_val = wears_mask.get()
    travel_val = travel.get()
    sanitize_val = sanitize.get()
    party_val = party.get()
    temp_val = temp.get()
    symptoms = []
    # deal with symptoms
    if (symptom1.get() == 1):
        symptoms.append("Fever or chills")
    if (symptom2.get() == 1):
        symptoms.append("Cough")
    if (symptom3.get() == 1):
        symptoms.append("Shortness of breath or difficulty breathing")
    if (symptom4.get() == 1):
        symptoms.append("New loss of taste or smell")
    if (symptom5.get() == 1):
        symptoms.append("Fatigue")
    if (symptom6.get() == 1):
        symptoms.append("Muscle or body aches")
    if (symptom7.get() == 1):
        symptoms.append("Headache")
    if (symptom8.get() == 1):
        symptoms.append("Sore throat")
    if (symptom9.get() == 1):
        symptoms.append("Congestion or runny nose")
    if (symptom10.get() == 1):
        symptoms.append("Nausea or vomiting")
    if (symptom11.get() == 1):
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


def sendResults():
    if not(validation()):
        return

    # messagebox.showinfo("Pending", "I am processing your information")
    form_values = getFormValues()
    covid_ai = CovidAIBrigde(form_values["patient_name"], True)
    covid_ai.store_patient_activities(
        form_values["wears_mask"], form_values["travels"], form_values["sanitizes"], form_values["parties"])
    covid_ai.store_temperature(form_values["temp"])
    covid_ai.store_symptoms(form_values["symptoms"])
    covid_ai.store_home_parish(form_values['current_parish'])

    diagnosis = covid_ai.diagnose()
    print(diagnosis)
    # diagnosis_accuracy = diagnosis * 100
    # if (diagnosis_accuracy >= 50 and diagnosis_accuracy <= 75):
    #     messagebox.showinfo(
    #         "Results", "You may test positive for COVID 19, please take a real test if you can")
    # elif (diagnosis_accuracy > 75):
    #     messagebox.showinfo(
    #         "Results", "Based on your answers I think you positive for COVID 19, please take a real test immediately for confirmation")
    # else:
    #     messagebox.showinfo(
    #         "Results", "I have no reason to believe you have COVID-19, however, I recommend you still take a real test")


# Initializes the tk library
app = Tk()

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

# constants
TEXT_FONT = "poppins"
TEXT_FONT_SIZE = 9


# all frames
section_1_frame = LabelFrame(
    app, text="What should I call you?", font=(TEXT_FONT, 11))
section_2_frame = LabelFrame(
    app, text="Where did you come from?", font=(TEXT_FONT, 11))
section_3_frame = LabelFrame(
    app, text="What have you been up to?", font=(TEXT_FONT, 11))
section_4_frame = LabelFrame(
    app, text="What symptoms do you have?", font=(TEXT_FONT, 11))
section_5_frame = Frame(app)
section_6_frame = Frame(app)

section_6_frame.configure(bg="#333")

section_1_frame.pack(fill=X, padx=10, pady=5, ipadx=10, ipady=10)
section_2_frame.pack(fill=X, padx=10, pady=5, ipadx=10, ipady=10)
section_3_frame.pack(fill=X, padx=10, pady=5, ipadx=10, ipady=10)
section_4_frame.pack(fill=X, padx=10, pady=5, ipadx=10, ipady=10)
section_5_frame.pack(fill=X, padx=10, pady=5, ipadx=10, ipady=10)
section_6_frame.pack(fill=X, ipadx=10, side=BOTTOM)


first_name = StringVar()
last_name = StringVar()
parish = StringVar()
temp = StringVar()

wears_mask = StringVar()
travel = StringVar()
sanitize = StringVar()
party = StringVar()

symptom1 = IntVar()
symptom2 = IntVar()
symptom3 = IntVar()
symptom4 = IntVar()
symptom5 = IntVar()
symptom6 = IntVar()
symptom7 = IntVar()
symptom8 = IntVar()
symptom9 = IntVar()
symptom10 = IntVar()
symptom11 = IntVar()


Label(section_1_frame, text="First Name", font=(
    TEXT_FONT, TEXT_FONT_SIZE)).grid(row=0, column=0, padx=10, sticky=W)
Entry(section_1_frame, textvariable=first_name, relief=FLAT, font=(
    TEXT_FONT, TEXT_FONT_SIZE)).grid(row=1, column=0, padx=10, sticky=W)

Label(section_1_frame, text="Last Name", font=(
    TEXT_FONT, TEXT_FONT_SIZE)).grid(row=0, column=2, padx=10, sticky=W)
Entry(section_1_frame, textvariable=last_name, relief=FLAT, bd=1, font=(
    TEXT_FONT, TEXT_FONT_SIZE)).grid(row=1, column=2, padx=10, sticky=W)


# store input value
parish.set(ParishList[0])
# input element
Label(section_2_frame, text="Parish", font=(TEXT_FONT, TEXT_FONT_SIZE)).grid(
    row=1, column=0, padx=10, sticky=W)
parish_options = OptionMenu(section_2_frame, parish, *ParishList)
parish_options.config(width=20, bg="#fff", relief=GROOVE,
                      activebackground='#fff')

# Questions about what the patient was up to
# store input value
wears_mask.set(ChoiceList[0])
# inpput element
Label(section_3_frame, text='Do you wear a mask?', font=(
    TEXT_FONT, TEXT_FONT_SIZE), padx=5).grid(row=1, column=2, sticky=W)
wears_mask_options = OptionMenu(section_3_frame, wears_mask, *ChoiceList)
wears_mask_options.config(bg="#fff", relief=GROOVE, activebackground='#fff')


travel.set(ChoiceList[0])

Label(section_3_frame, text='Do you travel alot?', font=(
    TEXT_FONT, TEXT_FONT_SIZE), padx=5).grid(row=2, column=2, sticky=W)
travel_options = OptionMenu(section_3_frame, travel, *ChoiceList)
travel_options.config(bg="#fff", relief=GROOVE, activebackground='#fff')


sanitize.set(ChoiceList[0])

Label(section_3_frame, text='Do you wash your hands and sanitize?', font=(
    TEXT_FONT, TEXT_FONT_SIZE), padx=5).grid(row=3, column=2, sticky=W)
sanitize_options = OptionMenu(section_3_frame, sanitize, *ChoiceList)
sanitize_options.config(bg="#fff", relief=GROOVE, activebackground='#fff')

party.set(ChoiceList[0])

Label(section_3_frame, text='Do you go to parties?', font=(
    TEXT_FONT, TEXT_FONT_SIZE), padx=5).grid(row=4, column=2, sticky=W)
party_options = OptionMenu(section_3_frame, party, *ChoiceList)
party_options.config(bg="#fff", relief=GROOVE, activebackground='#fff')

Checkbutton(section_4_frame, variable=symptom1, onvalue=1, offvalue=0,
            text="Fever or chills").grid(row=0, column=0, sticky=W)
Checkbutton(section_4_frame, variable=symptom2, onvalue=1,
            offvalue=0, text="Cough").grid(row=1, column=0, sticky=W)
Checkbutton(section_4_frame, variable=symptom3, onvalue=1, offvalue=0,
            text="Shortness of breath or difficulty breathing").grid(row=2, column=0, sticky=W)
Checkbutton(section_4_frame, variable=symptom4, onvalue=1, offvalue=0,
            text="New loss of taste or smell").grid(row=3, column=0, sticky=W)


Checkbutton(section_4_frame, variable=symptom5, onvalue=1,
            offvalue=0, text="Fatigue").grid(row=0, column=1, sticky=W)
Checkbutton(section_4_frame, variable=symptom6, onvalue=1, offvalue=0,
            text="Muscle or body aches").grid(row=1, column=1, sticky=W)
Checkbutton(section_4_frame, variable=symptom7, onvalue=1,
            offvalue=0, text="Headache").grid(row=2, column=1, sticky=W)
Checkbutton(section_4_frame, variable=symptom8, onvalue=1,
            offvalue=0, text="Sore throat").grid(row=3, column=1, sticky=W)

Checkbutton(section_4_frame, variable=symptom9, onvalue=1, offvalue=0,
            text="Congestion or runny nose").grid(row=0, column=2, sticky=W)
Checkbutton(section_4_frame, variable=symptom10, onvalue=1, offvalue=0,
            text="Nausea or vomiting").grid(row=1, column=2, sticky=W)
Checkbutton(section_4_frame, variable=symptom11, onvalue=1,
            offvalue=0, text="Diarrhea").grid(row=2, column=2, sticky=W)


Label(section_5_frame, text="What is your temperature?", font=(
    TEXT_FONT, TEXT_FONT_SIZE)).grid(row=0, column=0, padx=10, sticky=W)
Entry(section_5_frame, textvariable=temp, relief=FLAT, font=(
    TEXT_FONT, TEXT_FONT_SIZE)).grid(row=1, column=0, padx=10, sticky=W)


Button(section_6_frame, text="Submit", height=2, width=10, bg="#e5625e", fg="#fff", activebackground='#e5625e',
       relief=FLAT, command=sendResults).grid(row=0, column=0, sticky=W, pady=15, padx=10)
Label(section_6_frame, text='✔ Whenever you are done please press this button', font=(
    TEXT_FONT, TEXT_FONT_SIZE), padx=5, bg="#333", fg="#fff").grid(row=0, column=1, sticky=W)

parish_options.grid(row=2, column=0, sticky=W, padx=10)
wears_mask_options.grid(row=1, column=3, sticky=W)
travel_options.grid(row=2, column=3, sticky=W)
sanitize_options.grid(row=3, column=3, sticky=W)
party_options.grid(row=4, column=3, sticky=W)


app.title('Covid AI Expert System')
app.resizable(0, 0)
app.mainloop()

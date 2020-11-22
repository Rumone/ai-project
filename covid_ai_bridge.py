from pyswip import Prolog


class CovidAIBrigde:
    """
    Communicates directly with prolog scripts to return diagnosis
    """

    def __init__(self, name, log=False):
        self.prolog = Prolog()
        self.patient_name = name.split(" ")[0].lower()
        self.log = log

        self.prolog.consult('covid.pl')

    def store_home_parish(self, parish):
        """
        Store the patient current home parish
        Parameters:
            parish(list): What symptoms does the patients
        """
        parish = parish.lower()
        if "st." in parish:
            parish = parish.split(" ")
            parish[0] = "saint"
            parish = "_".join(parish)
        query_string = f"from_parish({self.patient_name}, {parish})"
        self.prolog.asserta(query_string)

        if self.log:
            self.__log_function(query_string)

    def store_symptoms(self, symptoms):
        """
        Store the patient symptoms
        Parameters:
            symptoms(list): What symptoms does the patients
        """
        query_strings = [
            f"has_symptom({self.patient_name}, '{symptom}')" for symptom in symptoms]
        for query_string in query_strings:
            self.prolog.asserta(query_string)

        if self.log:
            for query_string in query_strings:
                self.__log_function(query_string)

    def store_temperature(self, temperature):
        """
        Store the patient temperature
        Parameters:
            temperature(int): What is the patients temperature
        """
        query_string = f"patient_temperature({self.patient_name}, {temperature})"
        self.prolog.asserta(query_string)

        if self.log:
            self.__log_function(query_string)

    def store_patient_activities(self, wm, t, s, p):
        """
        Store the patient activities that could contribute to diagnosis
        Parameters:
            wm(str): Does the patient usually wear a mask
            t(str): Does the patient travel alot
            s(str): Does the patient sanitize regularly
            p(str): Does the patient go to parties
        """
        query_string_mask = f"wears_mask({self.patient_name}, {wm.lower()})"
        query_string_travel = f"travels({self.patient_name}, {t.lower()})"
        query_string_sanitize = f"sanitizes({self.patient_name}, {s.lower()})"
        query_string_party = f"goes_parties({self.patient_name}, {p.lower()})"

        self.prolog.asserta(query_string_mask)
        self.prolog.asserta(query_string_travel)
        self.prolog.asserta(query_string_sanitize)
        self.prolog.asserta(query_string_party)

        if (self.log):
            self.__log_function(query_string_mask)
            self.__log_function(query_string_travel)
            self.__log_function(query_string_sanitize)
            self.__log_function(query_string_party)

    def diagnose(self):
        """
        Diagnosis and returns a value for how much the chances this patient has covid
        """
        results = list(self.prolog.query(f"has_covid({self.patient_name}, X)"))
        return results[0]

    def __log_function(self, string):
        """
        prints out any string passed in with specific format
        """
        print(f"I KNOW: {string}.")

    def memory_wipe(self):
        """
        wipe information about patient from the agents memory
        """
        # define predicate strings
        query_string_symptom = f"has_symptom({self.patient_name},_)"
        query_string_parish = f"from_parish({self.patient_name},_)"
        query_string_temp = f"patient_temperature({self.patient_name},_)"
        query_string_mask = f"wears_mask({self.patient_name},_)"
        query_string_travel = f"travels({self.patient_name},_)"
        query_string_sanitize = f"sanitizes({self.patient_name},_)"
        query_string_party = f"goes_parties({self.patient_name},_)"

        self.prolog.retractall(query_string_symptom)
        self.prolog.retract(query_string_parish)
        self.prolog.retract(query_string_temp)
        self.prolog.retract(query_string_mask)
        self.prolog.retract(query_string_travel)
        self.prolog.retract(query_string_sanitize)
        self.prolog.retract(query_string_party)

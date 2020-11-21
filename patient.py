from pyswip import Functor, Variable, Query, call, Prolog
prolog = Prolog()
prolog.consult('covid.pl')

class Patient:
    def __init__(self, name, parish, wears_mask, travels, sanitizes, pary, symptoms):
        self.name = name
        self.parish = parish
        self.wears_mask = wears_mask.lower()
        self.travels = travels.lower()
        self.sanitizes = sanitizes.lower()
        self.pary = pary.lower()
        self.symptoms = symptoms

    def process_patient_info(self):
        # format parish
        formatted_parish = self.parish
        patient_name = self.name.split(" ")[0].lower()
        if "St." in self.parish:
            formatted_parish = self.parish.split(" ")
            formatted_parish[0] = "saint"
            formatted_parish = "_".join(formatted_parish)

        query_string_homeparish = "from_parish({}, {})".format(patient_name, formatted_parish.lower())

        query_string_mask = "wears_mask({}, {})".format(patient_name, self.wears_mask)
        query_string_travel = "travels({}, {})".format(patient_name, self.travels)
        query_string_sanitize = "sanitizes({}, {})".format(patient_name, self.sanitizes)
        query_string_party = "goes_parties({}, {})".format(patient_name, self.pary)

        for symptom in self.symptoms:
            query_string_symptom = "has_symptom({}, '{}')".format(patient_name, symptom)
            print(query_string_symptom)


        query_string_temp = "patient_temperature({}, {})".format(patient_name, 50)

        prolog.assertz(query_string_homeparish)
        prolog.assertz(query_string_temp)
        prolog.assertz(query_string_mask)
        prolog.assertz(query_string_travel)
        prolog.assertz(query_string_sanitize)
        prolog.assertz(query_string_party)

        print(list(prolog.query("has_symptom({},X)".format(patient_name))))

        print(list(prolog.query("has_covid({},X)".format(patient_name))))


        # prolog.retractall("has_symptom(_,_)")
        # print(list(prolog.query("has_symptom({}, X)".format(patient_name))))
    
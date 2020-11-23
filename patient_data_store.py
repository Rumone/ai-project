import sqlite3
from sqlite3 import Error
from datetime import date


class PatientDataStore():
    """
    Stores patient information in sqlite3 database
    """
    __instance = None

    @staticmethod
    def getInstance():
        """
        This is a static method to create class as a singleton
        """
        if PatientDataStore.__instance == None:
            PatientDataStore()
        return PatientDataStore.__instance

    def __init__(self):
        """
        Initialize connection to sqlite datbase
        """
        if PatientDataStore.__instance != None:
            raise Exception("This class is a singleton")
        else:
            PatientDataStore.__instance = self
            self.__open_connection()
            patients_table = "CREATE TABLE IF NOT EXISTS patients(id integer PRIMARY KEY, name text, temperature integer, home_parish text, diagnosis integer, created_at text)"
            cursorObj = self.con.cursor()
            cursorObj.execute(patients_table)
            self.con.commit()

    def store_patient(self, name, parish, temp, diagnosis):
        """
        Initialize connection to sqlite datbase
        Parameters:
            name(str): patients name
            parish(str): patients home parish
            temp(int): patients temperature
            diagnosis(int): patients diagnosis percentage chance patient has covid            
        """
        created_at = date.today().strftime("%d-%m-%Y")
        new_patient = f"INSERT INTO patients(name, temperature, home_parish, diagnosis, created_at) VALUES ('{name}', {temp}, '{parish}', {diagnosis}, '{created_at}')"
        cursorObj = self.con.cursor()
        cursorObj.execute(new_patient)
        self.con.commit()

    def get_patients(self):
        """
        Return all patients stored
        """
        cursorObj = self.con.cursor()
        cursorObj.execute("SELECT * FROM patients")
        rows = list(cursorObj.fetchall())
        print(rows)
        self.con.commit()

    def __open_connection(self):
        try:
            self.con = sqlite3.connect("patient.db")
            print("[Connection established]")
        except Error:
            print(Error)

    def __close_connection(self):
        self.con.close()


if __name__ == "__main__":
    pateintdb = PatientDataStore()

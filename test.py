from pyswip import Prolog
prolog = Prolog()
prolog.consult("covid.pl")
print(list(prolog.query("has_covid(rumone, X)")))
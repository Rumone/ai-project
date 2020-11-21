:- (dynamic wears_mask/2).
:- (dynamic travels/2).
:- (dynamic goes_parties/2).
:- (dynamic sanitizes/2).

:- (dynamic has_symptom/2).
:- (dynamic from_parish/2).
:- (dynamic patient_temperature/2).


% ALL SYMPTOMS BASED ON RESEARCH
symptom('Fever or chills').
symptom('Cough').
symptom('Shortness of breath or difficulty breathing').
symptom('Fatigue').
symptom('Muscle or body aches').
symptom('Headache').
symptom('New loss of taste or smell').
symptom('Sore throat').
symptom('Congestion or runny nose').
symptom('Nausea or vomiting').
symptom('Diarrhea').


parish(kingston).
parish(saint_james).
parish(saint_elizabeth).
parish(hanover).
parish(trelawny).
parish(clarendon).
parish(manchester).
parish(saint_ann).
parish(saint_catherine).
parish(saint_mary).
parish(portland).
parish(saint_thomas).
parish(saint_andrew).

% percentage of the number of covid cases per parish
% the values here are random as of current

% kingston - 40%
covid_cases(kingston, 0.8).
% hanover - 10%
covid_cases(hanover, 0.1).
% trelawny - 20%
covid_cases(trelawny, 0.2).
% clarendon - 10%
covid_cases(clarendon, 0.1).
% manchester - 10%
covid_cases(manchester, 0.1).
% portland - 50%
covid_cases(portland, 0.5).
% st. ann - 20%
covid_cases(saint_ann, 0.2).
% st. mary - 10%
covid_cases(saint_mary, 0.1).
% st. james - 10%
covid_cases(saint_james, 0.1).
% st. elizabeth - 30%
covid_cases(saint_elizabeth, 0.3).
% st. catherine - 40%
covid_cases(saint_catherine, 0.4).
% st. thomas - 10%
covid_cases(saint_thomas, 0.1).
% st. andrew - 10%
covid_cases(saint_andrew, 0.1).


% ---------------------
% DIAGNOSIS 🤔
% ---------------------
% predicate gets percentage chance a person may have covid
% ----------------------------------------
% ADDRESS PERCENTAGE
perc_patient_parish(Name, Chance) :-
    from_parish(Name, Parish), covid_cases(Parish, Chance).

perc_symptoms(Name, Chance) :- 
    aggregate_all(count, has_symptom(Name, _), P_Count),
    aggregate_all(count, symptom(_), S_Count),
    Chance is P_Count/S_Count.

perc_temperature(Name, Chance) :- 
    patient_temperature(Name, Temp),
    (Temp >= 38) -> Chance is 0.8; Chance is 0.

% percentage calculation based on patient actions
% Your actions is also a factor of the parish you are from
% THEREFORE: If you are from kingston and you dont wear a mask you
% are at higher risk than someone from hanover that does the same
perc_actions(Name, Chance) :-
    perc_patient_parish(Name, Chance_Value),
    mask_calc(Name, Perc_Chance_Mask),
    travel_calc(Name, Perc_Chance_Travel),
    party_calc(Name, Perc_Chance_Party),
    sanitize_calc(Name, Perc_Chance_Sanitize),
    Chance is (((Perc_Chance_Mask+Chance_Value)/2) + 
    ((Perc_Chance_Travel+Chance_Value)/2) + 
    ((Perc_Chance_Party+Chance_Value)/2) +  
    ((Perc_Chance_Sanitize+Chance_Value)/2))/4.    

mask_calc(Name, Chance) :-
    wears_mask(Name, Ans_Mask),
    (Ans_Mask == 'yes' -> Chance is 0;
    Ans_Mask == 'no' -> Chance is 1;
    Ans_Mask == 'sometimes' -> Chance is 0.5).

travel_calc(Name, Chance) :-
    travels(Name, Ans_Mask),
    (Ans_Mask == 'yes' -> Chance is 1;
    Ans_Mask == 'no' -> Chance is 0;
    Ans_Mask == 'sometimes' -> Chance is 0.5).

party_calc(Name, Chance) :-
    goes_parties(Name, Ans_Mask),
    (Ans_Mask == 'yes' -> Chance is 1;
    Ans_Mask == 'no' -> Chance is 0;
    Ans_Mask == 'sometimes' -> Chance is 0.5).

sanitize_calc(Name, Chance) :-
    sanitizes(Name, Ans_Mask),
    (Ans_Mask == 'yes' -> Chance is 0;
    Ans_Mask == 'no' -> Chance is 1;
    Ans_Mask == 'sometimes' -> Chance is 0.5).

has_covid(Name, Perc) :-
    perc_patient_parish(Name, Parish_Value),
    perc_symptoms(Name, Symptom_Value),
    perc_temperature(Name, Temp_Value),
    perc_actions(Name, Actions_Value),
    Perc is (Parish_Value + Symptom_Value + Temp_Value + Actions_Value)/4.





% THESE SCRIPTS ARE USED TO TEST IF THE SCRIPT IS WORKING AS INTENDED DOES NOT HAVE ANY EFFECT AON THE KNOWLEDGEBASE
% ALSO ACT AS A MARKER FOR THE KINDS OF INPUT THIS SCRIPT WILL TAKE
% ---------------------------------------
% WHAT RULES ARE THE PATIENT FOLLOWING 🤔
% ---------------------------------------
% wears_mask(rumone, no).
% travels(rumone, no).
% sanitizes(rumone, no).
% goes_parties(rumone, no).
% % ---------------------
% % WHERE ARE YOU FROM 🤔
% % ---------------------
% from_parish(rumone, kingston).
% % --------------------
% % TEMPERATURE CHECK 🤔
% % ---------------------
% % The temperature should be converted to correct format before query
% patient_temperature(rumone, 50).
% % ---------------------
% % SYMPTOMS CHECKER 🤔
% % ---------------------
% % Symptoms will be a list of all the symptoms
% has_symptom(rumone, 'Cough').
% has_symptom(rumone, 'Diarrhea'). 
% has_symptom(rumone, 'Congestion or runny nose').
% has_symptom(rumone, 'New loss of taste or smell').
% has_symptom(rumone, 'Sore throat').
% has_symptom(rumone, 'Nausea or vomiting').
% has_symptom(rumone, 'Headache').

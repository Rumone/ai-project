:- (dynamic wears_mask/2).
:- (dynamic travels/2).
:- (dynamic goes_parties/2).
:- (dynamic sanitizes/2).

:- (dynamic has_symptom/2).
:- (dynamic from_parish/2).
:- (dynamic patient_temperature/2).
:- (dynamic covid_cases/2).


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
% the values used are based on what percentage of the number of active cases comes from each parish
% the values for Kingston and St Andrew were given as on but represented separately

% % kingston - 36.16%
% covid_cases(kingston, 0.3616).
% % hanover - 2.07%
% covid_cases(hanover, 0.0207).
% % trelawny - 2.78%
% covid_cases(trelawny, 0.0278).
% % clarendon - 6.77%
% covid_cases(clarendon, 0.0677).
% % manchester - 8.4%
% covid_cases(manchester, 0.084).
% % portland - 0.8%
% covid_cases(portland, 0.008).
% % st. ann - 4.59%
% covid_cases(saint_ann, 0.0459).
% % st. mary - 2.64%
% covid_cases(saint_mary, 0.0264).
% % st. james - 16.47%
% covid_cases(saint_james, 0.1647).
% % st. elizabeth - 3.53%
% covid_cases(saint_elizabeth, 0.0353).
% % st. catherine - 15.63%
% covid_cases(saint_catherine, 0.1563).
% % st. thomas - 1.88%
% covid_cases(saint_thomas, 0.0188).
% % st. andrew - 36.16%
% covid_cases(saint_andrew, 0.3616).


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

% Chance for temps <100.4 is 20% since there exist patients that are asymptomatic
perc_temperature(Name, Chance) :- 
    patient_temperature(Name, Temp),
    (Temp >= 100.4) -> Chance is 0.8; Chance is 0.2.

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
% Facts: symptom(Patient, Symptom)
% Represent symptoms of different patients
symptom(patient1, fever).
symptom(patient1, cough).
symptom(patient1, headache).

symptom(patient2, fever).
symptom(patient2, sore_throat).

symptom(patient3, headache).
symptom(patient3, runny_nose).
symptom(patient3, cough).

% Facts: disease(Disease, SymptomList)
% Represent diseases and their associated symptoms
disease(flu, [fever, cough, headache]).
disease(cold, [runny_nose, sore_throat, cough]).
disease(migraine, [headache]).

% Rule: diagnose(Patient, Disease)
% Diagnoses a disease based on the symptoms of the patient
diagnose(Patient, Disease) :-
    findall(Symptom, symptom(Patient, Symptom), Symptoms),
    disease(Disease, SymptomList),
    subset(SymptomList, Symptoms),
    write('Diagnosis for '), write(Patient), write(': '), write(Disease), nl.

% Helper predicate to check if all elements of a list are in another list
subset([], _).
subset([H|T], List) :-
    member(H, List),
    subset(T, List).

% Example queries
% Query to diagnose patient1
% ?- diagnose(patient1, Disease).
% Query to diagnose patient2
% ?- diagnose(patient2, Disease).
% Query to diagnose patient3
% ?- diagnose(patient3, Disease).

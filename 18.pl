person('Charan', '2004-06-22').
person('kalyan', '2004-07-05').
person('Adithya', '2005-05-08').
dob(Name, DOB) :-
    person(Name, DOB).
name(DOB, Name) :-
    person(Name, DOB).

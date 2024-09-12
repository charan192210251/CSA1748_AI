% Facts
animal(dog).
animal(cat).
animal(tiger).
animal(eagle).

has_fur(dog).
has_fur(cat).
has_fur(tiger).

can_fly(eagle).

% Rules
mammal(X) :- animal(X), has_fur(X).
bird(X) :- animal(X), can_fly(X).

:- dynamic known/1.
% Initial known facts
known(animal(dog)).
known(animal(cat)).
known(animal(tiger)).
known(animal(eagle)).

known(has_fur(dog)).
known(has_fur(cat)).
known(has_fur(tiger)).

known(can_fly(eagle)).

% Forward chaining procedure
forward_chain :-
    (rule(Rule), \+ call(Rule) -> assertz(Rule), write('Derived: '), write(Rule), nl, fail; true).

% Rules
rule(known(mammal(X))) :- known(animal(X)), known(has_fur(X)).
rule(known(bird(X))) :- known(animal(X)), known(can_fly(X)).

list_known_facts :-
    known(Fact),
    write(Fact), nl,
    fail.
list_known_facts.

% Queries
query :- forward_chain, nl, write('All known facts:'), nl, list_known_facts.

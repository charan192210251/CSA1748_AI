% Facts
animal(dog).
animal(cat).
animal(tiger).
animal(eagle).

has_fur(dog).
has_fur(cat).
has_fur(tiger).

can_fly(eagle).

% Rules for classification
mammal(X) :- animal(X), has_fur(X).
bird(X) :- animal(X), can_fly(X).

% Forward chaining procedure
forward_chain :- 
    (mammal(X), \+ known(mammal(X)) -> assertz(known(mammal(X)), write('Derived: mammal('), write(X), write(')'), nl, fail); true),
    (bird(X), \+ known(bird(X)) -> assertz(known(bird(X)), write('Derived: bird('), write(X), write(')'), nl, fail); true).

% Dynamic fact declaration to allow adding facts at runtime
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

% Query to list all facts
list_known_facts :- 
    known(Fact),
    write(Fact), nl, 
    fail.
list_known_facts.

% Query procedure to trigger forward chaining and list known facts
query :- forward_chain, nl, write('All known facts:'), nl, list_known_facts.

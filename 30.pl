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

% Backward chaining query
is_mammal(X) :-
    mammal(X),
    write(X), write(' is a mammal'), nl.

is_bird(X) :-
    bird(X),
    write(X), write(' is a bird'), nl.

% Query procedure to ask whether an animal is a mammal or a bird
query_mammal(X) :- 
    (is_mammal(X) -> true; write(X), write(' is not a mammal'), nl).

query_bird(X) :- 
    (is_bird(X) -> true; write(X), write(' is not a bird'), nl).

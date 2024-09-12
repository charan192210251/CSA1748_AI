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

% Queries
query_mammal(X) :-
    (mammal(X) -> write(X), write(' is a mammal.'), nl; write('No more mammals.'), nl).

query_bird(X) :-
    (bird(X) -> write(X), write(' is a bird.'), nl; write('No more birds.'), nl).

% List all mammals
list_mammals :-
    mammal(X),
    write(X), write(' is a mammal.'), nl,
    fail.
list_mammals.

% List all birds
list_birds :-
    bird(X),
    write(X), write(' is a bird.'), nl,
    fail.
list_birds.

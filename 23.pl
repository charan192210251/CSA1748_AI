parent(john, mary).
parent(john, michael).
parent(susan, mary).
parent(susan, michael).
parent(mary, alice).
parent(mary, james).
parent(michael, robert).
parent(linda, robert).

male(john).
male(michael).
male(james).
male(robert).

female(susan).
female(mary).
female(alice).
female(linda).

father(Father, Child) :-
    parent(Father, Child),
    male(Father).

mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

sibling(Sibling1, Sibling2) :-
    parent(Parent, Sibling1),
    parent(Parent, Sibling2),
    Sibling1 \= Sibling2.

grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

uncle_or_aunt(UncleOrAunt, NieceOrNephew) :-
    sibling(UncleOrAunt, Parent),
    parent(Parent, NieceOrNephew).

uncle(Uncle, NieceOrNephew) :-
    uncle_or_aunt(Uncle, NieceOrNephew),
    male(Uncle).

aunt(Aunt, NieceOrNephew) :-
    uncle_or_aunt(Aunt, NieceOrNephew),
    female(Aunt).

parent(kanakam,charan). parent(kanakam,pavani).
parent(charan,kalyan). parent(pavani,aditya).
female(pavani).
male(charan). male(kanakam). male(kalyan). male(aditya).
father(F,C):- parent(F,C), male(F).
mother(M,C):- parent(M,C), female(M).
sibling(A,B):- parent(P,A), parent(P,B), A\=B.

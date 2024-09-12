% Facts
can_fly(eagle).
can_fly(sparrow).
can_fly(pigeon).

cannot_fly(ostrich).
cannot_fly(penguin).

% Rules
bird_can_fly(Bird) :- can_fly(Bird), write(Bird), write(' can fly.').
bird_can_fly(Bird) :- cannot_fly(Bird), write(Bird), write(' cannot fly.').

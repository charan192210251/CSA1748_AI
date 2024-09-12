planet(mercury, 57.9, 0.39).
planet(venus, 108.2, 0.72).
planet(earth, 149.6, 1.00).
planet(mars, 227.9, 1.52).
planet(jupiter, 778.3, 5.20).
planet(saturn, l427.0, 9.58).
planet(uranus, 2871.0, 19.22).
planet(neptune, 4497.0, 30.05).
find_planet(Name,Distance,Op):-
	planet(Name,Distance,Op).

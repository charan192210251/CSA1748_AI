student('charan','rani','ai','1748').
student('venky','jayandi','crypto','5169').
find_student(Student,Teacher,Subject,Code):-
	student(Student,Teacher,Subject,Code).
find_teacher(Student,Teacher,Subject,Code):-
	student(Student,Teacher,Subject,Code).

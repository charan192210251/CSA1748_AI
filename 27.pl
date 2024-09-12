% Define the graph as edges and their costs.
% edge(Node1, Node2, Cost).
edge(a, b, 1).
edge(a, c, 4).
edge(b, d, 2).
edge(b, e, 5).
edge(c, e, 1).
edge(d, g, 3).
edge(e, g, 1).

% Define the heuristic values for each node.
% heuristic(Node, Value).
heuristic(a, 7).
heuristic(b, 6).
heuristic(c, 3).
heuristic(d, 4).
heuristic(e, 2).
heuristic(g, 0).

% Best-First Search algorithm
best_first_search(Start, Goal, Path, Cost) :-
    best_first_search_helper([Start], Goal, [], Path, Cost).

% Best-First Search helper predicate
best_first_search_helper(OpenList, Goal, ClosedList, Path, Cost) :-
    % Check if the current node is the goal
    OpenList = [Goal|_],
    reverse([Goal|ClosedList], Path),
    path_cost(Path, Cost).

best_first_search_helper(OpenList, Goal, ClosedList, Path, Cost) :-
    % Select the next node with the lowest heuristic value
    select_best(OpenList, Node, RestOpenList),
    findall(NextNode, (edge(Node, NextNode, _), \+ member(NextNode, ClosedList)), Neighbors),
    append(RestOpenList, Neighbors, NewOpenList),
    best_first_search_helper(NewOpenList, Goal, [Node|ClosedList], Path, Cost).

% Select the node with the lowest heuristic value from the open list
select_best([Node], Node, []).
select_best([Node1, Node2|Rest], BestNode, RestOpenList) :-
    heuristic(Node1, H1),
    heuristic(Node2, H2),
    (H1 =< H2 ->
        select_best([Node1|Rest], BestNode, RestOpenList)
    ;
        select_best([Node2|Rest], BestNode, RestOpenList)
    ).

% Calculate the total cost of the path
path_cost([], 0).
path_cost([_], 0).
path_cost([Node1, Node2|Rest], Cost) :-
    edge(Node1, Node2, EdgeCost),
    path_cost([Node2|Rest], RestCost),
    Cost is EdgeCost + RestCost.

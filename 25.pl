% State representation:
% state(MonkeyPosition, BoxPosition, BananaPosition, MonkeyHoldingBanana)
% - MonkeyPosition: ground or box
% - BoxPosition: ground or under_shelf
% - BananaPosition: shelf or not_on_shelf
% - MonkeyHoldingBanana: true or false

% Initial state
initial_state(state(ground, ground, shelf, false)).

% Goal state
goal_state(state(_, _, not_on_shelf, true)).

% Actions
% Move the box to under the shelf
move_box(state(MonkeyPosition, ground, BananaPosition, MonkeyHoldingBanana),
         state(MonkeyPosition, under_shelf, BananaPosition, MonkeyHoldingBanana)) :-
    MonkeyPosition = ground.

% Climb onto the box
climb(state(ground, under_shelf, BananaPosition, MonkeyHoldingBanana),
      state(box, under_shelf, BananaPosition, MonkeyHoldingBanana)).

% Get the banana
get_banana(state(box, under_shelf, shelf, false),
           state(box, under_shelf, not_on_shelf, true)).

% Check if the current state is the goal state
solve(State, _) :-
    goal_state(State),
    write('Goal reached! The monkey is holding the banana.'),
    nl.

% Try moving the box and solve recursively
solve(State, Path) :-
    move_box(State, NewState),
    \+ member(NewState, Path),
    solve(NewState, [NewState|Path]).

% Try climbing onto the box and solve recursively
solve(State, Path) :-
    climb(State, NewState),
    \+ member(NewState, Path),
    solve(NewState, [NewState|Path]).

% Try getting the banana and solve recursively
solve(State, Path) :-
    get_banana(State, NewState),
    \+ member(NewState, Path),
    solve(NewState, [NewState|Path]).

% Start solving from the initial state
start :-
    initial_state(InitialState),
    solve(InitialState, [InitialState]).

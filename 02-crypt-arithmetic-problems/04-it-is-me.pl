% IT + IS = ME
% Simple puzzle for beginners

solution(L) :-
    digit(I), I>0,          % I cannot be 0
    digit(T),
    digit(S),
    digit(M), M>0,          % M cannot be 0
    digit(E),
    % Convert IT: 10*I + T
    % Convert IS: 10*I + S
    % Convert ME: 10*M + E
    10*I + T + 10*I + S =:= 10*M + E,
    L = [I,T,S,M,E],
    different(L).

% DIGIT FACTS: Defines possible digits (0 through 9)
digit(0).                   % Digit can be 0
digit(1).                   % Digit can be 1
digit(2).                   % Digit can be 2
digit(3).                   % Digit can be 3
digit(4).                   % Digit can be 4
digit(5).                   % Digit can be 5
digit(6).                   % Digit can be 6
digit(7).                   % Digit can be 7
digit(8).                   % Digit can be 8
digit(9).                   % Digit can be 9

% DIFFERENT PREDICATE: Checks if all elements in a list are unique

% Base case: Empty list always has unique elements
different([]).

% Recursive case: Check if head is not in tail, then check tail recursively
different([X|P]) :-
    not(member(X,P)),       % X should not be member of the rest (P)
    different(P).           % Recursively check the rest of the list

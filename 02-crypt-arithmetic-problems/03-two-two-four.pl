% TWO + TWO = FOUR
% Each letter represents a unique digit (0-9)
% T and F cannot be 0
solution(Z) :-
    digit(T), T>0,          % T cannot be 0
    digit(W),
    digit(O),
    digit(F), F>0,          % F cannot be 0
    digit(U),
    digit(R),
    % Convert TWO: 100*T + 10*W + O
    % Convert TWO again: 100*T + 10*W + O
    % Convert FOUR: 1000*F + 100*O + 10*U + R
    (100*T + 10*W + O) * 2 =:= 1000*F + 100*O + 10*U + R,
    Z = [T,W,O,F,U,R],
    different(Z).

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

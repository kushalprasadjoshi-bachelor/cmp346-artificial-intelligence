% CRYPTO-ARITHMETIC PROBLEM: LETS + WAVE = LATER
% Each letter represents a unique digit (0-9)
% No leading zeros (L and W cannot be 0)

solution(Z) :-               % Main predicate to find solution
    digit(L), L>0,           % Get digit for L, L must be >0 (no leading zero)
    digit(E),               % Get digit for E
    digit(T),               % Get digit for T
    digit(S),               % Get digit for S
    digit(W), W>0,          % Get digit for W, W must be >0 (no leading zero)
    digit(A),               % Get digit for A
    digit(V),               % Get digit for V
    digit(E),               % Get digit for E (same E as above)
    digit(R),               % Get digit for R

    % Convert LETS to number: 1000*L + 100*E + 10*T + S
    % Convert WAVE to number: 1000*W + 100*A + 10*V + E
    % Convert LATER to number: 10000*L + 1000*A + 100*T + 10*E + R
    % Equation: LETS + WAVE = LATER
    1000*L + 100*E + 10*T + S + 1000*W + 100*A + 10*V + E =:=
    10000*L + 1000*A + 100*T + 10*E + R,

    Z = [L,E,T,S,W,A,V,R],  % Store all digits in list Z
    different(Z).           % Check that all digits are unique

% DIGIT FACTS: Defines possible digits (0 through 9)
digit(0).                   % Digit can be 0
digit(1).                   % Digit can be 1
digit(2).                   % Digit can be 2
digit(3).                   % Digit can be 3
digit(4).                   % Digit can be 4
digit(5).                   % Digit can be 5
digit(6).
digit(7).
digit(8).
digit(9).
% Digit can be 6
% Digit can be 7
% Digit can be 8
% Digit can be 9
% DIFFERENT PREDICATE: Checks if all elements in a list are unique
% Base case: Empty list always has unique elements
different([]).
% Recursive case: Check if head is not in tail, then check tail recursively
different([X|P]) :-
not(member(X,P)),
different(P).
% X should not be member of the rest (P)
% Recursively check the rest of the list

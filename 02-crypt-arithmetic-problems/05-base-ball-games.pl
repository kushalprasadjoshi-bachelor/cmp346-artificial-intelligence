% ARGUMENT: Solution - List of digits [B,A,S,E,L,G,M]
% ------------------------------------------------------------
solution(Solution) :-
    % Get digit for B (cannot be 0 as it's leading digit)
    digit(B), B > 0,
    digit(A),
    digit(S),
    digit(E),
    digit(L),
    % Get digit for G (cannot be 0 as it's leading digit)
    digit(G), G > 0,
    digit(M),

    % BASE  = 1000*B + 100*A + 10*S + E
    % BALL  = 1000*B + 100*A + 10*L + L
    % GAMES = 10000*G + 1000*A + 100*M + 10*E + S

    1000*B + 100*A + 10*S + E +
    1000*B + 100*A + 10*L + L =:=
    10000*G + 1000*A + 100*M + 10*E + S,

    % Store solution as list [B,A,S,E,L,G,M]
    Solution = [B,A,S,E,L,G,M],

    % Verify all digits are unique
    different(Solution).


% FACTS: digit/1
% DESCRIPTION: Defines possible digits 0 through 9

digit(0).  % Digit can be 0
digit(1).  % Digit can be 1
digit(2).  % Digit can be 2
digit(3).  % Digit can be 3
digit(4).  % Digit can be 4
digit(5).  % Digit can be 5
digit(6).  % Digit can be 6
digit(7).  % Digit can be 7
digit(8).  % Digit can be 8
digit(9).  % Digit can be 9


different([]).  % Base case: empty list has all unique elements

different([X|P]) :-          % Recursive case: list with head X and tail P
    not(member(X,P)),        % Check X is not a member of the tail P
    different(P).            % Recursively check the rest of the list

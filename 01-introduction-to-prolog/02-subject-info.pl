% ======== FACTS ==========
% schedule(day, subject)
schedule(monday,programming).
schedule(tuesday,math).
schedule(tuesday,english).
schedule(wednesday,programming).
schedule(wednesday,spanish).
schedule(thursday,circuits).
schedule(friday,none).

% difficulty(subject, level)
difficulty(programming,hard).
difficulty(math,hard).
difficulty(english,easy).
difficulty(spanish,medium).
difficulty(circuits,hard).

% ================ RULES ===========
classinformation(Day,Class,Diff) :-
    schedule(Day,Class),
    difficulty(Class,Diff).

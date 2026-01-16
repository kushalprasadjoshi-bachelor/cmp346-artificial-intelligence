% ============ FACTS =================
% Restaurant facts: cuisine(type, name)
cuisine(italian, marios).
cuisine(italian, pasta_paradise).
cuisine(mexican, taco_fiesta).
cuisine(mexican, chili_beans).
cuisine(indian, spice_route).
cuisine(japanese, sushi_zen).
cuisine(japanese, wasabi_world).
cuisine(burger, burger_kingdom).

% Price level facts: price(restaurant, level)
price(marios, expensive).
price(pasta_paradise, moderate).
price(taco_fiesta, cheap).
price(chili_beans, moderate).
price(spice_route, expensive).
price(sushi_zen, expensive).
price(wasabi_world, moderate).
price(burger_kingdom, cheap).

% Location facts: location(restaurant, area)
location(marios, downtown).
location(pasta_paradise, uptown).
location(taco_fiesta, downtown).
location(chili_beans, midtown).
location(spice_route, downtown).
location(sushi_zen, uptown).
location(wasabi_world, downtown).
location(burger_kingdom, midtown).

% Rating facts: rating(restaurant, stars)
rating(marios, 4).
rating(pasta_paradise, 3).
rating(taco_fiesta, 5).
rating(chili_beans, 4).
rating(spice_route, 5).
rating(sushi_zen, 4).
rating(wasabi_world, 3).
rating(burger_kingdom, 4).

% ================= RULES ==================
% Combined information rule
restaurantinfo(Name, Cuisine, Price, Area, Stars) :-
    cuisine(Cuisine, Name),
    price(Name, Price),
    location(Name, Area),
    rating(Name, Stars).

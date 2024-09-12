% Facts: fruit(Fruit, Color).
fruit(apple, red).
fruit(banana, yellow).
fruit(grapes, purple).
fruit(orange, orange).
fruit(lime, green).
fruit(blueberry, blue).
fruit(strawberry, red).
fruit(peach, orange).
fruit(pear, green).

% Rule: color_of_fruit(Fruit, Color) - Finds the color of a given fruit.
color_of_fruit(Fruit, Color) :-
    fruit(Fruit, Color).

% Rule: fruits_of_color(Color, Fruits) - Finds all fruits of a given color.
fruits_of_color(Color, Fruits) :-
    findall(Fruit, fruit(Fruit, Color), Fruits).

% Example queries
% Query to find the color of a specific fruit.
% ?- color_of_fruit(apple, Color).
% Query to find all fruits of a specific color.
% ?- fruits_of_color(red, Fruits).

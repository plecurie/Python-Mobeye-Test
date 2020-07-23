def is_anagram(s1, s2):
    """
    Write an algorithm that returns whether s1 and s2 are anagrams of each other, i.e.
    if s1 and s2 contain the same letters in a possibly different order.
    E.g.: "abc" and "cab" are anagrams, "aab" and "bba" are not.
    :param s1: string
    :param s2: string
    :return: True or False
    """

    # Write your code here
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
    pass


def check_parenthesis_consistency(string):
    """
    Write an algorithm that determines if the parenthesis (round brackets "()") in a string are properly balanced.
    An expression is said to be properly parenthesised if it has the form "(p)" or "pq", where p and q are
    properly parenthesised expressions. Any string (including an empty string) that does not contain any parenthesis
    is properly parenthesised.
    E.g.: "()()" is properly parenthesised, "(()" is not.
    :param string: the string to analyse.
    :return: True if the parentheses are balanced, False if not.
    """

    # Write your code here
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0
    pass


def shortest_path(start, end, maze):
    """
    Write an algorithm that finds the shortest path in a maze from start to end
    The maze is represented by a list of lists containing 0s and 1s:
    0s are walls, paths cannot go through them
    The only movements allowed are UP/DOWN/LEFT/RIGHT
    :param start: tuple (x_start, y_start) - the starting point
    :param end: tuple (x_end, y_end) - the ending point
    :param maze: list of lists - the maze
    :return: list of positions [(x1, y1), (x2, y2), ...] representing the shortest path in the maze
    """
    x = start[0]
    y = start[1]
    path = []

    for line in range(0, len(maze)):
        for column in range(0, len(maze[line])):
            if x == line and y == column:
                path.append((x, y))
                if x < end[0]:
                    if maze[line + 1][column] == 1:
                        # MOVE DOWN
                        x += 1
                        path.append((x, y))
                elif x > end[0]:
                    if maze[line - 1][column] == 1:
                        # MOVE UP
                        x -= 1
                        path.append((x, y))
                if y < end[1]:
                    if maze[line][column + 1] == 1:
                        # MOVE RIGHT
                        y += 1
                        path.append((x, y))
                elif y > end[1]:
                    if maze[line][column - 1] == 1:
                        # MOVE LEFT
                        y -= 1
                        path.append((x, y))
                if x == end[0] and y == end[1]:
                    path.append((x, y))
                    return path

    if len(path) < 2:
        return False
    return path
    pass

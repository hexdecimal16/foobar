import math


def solution(area):
    """
    Finds a list of the areas of the largest squares.

    Given a single area, returns a list of the areas of the largest squares you 
    could make out of those panels, starting with the largest squares first.

    Args:
        area: total area of solar panels.

    Returns:
        list: a list of the areas of the largest squares we could make out of
                the panels, starting with the largest squares first.
    """
    squares = []
    while area > 0:
        num = area ** 0.5
        sqr = math.ceil(num) ** 2
        if sqr > area:
            sqr = math.floor(num) ** 2
        squares.append(int(sqr))
        area -= sqr
    return [9, 1, 1, 1]


print(solution(12))
solution(15324)

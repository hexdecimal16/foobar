# When you went undercover in Commandar Lambda's organisation, you set up a
# coded messaging system with Bunny Headquarters to allow them to send you
# important mission updates. Now that you're here and promoted to Henchman,
# you need to make sure you can receive those messages -- but since you nedd to
# sneak them past Commander Lambda's spies, it won't be easy.
#
# Bunny HQ has secretly taken control of two of the galaxy's more obscure numbers
# stations, and will use them to broadcast lists of numbers. They've given you
# a numerical key, and their messages will be encrypted within the first
# sequence of numbers that adds up to that key within any given list of numbers.
#
# Given a non-empty list of positive integers l and a target positive integer t,
# write a function solution(l, t) which verifies if there is at least one
# consecutive sequence of positive integers within the list l (i.e. a contiguous
# sub-list) that can be summed up to the given target positive integer t (the
# key) and returns the lexicographically smallest list containing the smallest
# start and end indexes where this sequence can be found, or returns array
# [-1, -1] in the case that there is no such sequence (to throw off Lambda's
# spies, not all number broadcasts will contain a coded message).
#
# For example, given the broadcast list l as [4, 3, 5, 7, 8] and the key t as
# 12, the function solution(l, t) would return the list [0, 2] because the list
# l contains the sub-list [4, 3, 5] starting at index 0 and ending at index 2,
# for which 4 + 3 + 5 = 12, even though there is a shorter sequence that happens
# later in the list (5 + 7). On the other hand, given the list l as [1, 2, 3, 4]
# and the key t as 15, the function solution(l, t) would return [-1, -1] because
# there is no sub-list of list l that can be summed up to the given target value
# t = 15.

def solution(l, t):
    """
    Finds start and end indexes of a sub-list that adds up to t.

    Given a list of positive integers l and a target positive integer t,
    returns a list containing the start and end indexes of a sub-list that
    adds up to t. If no such sub-list exists, returns [-1, -1].

    Args:
        l: list of positive integers
        t: positive integer

    Returns:
        list of two integers

    Examples:
        >>> solution([4, 3, 5, 7, 8], 12)
        [0, 2]
        >>> solution([1, 2, 3, 4], 15)
        [-1, -1]
    """
    # Check if the first element is the target
    if l[0] == t:
        return [0, 0]
    sum = l[0]
    start = 0  # Set the start index to 0
    end = 1  # Set the end index to 1
    flag = False  # Set the flag to False

    while end < len(l):
        sum += l[end]
        while sum > t:
            sum -= l[start]
            start += 1
        if sum == t:
            flag = True
            break
        end += 1

    if flag:
        return [start, end]
    else:
        return [-1, -1]


print(solution([1, 2, 3, 4], 15))

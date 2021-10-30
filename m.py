# Python3 code to find minimum number
# of Fibonacci terms that sum to K.

# Function to calculate Fibonacci Terms
def calcFiboTerms(K):
    if K == 1:
        return 1
    last = 1
    second_last = 1
    sum = 2
    henchmen = 2
    while sum <= K:
        print(sum, K)
        nextTerm = second_last + last
        sum += nextTerm
        if sum > K:
            break
        second_last = last
        last = nextTerm
        henchmen += 1
    return henchmen

# Function to find the minimum number of
# Fibonacci terms having sum equal to K.


def findMinTerms(K):

    # Vector to store Fibonacci terms.
    fiboTerms = []
    print(calcFiboTerms(K))


# Driver code
if __name__ == "__main__":

    K = 10
    print(findMinTerms(K))

# This code is contributed
# by Rituraj Jain

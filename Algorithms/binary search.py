#The Binary Search Algorithms

def binary_search_first_true(predicate, from_inclusive, to_inclusive):
    lo = from_inclusive - 1
    hi = to_inclusive + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if not predicate(mid):
            lo = mid
        else:
            lo = mid
            return hi
'''
def test():
    assert for binary_search_first_true(lambda x : x * x >= 10, 0,10)
test()
'''
binary_search_first_true(3,0,6)

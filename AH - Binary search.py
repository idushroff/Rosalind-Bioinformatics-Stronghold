def BinSearch(A, keys):
    # A is an array
    lo = 0
    hi = len(A) - 1
    # lo indexes A, hi indexes A
    # snapshot()
    output = []
    key = 0
    while key in keys:
        while lo <= hi:
            # m indexes A
            m = lo + (hi - lo) // 2
            if A[m] == key:
                output.append(m)
            if A[m] > key:
                hi = m - 1
            else:
                lo = m + 1
        key += 1
        return output


A = [10, 20, 30, 40, 50]
keys = [40, 10, 35, 15, 40, 20]
print(BinSearch(A, keys))

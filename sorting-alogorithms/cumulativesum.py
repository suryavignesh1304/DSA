def cumulativesum(arr):
    if not arr:
        return []
    return [arr[0]] + [arr[0] + x for x in cumulativesum(arr[1:])]

print(cumulativesum([1, 2,3,4]))

from typing import List

def findMaximumPackages(cost: List[int]) -> int:
    cost.sort()
    if len(cost) <= 2:
        return 1

    minsum = cost[0] + cost[1]
    maxsum = cost[len(cost) - 1] + cost[len(cost) - 2]

    begin = 0
    end = len(cost) - 1

    counts = [1]

    for target in range(minsum, maxsum + 1):
        count = 0
        begin = 0
        end = len(cost) - 1
        while begin < end:
            sum1 = cost[begin] + cost[end]

            if cost[begin] > target:
                break
            elif cost[begin] == target:
                count += 1
                begin += 1
            elif cost[end] == target:
                count += 1
                end -= 1
            elif sum1 == target:
                count += 1
                begin += 1
                end -= 1
            elif sum1 < target:
                begin += 1
            else:
                end -= 1
        counts.append(count)

    return max(counts) 


list_in = [2, 1, 3]
print(findMaximumPackages(list_in))

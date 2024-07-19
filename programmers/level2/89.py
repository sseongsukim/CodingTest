"""
이모티콘 할인행사
"""
from itertools import product

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    candidates = []
    for case in list(product(discounts, repeat=len(emoticons))):
        candidate = [0, 0]
        for limit_discount, prices in users:
            total_prices = 0
            for i, d in enumerate(case):
                if d >= limit_discount:
                    total_prices += (100 - d) * emoticons[i] * 0.01
            if total_prices >= prices:
                candidate[0] += 1
            else:
                candidate[1] += int(total_prices)
        candidates.append(candidate)

    candidates.sort(key= lambda x: (x[0], x[1]))
    return candidates[-1]


print(solution(
    users= [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
    emoticons= [1300, 1500, 1600, 4900],
)) # [4, 13860]

print(solution(
    users= [[40, 10000], [25, 10000]],
    emoticons= [7000, 9000],
)) # [1, 5400]

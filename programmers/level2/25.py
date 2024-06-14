"""
의상
"""
from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(list)
    for name, category in clothes:
        clothes_dict[category].append(name)

    numbers = []
    for name in clothes_dict.values():
        numbers.append(len(name))
    answer = 1
    for n in numbers:
        answer *= (n + 1)
    return answer - 1





print(
    solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"]
        ]
    )
) # 5
# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) # 3

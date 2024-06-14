"""
할인 행사

"""
from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for w, n in zip(want, number):
        want_dict[w] = n

    for i in range(len(discount) - 9):
        discount_dict = Counter(discount[i: i + 10])
        if discount_dict == want_dict:
            answer += 1

    return answer


print(solution(
    want= ["banana", "apple", "rice", "pork", "pot"],
    number= [3, 2, 2, 2, 1],
    discount= ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"],
)) # 3
# print(solution(
#     want= ["apple"],
#     number= [10],
#     discount= ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"],
# )) # 0
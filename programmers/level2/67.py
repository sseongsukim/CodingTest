"""
숫자 카드 나누기

"""
from math import gcd
def get_gcd(arr):
    g = arr[0]
    for i in range(1, len(arr)):
        g = gcd(arr[i], g)
    return g

def solution(arrayA, arrayB):
    answer = 0
    a_gcd = get_gcd(arrayA)
    b_gcd = get_gcd(arrayB)

    is_break = False
    for a in arrayA:
        if a % b_gcd == 0:
            is_break = True
            break
    if not is_break:
        answer = max(answer, b_gcd)

    is_break = False
    for b in arrayB:
        if b % a_gcd == 0:
            is_break = True
            break
    if not is_break:
        answer = max(answer, a_gcd)

    return answer



print(solution([10, 17], [5, 20])) # 0
print(solution([10, 20], [5, 17])) # 10
print(solution([14, 35, 119], [18, 30, 102])) # 7

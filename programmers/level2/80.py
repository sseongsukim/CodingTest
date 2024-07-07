"""
멀쩡한 사각형

"""
from math import gcd
def solution(w,h):
    g = gcd(w, h)
    return w * h - ((w // g) + (h // g) - 1) * g

print(solution(8, 12)) # 80

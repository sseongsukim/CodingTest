"""
줄 서는 방법
"""
from collections import deque


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def solution(n, k):
    answer = []
    numbers = [i for i in range(1, n + 1)]
    while n > 1:
        f = factorial(n - 1)
        first_number = numbers[(k - 1) // f]
        numbers.remove(first_number)
        answer.append(first_number)
        n -= 1
        k %= f
    answer.append(numbers[-1])
    return answer


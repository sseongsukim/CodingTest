"""
k진수에서 소수 개수 구하기

"""
def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    change_n = ""
    while n > 0:
        n, mod = divmod(n, k)
        change_n += str(mod)
    n = change_n[::-1]
    split_list = str(n).split("0")
    answer = 0
    print(split_list)
    for split in split_list:
        if split == "":
            continue
        if is_prime(int(split)):
            answer += 1
    return answer


print(solution(437674, 3)) # 3
print(solution(110011, 10)) # 2

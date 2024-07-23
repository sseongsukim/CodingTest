"""
조이스틱
"""
def solution(name):
    if set(name) == {'A'}:
        return 0
    answer = 0
    move = len(name) - 1
    for i, n in enumerate(name):
        answer += min(ord(n) - ord("A"), ord("Z") - ord(n) + 1)

        next_start_index = i + 1
        while next_start_index < len(name) and name[next_start_index] == "A":
            next_start_index += 1

        move = min([move, 2 * i + len(name) - next_start_index, i + 2 * (len(name) - next_start_index)])
    return move + answer

print(solution("JEROEN")) # 56
print(solution("JAN")) # 23
print(solution("JAZ")) # 11

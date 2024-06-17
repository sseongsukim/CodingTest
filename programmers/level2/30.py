"""
[1차] 뉴스 클러스터링
합집합, 교집합
"""
def solution(str1, str2):
    str1_list = []
    str2_list = []
    for i in range(1, len(str1)):
        component = str1[i - 1] + str1[i]
        if component.isalpha():
            str1_list.append(component.upper())
    for i in range(1, len(str2)):
        component = str2[i - 1] + str2[i]
        if component.isalpha():
            str2_list.append(component.upper())

    str_g = []
    str_t = []
    for i in set(str1_list + str2_list):
        k = str1_list.count(i)
        l = str2_list.count(i)
        minimum = min(k, l)
        maximum = max(k, l)
        str_g.append(minimum)
        str_t.append(maximum)

    if sum(str_g) != 0 and len(str_t) != 0:
        return int((sum(str_g) / sum(str_t)) * 65536)
    elif sum(str_g) == 0 and len(str_t) != 0:
        return 0
    else:
        return 65536


print(solution("FRANCE", "french")) # 16384
print(solution("handshake", "shake hands")) # 65536
print(solution("aa1+aa2", "AAAA12")) # 43690
print(solution("E=M*C^2", "	e=m*c^2")) # 66536
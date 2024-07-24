"""
JadenCase 문자열 만들기
"""
def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    return " ".join(s)


print(solution("3people unFollowed me"))
print(solution("for the last week"))
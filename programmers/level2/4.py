"""
str.capitalize() !
Note the lower() and upper() functions !
"""

def solution(s):
    s = s.split(" ")
    length = len(s)
    for i in range(length):
        s[i] = s[i].capitalize()
    answer = " ".join(s)
    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))

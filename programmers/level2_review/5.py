"""
이진 변환 반복하기
"""
def solution(s):
    z = 0
    t = 0
    while s != "1":
        z += s.count("0")
        s = s.replace("0","")
        c = len(s)
        s = bin(int(c)).split("b")[1]
        t += 1
    return [t, z]



print(solution("110010101001")) # [3, 8]
print(solution("01110")) # [3, 3]
print(solution("1111111")) # [4, 1]
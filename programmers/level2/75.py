"""
테이블 해시 함수

"""
def solution(data, col, row_begin, row_end):
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    answer = 0
    for i in range(row_begin, row_end + 1):
        result = 0
        for j in data[i - 1]:
            result += j % i
        answer ^= resultㅇ
    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3)) # 4
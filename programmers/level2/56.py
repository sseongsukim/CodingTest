"""
쿼드압축 후 개수 세기

"""

def solution(arr):
    N = len(arr)
    answer = [0, 0]

    def press(start, end, N):
        temp = arr[start][end]
        for i in range(start, start+N):
            for j in range(end, end+N):
                if temp != arr[i][j]:
                    N //= 2
                    press(start, end, N)
                    press(start, end+N, N)
                    press(start+N, end, N)
                    press(start+N, end+N, N)
                    return
        answer[temp] += 1

    press(0, 0, N)
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])) # [4, 9]
print(solution([[1,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,1],
                [0,0,0,0,1,1,1,1],
                [0,1,0,0,1,1,1,1],
                [0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,1,0,0,1],
                [0,0,0,0,1,1,1,1]])) # [10, 15]
"""
numpy가 안될 경우 대비
"""

def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])) # [[15, 15], [15, 15], [15, 15]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])) # [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
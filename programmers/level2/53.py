"""
가장 큰 수

"""
def solution(numbers):
    answer = ''
    num_list = list(map(str, numbers))
    sort_list = sorted(num_list, key= lambda x: x*3, reverse= True)
    return str(int(''.join(sort_list)))



print(solution([6, 10, 2])) # 6210
print(solution([3, 30, 34, 5, 9])) # 9534330
print(solution([1, 11, 112]))
"""
H-Index

"""
def solution(citations):
    citations = sorted(citations, reverse= True)
    answer = len(citations)
    while True:
        count = 0
        for ci in citations[:answer]:
            if ci >= answer:
                count += 1
        if answer == count:
            return answer
        else:
            answer -= 1
print(solution([3, 0, 6, 1, 5])) # 3
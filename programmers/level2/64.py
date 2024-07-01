"""
호텔 대실
"""
from collections import defaultdict

def solution(book_time):
    least_time = 1e9
    last_time = -1e9
    change_book_time = defaultdict(list)
    for book in book_time:
        a, b = book
        a_hour, a_min = a.split(':')
        b_hour, b_min = b.split(':')
        least_time = min(least_time, int(a_hour) * 60 + int(a_min))
        last_time = max(last_time, int(b_hour) * 60 + int(b_min))
        change_book_time[int(a_hour) * 60 + int(a_min)].append(int(b_hour) * 60 + int(b_min) + 10)

    answer = 0
    room = []
    for t in range(least_time, last_time + 1):
        if t in change_book_time.keys():
            for value in change_book_time[t]:
                room.append(value)
        if t in room:
            count = room.count(t)
            for _ in range(count):
                room.remove(t)
        length = len(room)
        if length > answer:
            answer = length
    return answer


# print(solution([
#     ["15:00", "17:00"],
#     ["16:40", "18:20"],
#     ["14:20", "15:20"],
#     ["14:10", "19:20"],
#     ["18:20", "21:20"],
# ])) # 3
# print(solution([["09:10", "10:10"], ["10:20", "12:20"]])) # 1
# print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])) # 3
print(solution([["10:10", "12:10"], ["10:10", "12:10"], ["12:20", "12:30"], ["12:20", "12:30"]])) # 2
# print(solution([["01:00", "02:00"], ["02:10", "03:00"], ["03:10", "04:00"], ["04:00", "05:00"]]))
# print(solution([
#     ["00:00", "00:10"],
#     ["00:10", "00:15"],
#     ["00:10", "00:50"],
#     ["00:10", "00:59"],
#     ["00:30", "00:40"]
# ]))
# print(solution([["00:01","00:10"],["00:19","00:29"], ["00:20", "00:29"]]))
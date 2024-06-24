"""
주차 요금 계산

"""
from collections import defaultdict

def solution(fees, records):
    basic_hours, basic_fee, unit_hours, unit_fee = fees
    car_dict = defaultdict(list)
    for record in records:
        hour, minute = record[:5].split(":")
        if "IN" in record:
            number = record[-7: -3]
        if "OUT" in record:
            number = record[-8: -4]
        times = int(hour) * 60 + int(minute)
        car_dict[int(number)].append(times)

    for value in car_dict.values():
        if len(value) % 2 != 0:
            value.append(23 * 60 + 59)

    answer = {}
    for key, values in car_dict.items():
        sub_time = 0
        for i in range(0, len(values), 2):
            sub_time += values[i + 1] - values[i]
        if sub_time <= basic_hours:
            answer[key] = basic_fee
        else:
            if (sub_time - basic_hours) % unit_hours == 0:
                answer[key] = basic_fee + (sub_time - basic_hours) / unit_hours * unit_fee
            else:
                answer[key] = basic_fee + int((sub_time - basic_hours) / unit_hours + 1) * unit_fee

    result = []
    for key in sorted(answer):
        result.append(int(answer[key]))
    return result



print(solution(
    [180, 5000, 10, 600],
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],
)) # [14600, 34400, 5000]

print(solution(
    [120, 0, 60, 591],
    ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"],
)) # [0, 591]

print(solution(
    [1, 461, 1, 10],
    ["00:00 1234 IN"],
)) # [14841]

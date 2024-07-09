"""
광물 캐기

"""
def solution(picks, minerals):
    dia, iron, stone = picks
    dia_properties = {"diamond": 1, "iron": 1, "stone": 1}
    iron_properties = {"diamond": 5, "iron": 1, "stone": 1}
    stone_properties = {"diamond": 25, "iron": 5, "stone": 1}

    minerals = [minerals[l: l + 5] for l in range(0, len(minerals), 5)][:sum(picks)]
    minerals.sort(key=lambda x: (x.count('diamond'), x.count('iron'), x.count('stone')), reverse=True)

    answer = 0
    for mineral in minerals:
        if dia > 0:
            for name in mineral:
                answer += dia_properties[name]
            dia -= 1
        elif iron > 0:
            for name in mineral:
                answer += iron_properties[name]
            iron -= 1
        elif stone > 0:
            for name in mineral:
                answer += stone_properties[name]
            stone -= 1

    return answer

print(solution([1, 3, 2],
               ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
               )) # 12

print(solution([0, 1, 1],
               ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
               )) # 50



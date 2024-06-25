"""
오픈채팅방

"""
def solution(record):
    history = []
    nick_name_dict = {}
    for r in record:
        information = r.split(' ')
        if information[0] == "Enter":
            nick_name_dict[information[1]] = information[2]
        elif information[0] == "Change":
            nick_name_dict[information[1]] = information[2]
        history.append(information[:2])

    answer = []
    for h in history:
        if h[0] == "Change":
            continue
        nick_name = nick_name_dict[h[1]]
        if h[0] == "Enter":
            answer.append(f"{nick_name}님이 들어왔습니다.")
        if h[0] == "Leave":
            answer.append(f"{nick_name}님이 나갔습니다.")
    return answer







print(solution([
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
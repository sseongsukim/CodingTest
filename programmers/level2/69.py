"""
[3차] 방금그곡

"""
def solution(m, musicinfos):
    m = m.replace("C#", "H")
    m = m.replace("D#", "I")
    m = m.replace("F#", "J")
    m = m.replace("G#", "K")
    m = m.replace("A#", "L")
    answer = []


    for i, info in enumerate(musicinfos):
        start, end, title, code = info.split(",")
        code = code.replace("C#", "H")
        code = code.replace("D#", "I")
        code = code.replace("F#", "J")
        code = code.replace("G#", "K")
        code = code.replace("A#", "L")
        start_hour, start_min = start.split(":")
        end_hour, end_min = end.split(":")

        start_time = int(start_hour) * 60 + int(start_min)
        end_time = int(end_hour) * 60 + int(end_min)

        total_time = end_time - start_time
        song_time = len(code)
        if song_time == total_time:
            song_info = code
        elif song_time > total_time:
            song_info = code[:total_time]
        else:
            if total_time % song_time == 0:
                times = total_time // song_time
            else:
                times = total_time // song_time + 1
            song_info = code * times

        if m in song_info:
            answer.append((total_time, i, title))

    if len(answer) == 0:
        return "(None)"

    answer.sort(key= lambda x: (-x[0], x[1]))
    return answer[0][2]


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # "HELLO"
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])) # "FOO"
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # "WORLD"
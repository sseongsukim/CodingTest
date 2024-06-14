"""
영어 끝말잇기

"""
from collections import defaultdict
def solution(n, words):
    past_dict = defaultdict(list)
    past_alphabet = words[0][-1]
    past_dict[words[0][0]].append(words[0])
    for i in range(1, len(words)):
        first_alphabet = words[i][0]
        if words[i] in past_dict[first_alphabet]:
            return [i % n + 1, i // n + 1]
        if first_alphabet != past_alphabet:
            return [i % n + 1, i // n + 1]

        past_dict[first_alphabet].append(words[i])
        past_alphabet = words[i][-1]

    return [0, 0]

print(
    solution(
        3,
        ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    )
) # [3, 3]
print(
    solution(
        5,
        ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
    )
) # [0, 0]

print(
    solution(
        2,
        ["hello", "one", "even", "never", "now", "world", "draw"]
    )
) # [1, 3]

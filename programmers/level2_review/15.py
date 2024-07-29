"""
영어 끝말잇기
"""
from collections import defaultdict

def solution(n, words):
    answer = [0, 0]
    alphabet_dict = defaultdict(list)

    first_alphabet = words[0][0]
    alphabet_dict[first_alphabet].append(words[0])
    last_alphabet = words[0][-1]

    for i in range(1, len(words)):
        word = words[i]
        first_alphabet = word[0]
        if first_alphabet != last_alphabet or word in alphabet_dict[first_alphabet]:
            return [i % n + 1, i // n + 1]
        alphabet_dict[first_alphabet].append(word)
        last_alphabet = word[-1]
    return answer



print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])) # [3, 3]
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])) # [0, 0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])) # [1, 3]

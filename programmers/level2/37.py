"""
모음사전

"""



def solution(word):
    global answer, alphabet_list
    alphabet_list = ["A", "E", "I", "O", "U"]
    answer = 0

    def dfs(string):
        global answer, alphabet_list
        answer += 1
        print(string)
        if string == word:
            return True
        if len(string) == 5:
            return False
        for alpha in alphabet_list:
            if dfs(string + alpha):
                return True

    for alpha in alphabet_list:
        if dfs(alpha):
            return answer

print(solution("AAAAE")) # 6
print(solution("AAAE")) # 10
print(solution("I")) # 1563
print(solution("EIO")) # 1189
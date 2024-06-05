"""
K1KA5CB7
-> ABCKK13
AJKDLSI412K4JSJ9D
-> ADDIJJJKKLSS20
"""
N = input()
alphabets = []
numbers = []
for n in N:
    if n.isdigit():
        numbers.append(int(n))
    else:
        alphabets.append(n)

alphabets.sort()
answer = ''
for alphabet in alphabets:
    answer += alphabet
answer += str(sum(numbers))
print(answer)
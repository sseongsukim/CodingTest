import copy

def turn_left(key):
    length = len(key)
    new_key = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            new_key[j][length - i - 1] = key[i][j]
    return new_key

def check(new_lock):
    length = len(new_lock) // 3
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    length = len(lock)
    key_length = len(key)
    new_lock = [[1] * (length * 3) for _ in range(length * 3)]
    for i in range(length):
        for j in range(length):
            new_lock[i + length][j + length] = lock[i][j]

    answer = False
    for _ in range(4):
        key = turn_left(key)
        for i in range(1, length * 2 + 1):
            for j in range(1, length * 2 + 1):
                copy_lock = copy.deepcopy(new_lock)
                for x in range(key_length):
                    for y in range(key_length):
                        copy_lock[i + x][j + y] += key[x][y]

                if check(copy_lock):
                    return True

    return answer

print(solution(
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]],
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
))
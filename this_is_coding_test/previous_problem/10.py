import copy

def turn(key):
    length = len(key)
    new_key = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            new_key[j][length - i - 1] = key[i][j]

    return new_key

def check(new_lock):
    length = len(new_lock)
    index = length // 3
    for i in range(index, index * 2):
        for j in range(index, index * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    length = len(lock)
    new_lock = [[1] * (length * 3) for _ in range(length * 3)]
    for i in range(length):
        for j in range(length):
            new_lock[i + length][j + length] = lock[i][j]

    for _ in range(4):
        key = turn(key)

        for x in range(length * 2):
            for y in range(length * 2):
                newlock = copy.deepcopy(new_lock)
                for i in range(length):
                    for j in range(length):
                        newlock[x + i][y + j] += key[i][j]

                if check(newlock):
                    return True

    return False

print(solution(key= [[0, 0, 0], [1, 0, 0], [0, 1, 1]], lock= [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

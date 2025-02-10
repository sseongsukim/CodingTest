
def check_answer(lock):
    length = len(lock)
    N = length // 3

    for x in range(N, 2 * N):
        for y in range(N, 2 * N):
            if lock[x][y] == 0:
                return False
    return True

def turn_right(key):
    M = len(key)
    new_key = [[0] * M for _ in range(M)]
    for x in range(M):
        for y in range(M):
            new_key[y][M - x - 1] = key[x][y]
    return new_key

def solution(key, lock):
    M = len(key)
    N = len(lock)

    new_lock = [[0] * (3 * N) for _ in range(3 * N)]
    for x in range(N):
        for y in range(N):
            new_lock[x + N][y + N] = lock[x][y]

    for _ in range(4):
        key = turn_right(key)
        for i in range(1, 2 * M):
            for j in range(1, 2 * M):

                for x in range(N):
                    for y in range(N):
                        new_lock[i + x][j + y] += key[x][y]

                if check_answer(new_lock):
                    return True

                for x in range(N):
                    for y in range(N):
                        new_lock[i + x][j + y] -= key[x][y]

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
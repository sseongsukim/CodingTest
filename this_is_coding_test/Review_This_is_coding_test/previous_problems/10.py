
def turn(key):
    N = len(key)
    new_key = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            new_key[y][N - x - 1] = key[x][y]
    return new_key

def check_answer(lock):
    M = len(lock) // 3
    for x in range(M, M * 2):
        for y in range(M, M * 2):
            if lock[x][y] != 1:
                return False
    return True

def solution(key, lock):
    N = len(key)
    M = len(lock)

    new_lock = [[0] * (M * 3) for _ in range(M * 3)]
    for i in range(M):
        for j in range(M):
            new_lock[i + M][j + M] = lock[i][j]

    for _ in range(4):
        key = turn(key)
        for lx in range(1, M * 2):
            for ly in range(1, M * 2):

                for kx in range(N):
                    for ky in range(N):
                        new_lock[lx + kx][ly + ky] += key[kx][ky]
                if check_answer(new_lock):
                    return True
                for kx in range(N):
                    for ky in range(N):
                        new_lock[lx + kx][ly + ky] -= key[kx][ky]

    return False

print(solution(key= [[0, 0, 0], [1, 0, 0], [0, 1, 1]], lock= [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
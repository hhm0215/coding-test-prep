# 캐릭터가 있는 장소 1 X 1 크기의 정사각형으로 이뤄진 N X M 크기의 직사각형으로 각각의 칸은 육지 또는 바다
# 캐릭터는 동서남북 중 한 곳을 바라본다
# 맵의 각 칸은 (A, B)로 나타낼 수 있고, A는 북쪽에서 떨어진 칸의 개수, B는 서쪽에서 떨어진 칸의 개수
# 캐릭터는 상하좌우로 이동할 수 있고, 바다로 되어 있는 칸은 갈 수 없다
# 입력 조건 (3<=N, M<=50) (0<=A<=N-1) (0<=B<=M-1) (d: 0, 1, 2, 3    - 북, 동, 남, 서)
# 캐릭터가 이동할 수 있는 칸의 개수 구하기
n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
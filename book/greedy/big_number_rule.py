# 큰 수의 법칙 - 그리디
# N개의 수 중 가장 큰 수를 K번 연속으로, 그 다음 두 번째 큰 수를 1번 반복하며 M번 더하기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

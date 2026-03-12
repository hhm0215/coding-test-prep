# 숫자 카드 게임 문제 
# nxm 행렬에서 각 행의 최솟값 중 최댓값을 찾는 그리디 문제
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)
    

    

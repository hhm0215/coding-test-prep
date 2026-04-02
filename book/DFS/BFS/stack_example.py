# stack 예시 
# 선입후출 or 후입선출
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1]) # 스택에 들어있는 원소를 거꾸로 출력
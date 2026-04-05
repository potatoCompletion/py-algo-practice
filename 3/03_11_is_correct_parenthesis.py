# 올바른 괄호인지 판단 (단골문제)
# 1. queue를 이용해서 왼쪽부터 popleft
# 2. 열린 괄호면 count + 1, 닫힌 괄호면 -1
# 3. 만약 count가 -1이 되면 return False
# 4. 다 끝났을 때 count가 0이면 True, 아니면 False

from collections import deque

def is_correct_parenthesis(string):
    queue = deque(string)
    count = 0

    while queue:
        target = queue.popleft()
        if target == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    return count == 0


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
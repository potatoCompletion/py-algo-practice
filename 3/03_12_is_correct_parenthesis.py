# 올바른 괄호 확인 문제를 스택으로 다시 풀어보자 (스택이 제일 나은듯)

def is_correct_parenthesis(string):
    stack = []

    for c in string:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                stack.pop()

    if stack:
        return False
    else:
        return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
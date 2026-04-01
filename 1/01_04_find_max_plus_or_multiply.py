# 1. 0 혹은 양의 정수로만 이루어짐
# 2. 현재 결과값, 비교 대상 숫자가 0, 1이면 무조건 더하기, 그게 아니면 무조건 곱하기

def find_max_plus_or_multiply(array):
    plus_or_multiply_sum = array[0]

    for i in range(1, len(array)):
        if plus_or_multiply_sum <= 1 or array[i] <= 1:
            plus_or_multiply_sum += array[i]
        else:
            plus_or_multiply_sum *= array[i]

    return plus_or_multiply_sum

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))
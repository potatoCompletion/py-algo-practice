# 1. 정수 입력했을 때 그 정수 이하의 소수를 모두 반환
# 2. 소수 == 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수
# 3. 2부터 해당 숫자를 2로 나눈 값까지 하나씩 올라가면서 나머지 연산으로 0으로 떨어지는 수가 없는지 확인

# 1차 개선: 2부터 n - 1까지 모든 소수로 나누어 떨어지지 않는지 확인
# 2차 개선: 소수이려면 해당 숫자의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않음.

input = 20


def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in prime_list:
            if i * i <= n and n % i == 0:
                break
        else:       # for - else 는 for문이 break로 인해 종료되지 않았을 때 호출되는 조건이다.
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
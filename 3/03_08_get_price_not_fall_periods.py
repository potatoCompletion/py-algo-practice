# 주식 가격이 안떨어진 기간(초) 찾기
# queue 를 사용해서 풀어보자
# 1. popleft로 왼쪽에서 부터 빼면서 자기보다 작은 숫자 만날 때까지 순회
# 2. 하나 지나갈 때마다 초 기록
# 3. 끝날 때 result에다가 append
from collections import deque

prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    queue = deque(prices)
    result = []

    while queue:
        target = queue.popleft()
        period = 0
        for price in queue:
            period += 1
            if price < target:
                break

        result.append(period)

    return result


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))
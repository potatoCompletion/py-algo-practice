# 상품가격, 할인쿠폰 받아서 최대할인 적용받기
# 가장 높은 가격의 상품에 가장 높은 할인율을 배당해야 한다.
# 1. 상품가격을 내림차순으로 정렬
# 2. 할인 쿠폰을 내림차순으로 정렬
# 3. 둘 다 왼쪽부터 비교하고(popleft) 가격 계산

from collections import deque

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    prices = deque(prices)
    coupons = deque(coupons)
    result = 0

    while prices and coupons:
        price = prices.popleft()
        coupon = coupons.popleft()
        result += price - (price * (coupon / 100))

    while prices:
        result += prices.popleft()

    return result


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))
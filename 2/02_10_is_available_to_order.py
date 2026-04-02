# 정렬을 이용해 풀어보자 (set 이용도 고려해보자)
# 1. shop_menus sort 한다.
# 2. shop_orders 를 하나씩 꺼내서 shop_menus 이진탐색 (굳이?)

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()

    for order in orders:
        first_index = 0;
        second_index = len(shop_menus) - 1

        while first_index <= second_index:
            target_index = (first_index + second_index) // 2
            if menus[target_index] == order:
                break

            if order > menus[target_index]:
                first_index = target_index + 1
            else:
                second_index = target_index - 1

        else:
            return False



    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
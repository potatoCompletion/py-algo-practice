# 링크드리스트에서 끝에서 n번째 값 추출
# 링크드리스트 자료구조를 안건든다는 전제하에 풀어보자
# 1. 링크드리스트를 순회하면서 각각 순서별로 값을 list에 기록
# 2. 끝까지 순회한 후 len(list) - k 으로 조회

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        cur_node = self.head
        temp_list = []

        while cur_node is not None:
            temp_list.append(cur_node)
            cur_node = cur_node.next

        result_index = len(temp_list) - k

        return temp_list[result_index]



linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
# 1. 두 개의 링크드리스트를 받아서 들어있는 숫자 문자열을 엮어서 숫자로 만든다
# 2. 두 값을 더한 값을 반환


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


def get_linked_list_sum(linked_list_1, linked_list_2):
    linked_list_str_1 = ""
    linked_list_str_2 = ""

    cur_node = linked_list_1.head
    while (cur_node != None):
        linked_list_str_1 += str(cur_node.data)
        cur_node = cur_node.next

    cur_node = linked_list_2.head
    while (cur_node != None):
        linked_list_str_2 += str(cur_node.data)
        cur_node = cur_node.next

    return int(linked_list_str_1) + int(linked_list_str_2)


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
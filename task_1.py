class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


def merge_sort_linked_list(llist):
    if llist.head is None or llist.head.next is None:
        return llist

    middle = get_middle(llist.head)
    next_to_middle = middle.next

    middle.next = None

    left = LinkedList()
    left.head = llist.head
    right = LinkedList()
    right.head = next_to_middle

    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)

    sorted_list = LinkedList()
    sorted_list.head = sorted_merge(left.head, right.head)
    return sorted_list


def get_middle(head):
    if head is None:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def sorted_merge(left, right):
    if left is None:
        return right
    if right is None:
        return left

    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, left.next)

    return result


def merge_two_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)

# Виводимо обернений список
print('\nОбернений звʼязний список')
llist.reverse()
llist.print_list()
llist.reverse()

# Сортування списку
print("\nСортування зв'язного списку:")
sorted_llist = merge_sort_linked_list(llist)
print("Після сортування:")
sorted_llist.print_list()

# Об'єднання двох відсортованих списків
print("\nОб'єднання двох відсортованих списків:")
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)
list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)
merged_list = merge_two_sorted_lists(list1.head, list2.head)
merged_list.print_list()
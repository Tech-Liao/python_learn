class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.pre = next
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None

    def insert_head_list(self, date: int):
        """头插法"""
        node = ListNode(date)
        if self.head is None:
            self.head = node
            return True
        self.head.pre = node
        node.next = self.head
        self.head = node
        return True

    def insert_rear_list(self, date: int):
        node = ListNode(date)
        if self.head is None:
            self.head = node
            return True
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        else:
            cur.next = node
            node.pre = cur
            return True

    def insert_index_list(self, index, date):
        lenth = self.length_list()
        cur = self.head
        node = ListNode(date)
        if index <= 0:
            print("index is error")
            return False
        if index == lenth:
            while cur.next is not None:
                cur = cur.next
            else:
                cur.pre.next = node
                node.pre = cur.pre
                node.next = cur
                cur.pre = node
                return True
        if index == 1:
            cur.pre = node
            node.next = cur
            self.head = node
            return True
        if index > lenth:
            while cur.next is not None:
                cur = cur.next
            else:
                cur.next=node
                node.pre = cur
                return True
        while index - 1 > 0:
            cur = cur.next
            index -= 1
        else:
            node.next = cur
            node.pre = cur.pre
            cur.pre.next = node
            cur.pre = node
            return True

    def length_list(self):
        cur = self.head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def print_list(self):
        if self.head is None:
            print("List is None")
            return False
        cur = self.head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()
        return True

    def delete_index_list(self, index):
        lenth = self.length_list()
        if index <= 0 or index > lenth:
            print("index is error")
            return False
        cur = self.head
        if index == 1:
            cur.next.pre = None
            self.head = cur.next
            return cur
        if index == lenth:
            while index - 1 > 0:
                cur = cur.next
                index -= 1
            cur.pre.next = None
            return cur
        while index - 1 > 0:
            cur = cur.next
            index -= 1
        else:
            cur.pre.next = cur.next
            cur.next.pre = cur.pre
            return cur

    def modify_list(self, index, new):
        if index <= 0 or index > self.length_list():
            print("index is error")
            return False

        cur = self.head
        while index - 1 > 0:
            cur = cur.next
            index -= 1
        else:
            cur.val = new
            return True


list1 = LinkList()
x = [1, 2, 3, 4, 5, 6]
for i in x:
    list1.insert_rear_list(i)

list1.print_list()
list1.insert_index_list(0,10)
list1.print_list()
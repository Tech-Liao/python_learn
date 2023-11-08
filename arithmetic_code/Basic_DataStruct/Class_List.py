class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:

    def __init__(self):
        self.head = None

    def insert_head_list(self, date):
        """"""
        node = ListNode(date)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_rail_list(self, date):
        """尾插法"""
        node = ListNode(date)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def print_list(self):
        if self.head is None:
            print("List is None")
            return False
        cur = self.head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()

    def delete_list(self, val):
        if self.head is None:
            print("List is None,can not delete")
            return False
        if self.head.val == val:
            node = self.head
            self.head = self.head.next
            return node
        cur = self.head
        pre = cur
        while cur is not None:
            if cur.val != val:
                pre = cur
                cur = cur.next
            else:
                pre.next = cur.next
                return cur
        else:
            print("val is not in list")

    def modify_list(self, old, new):
        if self.head is None:
            print("List is None,can not delete")
            return False
        cur = self.head
        while cur is not None:
            if cur.val != old:
                cur = cur.next
            else:
                cur.val = new
                return True
        else:
            print("val is not in list")
            return False


List1 = LinkList()
List1.print_list()
x = [1, 2, 3, 4, 5, 6]
for i in x:
    List1.insert_head_list(i)
List1.print_list()
List2 = LinkList()
for i in x:
    List2.insert_rail_list(i)

List2.modify_list(3, 7)
List2.print_list()

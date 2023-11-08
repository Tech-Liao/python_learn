class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Binary_Tree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def pre_print(self, root):
        if not root:
            return
        print(root.val, end=' ')
        self.pre_print(root.left)
        self.pre_print(root.right)

    def in_print(self, root):
        if not root:
            return
        self.in_print(root.left)
        print(root.val, end=' ')
        self.in_print(root.right)

    def tail_print(self, root):
        if not root:
            return
        self.tail_print(root.left)
        self.tail_print(root.right)
        print(root.val, end=' ')

    def insert(self, val):
        node = TreeNode(val)
        if self.is_empty():
            self.root = node
            return True
        root = self.root
        root_pre = root
        while root:
            if root.val > val:
                root_pre = root
                root = root.left
            elif root.val < val:
                root_pre = root
                root = root.right
            else:
                print("val is already in tree")
                return
        if root_pre.val > val:
            root_pre.left = node
        else:
            root_pre.right = node

    def delete(self, val):
        if self.is_empty():
            print("tree is empty")
            return False
        pre = self.root
        cur = pre
        while cur:
            if cur.val > val:
                pre = cur
                cur = cur.left
            elif cur.val < val:
                pre = cur
                cur = cur.right
            else:
                break
        else:
            print("val is not in empty")
            return False
        if not cur.left or not cur.right:
            tmp = cur.left or cur.right
            if pre.left == cur:
                pre.left = tmp
            else:
                pre.right = tmp

        else:
            tmp = cur.right
            pre_tmp = tmp
            while tmp.left:
                pre_tmp = tmp
                tmp = tmp.left
            cur.val = tmp.val
            pre_tmp.left = tmp.right
        return True


tree = Binary_Tree()
x = [14, 7, 3, 9, 18, 16, 19]
for i in x:
    tree.insert(i)

tree.in_print(tree.root)
print()
tree.pre_print(tree.root)
print()

tree.delete(14)
tree.in_print(tree.root)
print()
tree.pre_print(tree.root)
print()
tree.delete(18)
tree.in_print(tree.root)
print()
tree.pre_print(tree.root)
print()
tree.delete(9)
tree.in_print(tree.root)
print()
tree.pre_print(tree.root)
print()
tree.delete(1)
tree.in_print(tree.root)
print()
tree.pre_print(tree.root)
print()

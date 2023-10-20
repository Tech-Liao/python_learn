"""二叉树的链式存储"""

import random
### 头节点类
class HeadNode:
    def __init__(self):
        self.val=0
        self.next=None

# 二叉树节点类
class TreeNode:
    def __init__(self,val):
        self.right=None
        self.left=None
        self.val=val


# 二叉树
class Binary_tree:
    def __init__(self):
        """定义执行根节点的头节点"""
        Head=HeadNode()
        self.head=Head

    def Is_Empty(self):
        if self.head.next is None:
            return True
        else:
            return False
        
    def pre_print(self,root):
        if root is None:
            return
        print(root.val,end=' ')
        self.pre_print(root.left)
        self.pre_print(root.right)

    def insert(self,val):
        node=TreeNode(val)
        if self.Is_Empty():
            self.head.next=node
            return True
        pre=self.head
        cur=pre.next
        while cur:
            if cur.val>=val:
                pre=cur
                cur=cur.left
            elif cur.val<val:
                pre=cur
                cur=cur.right

        if pre.val>=val:
            pre.left=node
        else:
            pre.right=node
        return True
    
    def delete(self,val):
        if self.Is_Empty():
            print("tree is empty")
            return False
        pre=self.head
        cur=pre.next
        while cur:
            if cur.val==val:
                break
            elif cur.val>=val:
                pre=cur
                cur=cur.left
            else:
                pre=cur
                cur=cur.right
        else:
            print("val not in tree")
            return False
        if cur.left is None or cur.right is None:
            """只有一个或0个子树"""
            temp=cur.left or cur.right
            if cur !=self.head.next:
                if pre.left==cur:
                    pre.left=temp
                else:
                    pre.right=temp
            else:
                self.head.next=temp
        else:
            temp=cur.right
            temp_pre=temp
            while temp.left is not None:
                temp_pre=temp
                temp=temp.left
            cur.val=temp.val
            if temp.right!=None:
                temp_pre.left=temp.right
                
            else:
                temp_pre.left=None


                

Tree=Binary_tree()
x=[1,4,0,8,7,2,3,6,5,9]
print(x)
for i in x:
    Tree.insert(i)
Tree.pre_print(Tree.head.next)
print()
Tree.delete(1)
Tree.pre_print(Tree.head.next)
print()
Tree.delete(8)
Tree.pre_print(Tree.head.next)
print()
Tree.delete(0)
Tree.pre_print(Tree.head.next)
print()

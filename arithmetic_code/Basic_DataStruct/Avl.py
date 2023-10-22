class TreeNode:
    def __init__(self,val):
        self.val=val
        self.height=0
        self.left=None
        self.right=None

class Avl_Tree:
    def __init__(self):
        self.root=None

    def height(self,node):
        if node is None:
            return -1
        return node.height

    def update_height(self,node):
        node.height=max(self.height(node.left),self.height(node.right))+1

    def balance_factor(self,node):
        if node is None:
            return 0
        return self.height(node.left)-self.height(node.right)

    def right_rotate(self,node):
        """
        右旋的情况：左子树深度增加，即平衡因子>1，
        且失衡节点的左节点的平衡因子>=0,说明插入的节点在左节点的左子树中。
        """
        child=node.left
        grandchild=child.right
        child.right=node
        node.left=grandchild
        self.update_height(node)
        self.update_height(child)
        return child

    def left_rotate(self,node):
        """
        左旋的情况和右旋是对称的，即平衡因子<-1，且失衡节点的右节点的平衡因子<=0
        """
        child=node.right
        grandchild=child.left
        child.left=node
        node.right=grandchild
        self.update_height(node)
        self.update_height(child)
        return child
    

    def rotate(self,node):
        balance_factor=self.balance_factor(node)
        if balance_factor>1:
            if self.balance_factor(node.left)>=0:
                "只是右旋"
                return self.right_rotate(node)
            else:
                "因为失衡节点左节点的平衡因子<0,所以先将左节点进行左旋再对失衡节点进行右旋"
                node.left=self.left_rotate(node.left)
                return self.right_rotate(node)
        elif balance_factor<-1:
            if self.balance_factor(node.right)<=0:
                return self.left_rotate(node)
            else:
                node.right=self.right_rotate(node.right)
                return self.left_rotate(node)

        return node
            
    def insert(self,val):
        self.root=self.insert_helper(self.root,val)

    def insert_helper(self,node,val):
        if node is None:
            return TreeNode(val)
        if val<node.val:
            "插入到节点左子树中"
            node.left=self.insert_helper(node.left,val)
        elif val>node.val:
            node.right=self.insert_helper(node.right,val)
        else:
            "重复节点不用插入"
            return node
        "每次插入完，需要更新深度，并且检查是否失衡"
        self.update_height(node)
        return self.rotate(node)

    def remove(self,val):
        self.root=self.remove_helper(self.root,val)

    def remove_helper(self,node,val):
        if not node:
            return None
        if val<node.val:
            node.left=self.remove_helper(node.left,val)
        elif val>node.val:
            node.right=self.remove_helper(node.right,val)
        else:
            if not node.left or not node.right:
                "删除节点只有一个子树或者0个子树"
                child=node.left or node.right
                if child is None:
                    return None
                else:
                    node=child
            else:
                "删除节点左右子树都在，需要拿删除字数的右子树中最左边的元素代替删除节点的元素"
                temp=node.right
                while temp.left:
                    temp=temp.left
                node.right=self.remove_helper(node.right,temp.val)
                node.val=temp.val
        self.update_height(node)
        return self.rotate(node)

    def pre_print(self,node):
       if not node:
           return
       print(node.val,end=' ')
       self.pre_print(node.left)
       self.pre_print(node.right)

    def in_print(self,node):
        if not node:
            return 
        self.in_print(node.left)
        print(node.val,end=' ')
        self.in_print(node.right)


tree=Avl_Tree()
x=[1,2,3,4,5,6,7,8,9]

for i in x:
    tree.insert(i)
tree.pre_print(tree.root)
print()
tree.in_print(tree.root)
print()

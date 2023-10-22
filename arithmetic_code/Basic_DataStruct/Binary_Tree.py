"""二叉树的链式存储"""
class TreeNode:
    """二叉树节点的定义"""
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Binary_Tree:
    """二叉树定义"""
    def __init__(self):
        self.root=None


    def insert(self,root,val):
        """
        root是二叉树的根，val是需要插入的值
        返回值是二叉树节点TreeNode
        """
        if root is None:
            return TreeNode(val)
        """
        小于节点则插入左子树，大于则插入右子树
        使用递归方式插入
        """
        if root.val>val:
            root.left=self.insert(root.left,val)
        if root.val<val:
            root.right=self.insert(root.right,val)
        return root

    def delete(self,root,val):
        if not root:
            print("val not in tree,or tree is empty")
            return root
        "大于root则在右子树，小于在左子树"
        if root.val>val:
            root.left=self.delete(root.left,val)
            return root
        if root.val<val:
            root.right=self.delete(root.right,val)
            return root
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                curr=root.right
                pre=curr
                while curr.left:
                    pre=curr
                    curr=curr.left
                root.val=curr.val
                pre.left=None
                return root

    def preorderTraversal(self,root):
        if not root:
            return 
        print(root.val,end=' ')
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

    def inorderTraversal(self,root):
        if not root:
            return 
        self.inorderTraversal(root.left)
        print(root.val,end=' ')
        self.inorderTraversal(root.right)


    def postorderTraversal(self,root):
        if not root:
            return 
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        print(root.val,end=' ')



x=[14,7,18,3,9,16,19]
Tree=Binary_Tree()
for i in x:
    Tree.root=Tree.insert(Tree.root,i)
Tree.inorderTraversal(Tree.root)
print()
Tree.root=Tree.delete(Tree.root,14)
Tree.preorderTraversal(Tree.root)
print()
Tree.inorderTraversal(Tree.root)
print()
Tree.root=Tree.delete(Tree.root,18)
Tree.preorderTraversal(Tree.root)
print()
Tree.inorderTraversal(Tree.root)
print()
Tree.root=Tree.delete(Tree.root,3)
Tree.preorderTraversal(Tree.root)
print()
Tree.inorderTraversal(Tree.root)
print()
Tree.root=Tree.delete(Tree.root,1)
Tree.root=Tree.delete(None,1)

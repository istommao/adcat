"""bintree."""


class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return '<TreeNode {}>'.format(str(self.val))


class StackTraversal(object):

    def preorder(self, root):
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                print(root.val)
                root = root.left

            if stack:
                root = stack.pop()
                root = root.right

    def inorder(self, root):
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            if stack:
                root = stack.pop()
                print(root.val)
                root = root.right

    def postorder(self, root):
        if not root:
            return
        stack1 = []
        stack2 = []
        node = root
        stack1.append(node)

        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().val)


class RecursiveTraversal(object):

    def __init__(self):
        self.traverse_path = []

    def preorder(self, root):
        if root:
            print(root.val)
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)
            self.traverse_path.append(root.val)

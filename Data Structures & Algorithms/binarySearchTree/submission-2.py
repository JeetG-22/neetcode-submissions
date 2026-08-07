class TreeMap:
    
    def __init__(self):
        self.root = None
        
    def insert(self, key: int, val: int) -> None:
        if not self.root: #if tree is empty
            self.root = TreeNode(key, val)
            return

        def insertNode(root):
            if not root:
                return TreeNode(key,val)
            if root.key < key:
                root.right = insertNode(root.right)
            elif root.key > key:
                root.left = insertNode(root.left)
            else:
                root.key, root.val = key,val
            return root
        self.root = insertNode(self.root)

    def get(self, key: int) -> int:
        def findVal(root):
            if not root:
                return -1
            if key > root.key:
                return findVal(root.right)
            elif key < root.key:
                return findVal(root.left)
            return root.val
        return findVal(self.root) 



    def getMin(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val
        


    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val


    def remove(self, key: int) -> None:

        def removeKey(root, key):
            if not root:
                return root
            if key > root.key:
                root.right = removeKey(root.right, key)
            elif key < root.key:
                root.left = removeKey(root.left, key)
            else:
                if root.left and root.right:
                    curr = root.right
                    while curr and curr.left:
                        curr = curr.left
                    root.key, root.val = curr.key, curr.val
                    root.right = removeKey(root.right, root.key)
                elif not root.left and not root.right:
                    return None
                elif root.left:
                    return root.left
                else:
                    return root.right
            return root
        self.root = removeKey(self.root, key)
        

    def getInorderKeys(self) -> List[int]:
        output = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            output.append(root.key)
            inorder(root.right)
        inorder(self.root)
        return output

class TreeNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


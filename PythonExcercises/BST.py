class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def get_children(self):
        values=[]
        if self.left != None:
            values.append(self.left)
        elif self.right!=None:
            values.append(self.right)
        return values

class BST:
    def __init__(self):
        self.root = None

    def set_root(self, val):
        if self.root:
            self.root.set(val)
        else:
            self.root = Node(val)

    def insert(self, val):
        if val > self.root.val:
            if self.root.right:
                self.ins_hel(self.root.right, val)
            else:
                self.root.right=Node(val)
        elif val <= self.root.val:
            if self.root.left:
                self.ins_hel(self.root.left, val)
            else:
                self.root.left=Node(val)

    def ins_hel(self, current_node, val):
        if val > current_node.val:
            if current_node.right:
                self.ins_hel(current_node.right, val)
            else:
                current_node.right = Node(val)
        elif val <= current_node.val:
            if current_node.left:
                self.ins_hel(current_node.left, val)
            else:
                current_node.left=Node(val)

    def find(self, val):
        if self.root:
            if self.root.val == val:
                return True, 'root'
            elif self.root.val < val:
                if self.root.right:
                    return self.find_helper(self.root.right, val)
                else:
                    return False
            elif self.root.val > val:
                if self.root.left:
                    return self.find_helper(self.root.left, val)
                else:
                    return False
        else:
            return False

    def find_helper(self, current_node, val):
        if val == current_node.val:
            return True
        elif val > current_node.val:
            if current_node.right:
                self.find_heler(current_node.right, val)
            else:
                return False
        elif val < current_node.val:
            if current_node.left:
                self.find_helper(current_node.left, val)
            else:
                return False

drzewo = BST()
drzewo.set_root(5)
drzewo.insert(7)
drzewo.insert(6)

print(drzewo.find(7))
print(drzewo.find_helper(drzewo.root.right, 7))


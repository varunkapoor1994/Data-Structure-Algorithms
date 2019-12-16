import pdb


class Node:
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None
        self.parent = None

    def find_successor(self):
        if self.right:
            return self.right.__find_min()
        if self.right is None and self.parent.left.key == self.key:
            return self.parent
        if self.right is None and self.parent.right.key == self.key:
            self.parent.right = None
            succ = find_successor(self.parent)
            self.parent.right = self
            return succ

    def __find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def splice_out(self):
        if not (self.right or self.left):
            if self.parent.left.key == self.key:
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.left and not self.right:
            if self.parent.left.key == self.key:
                self.parent.left = self.left
                self.left = None
            else:
                self.parent.right = self.left
                self.left = None
        elif self.right and not self.left:
            if self.parent.left.key == self.key:
                self.parent.left = self.right
                self.right = None
            else:
                self.parent.right = self.right
                self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert_Node(self, item):
        if not isinstance(item, Node):
            item = Node(item)
        if not self.root:
            self.root = item
        else:
            self.put(self.root, item)
        self.size = self.size+1

    def put(self, current_node, item):
        if item.key <= current_node.key:
            if current_node.left:
                self.put(current_node.left, item)
            else:
                current_node.left = item
                item.parent = current_node
        elif item.key > current_node.key:
            if current_node.right:
                self.put(current_node.right, item)
            else:
                current_node.right = item
                item.parent = current_node

    def get(self, value):
        if not self.root:
            return None
        res = self.__get_node(self.root, value)
        if res:
            return True
        return False

    def __get_node(self, current_node, value):
        if not current_node:
            return None
        if current_node.key == value:
            return current_node
        elif value < current_node.key:
            return self.__get_node(current_node.left, value)
        else:
            return self.__get_node(current_node.right, value)

    def delete_node(self, item):
        node = self.__get_node(self.root, item)
        if node is None:
            raise KeyError('Node not found')
        elif not node.left and not node.right:
            if node.parent.left.key == item:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left and not node.right:
            if node.parent.left.key == item:
                node.parent.left = node.left
                node.left = None
            else:
                node.parent.right = node.left
                node.left = None
        elif node.right and not node.left:
            if node.parent.left.key == item:
                node.parent.left = node.right
                node.right = None
            else:
                node.parent.right = node.right
                node.right = None
        elif node.right and node.left:
            succ = node.find_successor()
            succ.splice_out()
            node.key = succ.key
        return "{} deleted from Tree".format(item)

    def preorder(self, root, preorder_list):
        if root:
            preorder_list.append(root.key)
        if root.left:
            self.preorder(root.left, preorder_list)
        if root.right:
            self.preorder(root.right, preorder_list)
        if len(preorder_list) == self.size:
            return preorder_list

    def inorder(self, root, inorder_list):
        if root.left:
            self.inorder(root.left, inorder_list)
        inorder_list.append(root.key)
        if root.right:
            self.inorder(root.right, inorder_list)
        if len(inorder_list) == self.size:
            return inorder_list

    def postorder(self, root, postorder_list):
        if root.left:
            self.postorder(root.left, postorder_list)
        if root.right:
            self.postorder(root.right, postorder_list)
        postorder_list.append(root.key)
        if len(postorder_list) == self.size:
            return postorder_list

    def breath_first_search(self):
        current_node = self.root
        bfs = []
        queue = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            bfs.append(current_node.key)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return bfs

    def bfs_recursive(self, queue, node_list):
        if not len(queue):
            return node_list
        current_node = queue.pop(0)
        node_list.append(current_node.key)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.bfs_recursive(queue, node_list)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert_Node(25)
    tree.insert_Node(15)
    tree.insert_Node(10)
    tree.insert_Node(22)
    tree.insert_Node(4)
    tree.insert_Node(12)
    tree.insert_Node(18)
    tree.insert_Node(24)
    tree.insert_Node(50)
    tree.insert_Node(35)
    tree.insert_Node(70)
    tree.insert_Node(31)
    tree.insert_Node(44)
    tree.insert_Node(66)
    tree.insert_Node(90)

    print(tree.preorder(tree.root, []))
    print("Size of BST : ", tree.size)
    # print("Inorder")
    print(tree.inorder(tree.root, []))
    print(tree.postorder(tree.root, []))
    # print(tree.breath_first_search())
    # print(tree.bfs_recursive([tree.root], []))
    # print(tree.delete_node(16))
    # print(dir(tree))

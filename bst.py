class BinaryNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    """ A Binary Tree class """

    def __init__(self):
        self.root = None

    def insert(self, data):
        print("-> ", data)
        self.root = self.__insert(self.root, data)

    def __insert(self, node, data):
        if node is None:
            print("node is None")
            node = BinaryNode(data)  # No node exists so we create a new node
        elif data < node.data:
            print("data < node.data | ", data, "<", node.data)
            node.left = self.__insert(node.left, data)  # data is smaller than the current node so go to the left
        elif data > node.data:
            print("data > node.data | ", data, ">", node.data)
            node.right = self.__insert(node.right, data)
        return node

    def print_tree(self):
        self.__print_tree(self.root, 1)

    def __print_tree(self, node, depth):
        if node is None:
            return
        self.__print_tree(node.left, depth + 1)

        if self.root == node:
            print("*", node.data)
        else:
            print("  " * depth, node.data)

        self.__print_tree(node.right, depth + 1)

    def max_depth(self):
        return self.__max_depth(self.root)

    def __max_depth(self, node):
        if node is None:
            return 0
        return max(self.__max_depth(node.left), self.__max_depth(node.right)) + 1

    def exists(self, data):
        return self.__exists(self.root, data)

    def __exists(self, node, data):
        if node is None:
            return False
        print(node.data)
        if data < node.data:
            return self.__exists(node.left, data)
        elif data > node.data:
            return self.__exists(node.right, data)
        else:
            return True

    def leaf_count(self):
        return self.__leaf_count(self.root)

    def __leaf_count(self, node):
        if node is None:
            return 0
        if node.right is None and node.left is None:
            return 1
        else:
            return self.__leaf_count(node.left) + self.__leaf_count(node.right)

    def node_count(self, depth):
        return self.__node_count(self.root, depth)

    def __node_count(self, node, depth):
        if node is None:
            return 0
        if depth == 0:
            return 1  # trivial case with the root being the only node

        return self.__node_count(node.left, depth - 1) + self.__node_count(node.right, depth - 1)

    def right_side_view(self):
        """
        思路很简单：从root节点开始，一层一层往下走。
        因为root知道自己的left, right，所以下一层的左右关系知道了。
        然后第二层的下一层就是本层的：left -> left，left -> right，right -> left，right -> right

        因此推广以后，逻辑就是：

        其实：从root开始。

        接下来：
        - 从左到右遍历本层的每一个node，push它们每一个的left，most，就得到了下一层的nodes（并且是从左到右）
        - 进入下一层
        - 重复上面两步

        :return:
        """
        # 首先打印出root node
        # root node在它自己这一层肯定是rightmost的。
        print("*", self.root.data)

        # 我们要用到两个数组交替使用，
        # 一个是正在遍历的本层nodes，
        # 另一个是根据本层nodes生成的下一层nodes列表。
        foos = [self.root]  # foos的初始值是list
        bars = []  # bars用来保存foos的next level nodes，然后完成一次循环后，再交换。见下面实现即可。
        foobars = [foos, bars]

        # 使用x变量在两个数组之间切换。
        # 因为我们每完成一次循环，要把下一级数组作为本级数组，
        # 然后把本级数组清空，用来保存下一级数组。
        x = 0

        __max_depth = self.max_depth()  # 得到tree的层数，用来遍历每一层。

        # 遍历树的所有层。
        for d in range(__max_depth):  # 我们其实用不上d这个变量，只是要这么多的循环次数。
            # 遍历本层nodes，生成下一层的list。
            # 初始化为foobars[0]，里面是foos的初始值，也就是root。
            # 后续会是一层一层往下走。
            for n in foobars[x]:
                # 按顺序遍历本层的每一个node，然后生成下一层的node list，因为本层是从左到右，
                # 下一层也是从左到右这样，所以每一层的list都是按顺序排列的。
                if n.left is not None:
                    foobars[1 - x].append(n.left)
                if n.right is not None:
                    foobars[1 - x].append(n.right)

            # 遍历完本层后，拿出本层的rightmost元素
            rightmost = foobars[x][len(foobars[x]) - 1]
            print(rightmost.data)

            # 接下来要进入下一次循环了
            # 要使用下一层的node list
            x = 1 - x  # 因此，交换一下数组
            foobars[1 - x] = []  # 清空本层数组，用于下一次循环中保存下下层node list。


print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

tree = BinaryTree()
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.print_tree()
print("depth: ", tree.max_depth())

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

tree2 = BinaryTree()
tree2.insert(1)
tree2.insert(2)
tree2.insert(3)
tree2.print_tree()
print("depth: ", tree2.max_depth())

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

tree3 = BinaryTree()
tree3.insert(9)
tree3.insert(4)
tree3.insert(12)
tree3.insert(6)
tree3.insert(3)
tree3.insert(7)
tree3.insert(5)
tree3.print_tree()
print("depth: ", tree3.max_depth())

tree3.right_side_view()
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

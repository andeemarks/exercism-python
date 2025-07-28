class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.original_data = tree_data
        self.root = TreeNode(tree_data[0])

        for node in tree_data[1:]:
            branch = TreeNode(node)
            self.insert(self.root, branch)

    def insert(self, parent: TreeNode, child: TreeNode) -> None:
        if (child.data <= parent.data):
            if parent.left:
                self.insert(parent.left, child)
            else:
                parent.left = child

        if (child.data > parent.data):
            if parent.right:
                self.insert(parent.right, child)
            else:
                parent.right = child

    def data(self):
        return self.root

    def sorted_data(self) -> TreeNode:
        return self.add_smallest(self.root, [])

    def add_smallest(self, current: TreeNode, results: list[str]) -> list[str]:
        if current.left:
            results = self.add_smallest(current.left, results)

        results.append(current.data)

        if current.right:
            return self.add_smallest(current.right, results)
        
        return results

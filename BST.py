class BST:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    def insert_val(self, data):
        if data < self.data:
            if self.lchild:
                self.lchild.insert_val(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert_val(data)
            else:
                self.rchild = BST(data)
        
    def search_val(self, data):
        if self.data == data:
            print(f'Value {data} is present in the BST.')
            return
        elif data < self.data:
            if self.lchild:
                self.lchild.search_val(data)
            else:
                print(f'Value {data} is not present in the BST!')
        else:
            if self.rchild:
                self.rchild.search_val(data)
            else:
                print(f'Value {data} is not present in the BST!')
    
    def pre_order(self):
        print(self.data, '-->', end=' ')
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()
    
    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.data, '-->', end=' ')
        if self.rchild:
            self.rchild.in_order()
    
    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.data, '-->', end=' ')
    
    def level_order(self):
        if not self:
            return
        queue = [self]
        while queue:
            temp = queue.pop(0)
            print(temp.data, '-->', end=' ')
            if temp.lchild:
                queue += [temp.lchild]
            if temp.rchild:
                queue += [temp.rchild]

    def del_value(self, data):
        if data < self.data:
            if self.lchild:
                self.lchild = self.lchild.del_value(data)
            else:
                print(f'Value {data} is not present in the BST!')
        elif data > self.data:
            if self.rchild:
                self.rchild = self.rchild.del_value(data)
            else:
                print(f'Value {data} is not present in the BST!')
        else:
            if not self.lchild:
                return self.rchild
            elif not self.rchild:
                return self.lchild

            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.data = node.data
            self.rchild = self.rchild.del_value(node.data)
        return self

    def get_min(self):
        node = self
        while node.lchild:
            node = node.lchild
        print(f'Smallest value in the BST is {node.data}')
    
    def get_max(self):
        node = self
        while node.rchild:
            node = node.rchild
        print(f'Biggest value in the BST is {node.data}')


def tree_height(root):
    if root is None:
        return 0
    return 1 + max(tree_height(root.lchild), tree_height(root.rchild))

def get_count(node):
    if not node:
        return 0
    return 1 + get_count(node.lchild) + get_count(node.rchild)

def are_identical(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    return (
        tree1.data == tree2.data and
        are_identical(tree1.lchild, tree2.lchild) and
        are_identical(tree1.rchild, tree2.rchild)
    )

def sum_of_nodes(root):
    if root is None:
        return 0
    return root.data + sum_of_nodes(root.lchild) + sum_of_nodes(root.rchild)

def sum_of_leaf_nodes(root):
    if root is None:
        return 0
    if root.lchild is None and root.rchild is None:
        return root.data
    return sum_of_leaf_nodes(root.lchild) + sum_of_leaf_nodes(root.rchild)




if __name__ == '__main__':
    # Clear the console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # Example usage of the BST class
    bst = BST(10)
    li = [6, 1, 3, 6, 98, 3, 7]
    for i in li:
        bst.insert_val(i)

    # bst.del_value(1)
    # bst.search_val(3)
    # print(f'Total value in the BST is {get_count(bst)}')
    # print()
    # bst.get_min()
    # bst.get_max()
    # print('\n', tree_height(bst))
    # bst.del_value(10)

    bst.pre_order()
    print()
    bst.in_order()
    print()
    bst.post_order()
    print()
    bst.level_order()


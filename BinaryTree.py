class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    def insert_val(self, data):
        queue = [self]
        while queue:
            node = queue.pop(0)
            if not node.lchild:
                node.lchild = BinaryTree(data)
                return
            else:
                queue.append(node.lchild)
            
            if not node.rchild:
                node.rchild = BinaryTree(data)
                return
            else:
                queue.append(node.rchild)

    def delete_val(self, data):
        queue = [self]
        target = None
        last = None
        parent_last = None
        while queue:
            last = queue.pop(0)
            if last.data == data:
                target = last
            if last.lchild:
                parent_last = last
                queue.append(last.lchild)
            if last.rchild:
                parent_last = last
                queue.append(last.rchild)
        if target:
            target.data = last.data
            if parent_last.rchild == last:
                parent_last.rchild = None
            else:
                parent_last.lchild = None
            del last

    def pre_order(self):
        print(self.data, '-->', end=' ')
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()


bt = BinaryTree(3)
bt.insert_val(5)
bt.insert_val(10)
bt.pre_order()

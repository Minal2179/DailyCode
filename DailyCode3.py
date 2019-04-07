class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self, root):
        stack = []

        def encode(node):
            if node:
                stack.append(str(node.val))
                encode(node.left)
                encode(node.right)
            else:
                stack.append("empty")

        encode(root)
        return ','.join(stack)

    def deserialize(self, data):

        def decode(serial_str):

            each = next(serial_str)
            if each == "empty":
                return None

            node = Node(each)
            node.left = decode(serial_str)
            node.right = decode(serial_str)
            return node

        serial_str = iter(data.split(','))
        return decode(serial_str)

    # def serialize(self, node):
    #     stack = []
    #     serial = ''
    #     if node:
    #         stack.append(node)
    #         serial += node.val
    #     else:
    #         return ''
    #     while stack:
    #         top = stack.pop()
    #         if top:
    #             print(top.val)
    #             print(stack)
    #             print(serial)
    #             stack.append(top.right)
    #             stack.append(top.left)
    #             if top.left:
    #                 left = True
    #                 serial += ','
    #                 serial += top.left.val
    #             else:
    #                 serial += ', None'
    #
    #             if top.right:
    #                 right = True
    #                 serial += ','
    #                 serial += top.right.val
    #
    #             else:
    #                 serial += ', None'
    #     return serial
    #
    #
    # def deserialize(self, serial):
    #     serial_stack = serial.split(',')
    #     stack = []
    #     while serial_stack:
    #         stack.append(serial_stack.pop(0))



if __name__ == "__main__":
    test = Node('root', Node('left', Node('left.left')), Node('right'))
    serial = test.serialize(test)
    print(serial)
    print(test.deserialize(serial).left.left.val)
class Solution:
    def isValidSerialization(self, preorder: 'str') -> 'bool':
        stack = []
        nodes = preorder.split(",")
        for i in range(len(nodes)):
            val = nodes[i]
            if val != '#':
                stack.append([False, False])
            else:
                stack.append([True, True])
                element = stack[-1]
                while element[0] and element[1]:
                    stack.pop()
                    if len(stack) == 0:
                        if i == len(nodes) - 1:
                            return True
                        else:
                            return False
                    element = stack[-1]
                    if element[0]:
                        element[1] = True
                    else:
                        element[0] = True

        return len(stack) == 0

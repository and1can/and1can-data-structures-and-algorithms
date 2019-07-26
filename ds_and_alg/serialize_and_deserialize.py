# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def serializeHelper(root, data): 
    if root: 
        data.append(root.val)
        serializeHelper(root.left, data)
        serializeHelper(root.right, data)
    else: 
        data.append(None)
    return data

def deserializeHelper(data): 
    if data[0] == None: 
        data.pop(0)
        return None
    else: 
        curr = TreeNode(data.pop(0))
        curr.left = deserializeHelper(data)
        curr.right = deserializeHelper(data)
        return curr

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return serializeHelper(root, [])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root = TreeNode(data.pop(0))
        if root.val != None: 
            root.left = deserializeHelper(data)
            root.right = deserializeHelper(data)
        else: 
            return None
        
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        if root.left is None and root.right is None:
            return str(root.val) + ""
        elif root.left is None:
            return str(root.val) + "()" + "(" + self.serialize(root.right) + ")"
        elif root.right is None:
            return str(root.val) + "(" + self.serialize(root.left) + ")"
        return str(root.val) + "(" + self.serialize(root.left) + ")" + "(" + self.serialize(root.right) + ")"

    def deserialize(self, s):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if s is None or len(s) == 0: return None
        firstParen = s.find("(")
        if firstParen == -1:
            val = int(s)
        else:
            val = int(s[0: firstParen])

        cur = TreeNode(val)

        if firstParen == -1: return cur

        start = firstParen
        leftParenCount = 0
        for i in range(start, len(s)):
            if s[i] == '(':
                leftParenCount += 1
            elif s[i] == ')':
                leftParenCount -= 1
            if leftParenCount == 0 and start == firstParen:
                cur.left = self.deserialize(s[start + 1: i])
                start = i + 1
            elif leftParenCount == 0:
                cur.right = self.deserialize(s[start + 1: i])
        return cur

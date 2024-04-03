class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    # Print inorder traversal
    def print(self):
        if self.left is not None:
            self.left.print()
        print(f"{self.data}", end=" ")
        if self.right is not None:
            self.right.print()

    def insert(self, val):
        # Special case for empty tree
        if self.data is None:
            self.data = val
            return

        # <= causes duplicate elements to be sent left
        if val <= self.data:
            if self.__hasLeft():
                self.left.insert(val)
            else:
                self.left = node(val)
        else:
            if self.__hasRight():
                self.right.insert(val)
            else:
                self.right = node(val)
    
    def remove(self, val):
        # Get node to remove
        target = self.__findNode(val)

        if val is not target.data:
            raise RuntimeError("ERROR: value could not be found in tree")
    
    # Return parent of node in tree rooted at head
    def parent(self, root):
        # Case where node has no parent, return self
        if self.data is root.data:
            return self
        
        # Node is to the left
        if self.data <= root.data:
            # Parent found
            if root.left.data is self.data:
                return root
            # Parent not yet found, recurse
            else:
                return self.parent(root.left)


    def isEmpty(self) -> bool:
        return self.data is None


    def __findNode(self, val):
        # Check for empty tree
        if self.data is None:
            raise RuntimeError("ERROR: Cannot search empty tree")

        # Base case: node is external (nowhere left to search)
        if self.__isExternal():
            return self
        
        if val < self.data:
            return self.left.__findNode(val) if self.__hasLeft() else self
        elif val > self.data:
            return self.right.__findNode(val) if self.__hasRight() else self
        else:
            return self               


    def __isExternal(self) -> bool:
        return not (self.__hasLeft and self.__hasRight)

    def __hasLeft(self) -> bool:
        return self.left is not None
    
    def __hasRight(self) -> bool:
        return self.right is not None
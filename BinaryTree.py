class newNode():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


""" Inorder traversal of a binary tree"""

''''def inorder(temp):
    if (not temp):
      return

    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)'''''

def IterativeInorder(root):
    if(root==None):
        return
    s=[]
    current=root
    while(current!=None or len(s)>0):
        while(current!=None):
            s.append(current)
            current=current.left
        current=s.pop()
        print(current.data)
        current=current.right
def preOrder(temp):
    if (not temp):
      return
    print(temp.data,end=" ")
    preOrder(temp.left)
    preOrder(temp.right)

def Iterative_preOrder(root):
    if root is None:
        return
    s1=[]
    s1.append(root)
    while(len(s1)>0 ):
        temp=s1.pop()
        print(temp.data)
        if temp.right is not None:
            s1.append(temp.right)
        if temp.left is not None:
            s1.append(temp.left)
def postOrder(temp):
    if (not temp):
      return

    postOrder(temp.left)
    postOrder(temp.right)
    print(temp.data, end=" ")


def postOrderIterative(root):
    # Check for empty tree
    if root is None:
        return

    stack = []

    while (True):

        while (root):
            # Push root's right child and then root to stack
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)

            # Set root as root's left child
            root = root.left

            # Pop an item from stack and set it as root
        root = stack.pop()

        # If the popped item has a right child and the
        # right child is not processed yet, then make sure
        # right child is processed before root
        ab=peek(stack)
        if (root.right is not None and
                ab == root.right):
            stack.pop()  # Remove right child from stack
            stack.append(root)  # Push root back to stack
            root = root.right  # change root so that the
            # righ childis processed next

        # Else print root's data and set root as None
        else:
            print(root.data)
            root = None

        if (len(stack) <= 0):
            break
def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None
# A iterative function to do postorder traversal of
# a given binary tree


# Driver code
if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(11)
    root.left.left = newNode(7)
    root.right = newNode(9)
    root.right.left = newNode(15)
    root.right.right = newNode(8)

    print("Inorder traversal before insertion:", end=" ")
    #inorder(root)
    #IterativeInorder(root)
    #preOrder(root)
    #Iterative_preOrder(root)
    #postOrder(root)
    postOrderIterative(root)
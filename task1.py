class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_in_bst(root):
    if root is None:
        return None  # Якщо дерево порожнє, повертаємо None
    current = root
    # Рухаємось по правих гілках, поки це можливо
    while current.right is not None:
        current = current.right
    return current.value

# Приклад використання
if __name__ == "__main__":
    # Створюємо приклад дерева
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(25)

    # Знаходимо найбільше значення
    max_value = find_max_in_bst(root)
    print("Найбільше значення в BST:", max_value)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min_in_bst(root):
    if root is None:
        return None  # Якщо дерево порожнє, повертаємо None
    current = root
    # Рухаємось по лівих гілках, поки це можливо
    while current.left is not None:
        current = current.left
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

    # Знаходимо найменше значення
    min_value = find_min_in_bst(root)
    print("Найменше значення в BST:", min_value)

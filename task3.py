class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_values_in_bst(root):
    if root is None:
        return 0  # Якщо дерево порожнє, повертаємо 0
    # Рекурсивно обробляємо ліве та праве піддерево, а потім додаємо значення поточного вузла
    return sum_of_values_in_bst(root.left) + root.value + sum_of_values_in_bst(root.right)

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

    # Знаходимо суму всіх значень
    total_sum = sum_of_values_in_bst(root)
    print("Сума всіх значень в дереві:", total_sum)

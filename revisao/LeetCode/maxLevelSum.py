from collections import deque
from typing import Optional

# Definição básica para um nó da árvore (fornecida pelo LeetCode)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Inicializa variáveis para guardar o recorde
        max_sum = float('-inf') # Começa com o menor valor possível
        best_level = 1
        current_level = 1
        
        # A fila começa com a raiz da árvore
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            # Processar todos os nós do nível atual
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # Adicionar os "filhos" para a próxima rodada (próximo nível)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Verificar se este nível bateu o recorde anterior
            if level_sum > max_sum:
                max_sum = level_sum
                best_level = current_level
            
            current_level += 1
            
        return best_level
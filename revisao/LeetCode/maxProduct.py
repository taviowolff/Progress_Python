class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []
        
        # Função auxiliar para calcular a soma de cada nó e seus filhos
        def get_sum(node):
            if not node:
                return 0
            
            # A soma deste nó é: seu valor + soma da esquerda + soma da direita
            current_sum = node.val + get_sum(node.left) + get_sum(node.right)
            
            # Guarda essa soma na nossa lista para testar depois
            all_sums.append(current_sum)
            return current_sum
        
        # 1. Calcula a soma total (o último elemento de all_sums será o total)
        total_sum = get_sum(root)
        
        # 2. Calcula o produto máximo testando cada subárvore gravada
        max_prod = 0
        for s in all_sums:
            product = s * (total_sum - s)
            if product > max_prod:
                max_prod = product
        
        # Retorna o resultado com o módulo solicitado (10^9 + 7)
        return max_prod % (10**9 + 7)
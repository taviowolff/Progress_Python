class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total_sum = 0
        min_abs_value = float('inf')
        negative_count = 0
        
        for row in matrix:
            for val in row:
                # 1. Soma o valor absoluto de cada número
                total_sum += abs(val)
                
                # 2. Conta quantos negativos existem
                if val < 0:
                    negative_count += 1
                
                # 3. Mantem rastro do menor valor absoluto encontrado
                if abs(val) < min_abs_value:
                    min_abs_value = abs(val)
        
        # Se a contagem de negativos for ímpar, subtraí duas vezes o menor valor
        # (Uma para remover ele da soma total e outra para torná-lo negativo)
        if negative_count % 2 != 0:
            return total_sum - 2 * min_abs_value
            
        return total_sum
    
# exemplo de uso
sol = Solution()
print(sol.maxMatrixSum([[1,-1],[-1,1]]))
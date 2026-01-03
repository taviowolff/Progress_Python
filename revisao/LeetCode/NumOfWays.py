class Solution:
    def numOfWays(self, n: int) -> int:
        # Constante do módulo solicitada no problema
        MOD = 10**9 + 7
        
        # Valores iniciais para n = 1
        aba = 6
        abc = 6
        
        # Calculando para cada linha de 2 até n
        for _ in range(1, n):
            # Guardamos os valores anteriores para o cálculo
            novo_aba = (3 * aba + 2 * abc) % MOD
            novo_abc = (2 * aba + 2 * abc) % MOD
            
            aba, abc = novo_aba, novo_abc
            
        return (aba + abc) % MOD

# Teste rápido
sol = Solution()
print(f"Resultado para n=1: {sol.numOfWays(1)}")    # Saída: 12
print(f"Resultado para n=5000: {sol.numOfWays(5000)}") # Saída: 30228214
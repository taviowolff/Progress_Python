class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # Inicializa a matriz DP
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Caso base: Se s2 estiver vazia, temos que deletar tudo de s1
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
            
        # Caso base: Se s1 estiver vazia, temos que deletar tudo de s2
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        # Preenchendo a tabela
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    # Caracteres iguais: custo zero
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # Caracteres diferentes: escolhe o mínimo entre deletar de s1 ou s2
                    dp[i][j] = min(
                        dp[i-1][j] + ord(s1[i-1]),
                        dp[i][j-1] + ord(s2[j-1])
                    )

        return dp[m][n]
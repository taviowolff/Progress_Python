import math

class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        total_sum = 0
        
        for num in nums:
            divisors = self.get_divisors(num)
            if len(divisors) == 4:
                total_sum += sum(divisors)
                
        return total_sum

    def get_divisors(self, n: int) -> set:
        divs = set()
        # Apenas a raiz quadrada de n
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divs.add(i)
                divs.add(n // i)
                # Se em qualquer momento passar de 4, já podemos parar
                if len(divs) > 4:
                    return divs
        return divs

# exemplo de uso
sol = Solution()    
print(sol.sumFourDivisors([21, 4, 7]))  # Output: 32

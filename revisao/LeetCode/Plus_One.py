from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        # Percorre de trás para frente
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s // 10
        
        # Se após o loop ainda houver carry (ex: [9,9] + 1)
        if carry:
            digits = [1] + digits
            
        return digits

# Exemplo de uso
if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
    print(solution.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]  
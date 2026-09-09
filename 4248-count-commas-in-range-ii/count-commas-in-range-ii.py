class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        threshold = 1000
        
        while n >= threshold:
            total_commas += (n - threshold + 1)
            threshold *= 1000  # Move to the next comma tier (1,000,000, etc.)
            
        return total_commas
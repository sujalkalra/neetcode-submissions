class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n in seen:
                return False
            seen.add(n)
            temp = 0
            for c in str(n):
                temp += int(c)**2
            n = temp
            if n == 1:
                return True
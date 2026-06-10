class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOne(n):
            count = 0
            while n:
                n&=n-1
                count+=1
            return count

        res = []
        for i in range(n+1):
            res.append(countOne(i))
        return res
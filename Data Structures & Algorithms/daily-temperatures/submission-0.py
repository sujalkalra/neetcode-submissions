class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        for i in range(n):
            stack = [temperatures[i]]
            for j in range(i,n):
                if temperatures[j]<=stack[0]:
                    stack.append(temperatures[j])
                else:
                    res[i]=len(stack)-1
                    break
        return res
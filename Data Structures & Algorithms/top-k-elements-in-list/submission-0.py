class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)

        sl = sorted(frequency.items() ,key =  lambda x:x[1])
        print(sl)
        res = []
        for i in sl[len(sl)-k:len(sl)]:
            res.append(i[0])
        return res

import bisect
class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.insert(bisect.bisect_left(self.stream,num),num)

    def findMedian(self) -> float:
        if len(self.stream)%2 == 0:
            return (self.stream[len(self.stream)//2-1]+self.stream[len(self.stream)//2])/2
        else:
            return self.stream[len(self.stream)//2]
        
class Solution:
    def findSubsequences(self, nums):
        self.arr = nums
        self.hashSet = set()
        self.recursion([], 0)
        return list(self.hashSet)
    
    def recursion(self, arrayList, index):
        if len(arrayList) >= 2:
            self.hashSet.add(tuple(arrayList))
        
        for i in range(index, len(self.arr)):
            if len(arrayList) == 0 or self.arr[i] >= arrayList[-1]:
                arrayList.append(self.arr[i])
                self.recursion(arrayList, i + 1)
                arrayList.pop()

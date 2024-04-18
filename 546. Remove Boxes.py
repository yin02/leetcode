# 546. Remove Boxes (hard)
# Zhengyan Hu

class Solution(object):
    def removeBoxes(self, boxes):
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        return self.operate(boxes, 0, n - 1, 0, dp)

    def operate(self, boxes, i, j, k, dp):
        if i > j:
            return 0
        if dp[i][j][k] > 0:
            return dp[i][j][k]
        
        res = (k + 1) * (k + 1) + self.operate(boxes, i + 1, j, 0, dp)
        
        for m in range(i + 1, j + 1):
            if boxes[i] == boxes[m]:
                res = max(res, self.operate(boxes, i + 1, m - 1, 0, dp) + self.operate(boxes, m, j, k + 1, dp))
        
        dp[i][j][k] = res
        return res

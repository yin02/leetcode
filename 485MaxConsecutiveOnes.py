#485. Max Consecutive Ones(Easy)
#Zhengyan Hu

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        dp = [0] * len(nums)
        max_count = 0
        if nums[0] == 0:
            dp[0] = 0
        else:
            dp[0] = 1
            max_count = 1

        for i in range(1, len(nums)):
            if nums[i] == 1:
                dp[i] = dp[i - 1] + 1
                max_count = max(dp[i], max_count)
            else:
                dp[i] = 0
        return max_count

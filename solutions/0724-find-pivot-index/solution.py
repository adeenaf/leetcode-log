class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        ans = []
        sumLeft = []
        sumRight = []
        ans.append(nums[0])
        for i in range(1, len(nums)):
            ans.append(ans[i - 1] + nums[i])

        for i in range(len(nums)):
            sumLeft.append(ans[i] - nums[i])
            sumRight.append(total - ans[i])
            if sumLeft[i] == sumRight[i]:
                return i
        return -1

class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []          # Constraints に 0 <= nums.length があるので空入力対策

        result = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:      # 切れ目
                end = nums[i-1]
                if start == end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))
                start = nums[i]

        # 最後の区間
        end = nums[-1]
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end))

        return result

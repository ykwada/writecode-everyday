class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0 # ポインタを2つ用意する
        for fast in range(1, len(nums)): # 先行ポインタが走査する 
            if nums[fast] != nums[slow]: # 2つのポインタの値が異なるとき
                slow += 1                # slowを進める
                nums[slow] = nums[fast]  # 先で見つけた異なった値を格納。（詰める） 
        return slow + 1                  # 要素の個数を返す

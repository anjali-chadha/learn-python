class TwoSum(object):
    def twoSum(self, nums, target):
        """
       :type nums: List[int]
       :type target: int
       :rtype: List[int]
       """
        dictionary = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in dictionary:
                return [dictionary[m], i]
            else:
                dictionary[n] = i
        return []

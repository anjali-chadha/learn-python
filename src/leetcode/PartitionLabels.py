#https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        last = {c: i for i, c in enumerate(S)}
        L = R = 0;
        for i, c in enumerate(S):
            R = max(R, last[c])
            if i == R:
                result.append(R + 1 - L)
                L = R + 1
        return result
        
        

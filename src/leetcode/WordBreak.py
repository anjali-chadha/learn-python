class WordBreak(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        ok[i] tells whether s[:i] can be built.
     n = len(s)
        is_breakable = [False] * (n+1)
        is_breakable[0] = True
        for i in xrange(1,n+1):
            for j in xrange(0,i):
                if is_breakable[j] and s[j:i] in wordDict:
                    is_breakable[i] = True
                    break
        return is_breakable[n]
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]

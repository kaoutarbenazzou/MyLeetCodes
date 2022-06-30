class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = dict()

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    res = i == len(s)
                else:
                    match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        res = dp(i, j + 2) or (match and dp(i + 1, j))
                    else:
                        res = match and dp(i + 1, j + 1)

                memo[i, j] = res

            return memo[i, j]

        return dp(0, 0)
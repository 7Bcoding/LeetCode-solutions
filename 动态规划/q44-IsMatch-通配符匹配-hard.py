class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 解法：动态规划
        # 在给定的模式 p 中，只会有三种类型的字符出现：
        # 1. 小写字母 a-z，可以匹配对应的一个小写字母；
        # 2. 问号 ?，可以匹配任意一个小写字母；
        # 3. 星号 *∗，可以匹配任意字符串，可以为空，也就是匹配零或任意多个小写字母。
        # 其中「小写字母」和「问号」的匹配是确定的，而「星号」的匹配是不确定的，因此我们需要枚举所有的匹配情况。
        # 我们用 dp[i][j] 表示字符串 s 的前 i 个字符和模式 p 的前 j 个字符是否能匹配。在进行状态转移时，我们
        # 可以考虑模式 p 的第 j 个字符 p[j]，与之对应的是字符串 s 中的第 i 个字符 s[i]
        # 1. 如果 p[j] 是小写字母，那么 s[i] 也必须是小写字母，状态转移方程为：
        # dp[i][j] = (s[i]==p[j]) ^ dp[i-1][j-1]
        # 2. 如果p[j]为问号，则s[i]为任意字符都能匹配。状态转移方程为：
        # dp[i][j] = dp[i-1][j-1]
        # 3. 如果 p[j] 是星号，那么同样对 s[i] 没有任何要求，但是星号可以匹配零或任意多个小写字母，因此状态转
        # 移方程分为两种情况，即使用或不使用这个星号：
        # dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
        # 如果我们不使用这个星号，那么就会从 dp[i][j-1] 转移过来，如果我们使用这个星号，那么就会从 dp[i-1][j] 转移而来。
        # 归纳如下：
        # 1. dp[i][j] = dp[i−1][j−1], ———— s[i]与p[j]相同或p[j]是问号
        # 2. dp[i][j] = dp[i][j−1]∨dp[i−1][j], ———— p[j]为星号
        # 3. dp[i][j] = False, ———— 其他情况
        # 边界条件：
        # 1. dp[0][0] = dp[0][0]=True，即当字符串 s 和模式 p 均为空时，匹配成功；
        # 2. dp[i][0] = dp[i][0]=False，即空模式无法匹配非空字符串；
        # 3. dp[0][j] 需要分情况讨论：因为星号才能匹配空字符串，所以只有当模式 p 的前 j 个字符均为星号时，dp[0][j] 才为真。

        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


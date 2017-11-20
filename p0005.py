from timeit import Timer


def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        # Transform S into t.
        # For example, S = "abba", t = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        t = '#'.join('^{}$'.format(s))
        n = len(t)
        p = [0] * n
        c, r = 0, 0

        # import sys
        # sys.setcheckinterval(100000)

        for i in range(1, n-1):
                p[i] = (r > i) and min(r - i, p[2*c - i]) # equals to i' = c - (i-c)
                # Attempt to expand palindrome centered at i
                while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                        p[i] += 1

                # If palindrome centered at i expand past r,
                # adjust center based on expanded palindrome.
                if i + p[i] > r:
                        c, r = i, i + p[i]

        # Find the maximum element in p.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(p))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]


t = Timer(lambda: longestPalindrome('babad'))
print(t.timeit(number=10))

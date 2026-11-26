class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        """The left column: converting part of word1 into nothing
        "it takes i operations (deletions) to turn i letters into nothing."
        Converting "h" (1 letter) into "" → delete the h → 1 operation.
        Converting "ho" (2 letters) into "" → delete h, delete o → 2 operations.
        Converting "hor" (3 letters) into "" → delete all 3 → 3 operations."""

        for i in range(m + 1):
            dp[i][0] = i

        """The top row: converting nothing into part of word2

            Now flip it around: you have nothing (empty string), and you want to build up toward "r", then "ro", then "ros". The only operation that can create letters out of nothing is inserting.

            Converting "" into "r" → insert r → 1 operation.
            Converting "" into "ro" → insert r, insert o → 2 operations.
            Converting "" into "ros" → insert all 3 letters → 3 operations.

            Same idea, mirrored: converting nothing into a string of length j always costs exactly j insertions."""

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if(word1[i - 1] == word2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                                        #  replace       delete      insert
        return dp[m][n]


"""Step 1 — what does dp[i][j] mean?

Same counting-from-1 convention as LCS: dp[i][j] = minimum operations to convert the first i characters of word1 into the first j characters of word2.

Step 2 — what's the last operation?

Look at the last characters, word1[i-1] and word2[j-1]:

Case A — they match: no operation needed for this pair — just carry forward whatever it cost to convert everything before these matching characters: dp[i-1][j-1].

Case B — they don't match: you must do one operation here, and there are three choices for what that operation is:

Replace word1[i-1] with word2[j-1]: this resolves both last characters at once, so you fall back to dp[i-1][j-1] (one character consumed from each) + 1 for this replace.
Delete word1[i-1]: you've consumed one character from word1 but none from word2 yet, so fall back to dp[i-1][j] + 1 for the delete.
Insert a character into word1 matching word2[j-1]: this consumes one character from word2 but none (yet) from word1, so fall back to dp[i][j-1] + 1 for the insert.
Step 3 & 4 — recurrence

Since we want the minimum operations, take min across the three choices in Case B:

if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                       #  replace       delete      insert

Base case: dp[i][0] = i (converting i characters into an empty string needs exactly i deletions). dp[0][j] = j (converting an empty string into j characters needs exactly j insertions). These aren't 0 like LCS's base case — here, even with one string empty, there's real work to do (deleting or inserting everything), so the base case itself needs its own small loop to fill in."""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        sorted_pairs = sorted(count.items(), key = lambda pair: pair[1], reverse = True)

        result = ""
        for ch, freq in sorted_pairs:
            result += ch * freq

        return result

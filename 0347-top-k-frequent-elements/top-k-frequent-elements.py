class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        sorted_pairs = sorted(count.items(), key = lambda pair: pair[1], reverse = True)
        top_k_pairs = sorted_pairs[:k]
        result = [pair[0] for pair in top_k_pairs]

        return result

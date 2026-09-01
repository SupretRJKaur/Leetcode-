from collections import Counter


class Solution:

    def topKFrequent(self, nums, k):
        # 1. Count frequencies
        count = Counter(nums)

        # 2. Bucket where index = frequency
        # max possible frequency is len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        # 3. Gather top k elements from highest frequency bucket down to lowest
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
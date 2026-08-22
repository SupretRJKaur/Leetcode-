from collections import Counter


class Solution:

    def leastInterval(self, tasks, n):
        counts = [0] * 26  # Line 5
        for task in tasks:  # Line 6
            counts[ord(task) - ord("A")] += 1  # Line 7

        max_freq = max(counts)  # Line 9
        max_count = counts.count(max_freq)  # Line 10

        ans = (max_freq - 1) * (n + 1) + max_count  # Line 12

        return max(ans, len(tasks))  # Line 14
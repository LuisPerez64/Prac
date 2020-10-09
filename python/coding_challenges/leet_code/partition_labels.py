"""
Question:
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so
that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.


Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.

"""

from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        return self.first_implementation(S)

    def first_implementation(self, S: str) -> List[int]:
        """
        iterate over the string and create a dict with the letters as the key and their last seen index.
        After the iteration find common groups that have an upper bound < another groups start.
        base this on the first letter in the group, and create each partition based on when it was last seen.
        Do this for the letter that comes next incrementing this partition until the next interval.
        Once we reach a letter that has not been seen in the previous partition start the process again from that index.
        After the start,end indices are collected return the difference between the end and start of each disjoint
        partition +1 to denote their sizes.
        """
        seen_interval = {}
        for idx, val in enumerate(S):
            if val in seen_interval:
                # update the last seen interval.
                seen_interval[val][1] = idx
            else:
                seen_interval[val] = [idx, idx]
        partitions = []
        # iterate over the intervals sorted based on start time and as long as there is overlap keep consuming.
        for start, end in sorted(seen_interval.values(), key=lambda k: k[0]):
            if not partitions:
                partitions.append([start, end])
            else:
                # if the start of the current partition is before the previous one ended then extend it
                if partitions[-1][1] > start:
                    partitions[-1][1] = max(end, partitions[-1][1])
                else:
                    # the end of the previous interval is met. start a new one.
                    partitions.append([start, end])
        return [x[1] - x[0] + 1 for x in partitions]

Solution().partitionLabels("ababcbacadefegdehijhklij")
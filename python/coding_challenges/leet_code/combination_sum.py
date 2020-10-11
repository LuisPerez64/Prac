"""
REVISIT: This is a twist on the backtracking algo. Not too different from the combination_sum_iii and in a way easier.
Question: https://leetcode.com/problems/combination-sum/
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for
 the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]


Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500

"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.first_implementation(candidates, target)

    def first_implementation(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Use the backtracking algo to get the possible combinations.
        Sort the input as its not stated that its sorted.
        """
        candidates.sort()
        results = []

        def find_valid(remain: int, comb: List[int], choice_idx: int) -> bool:
            if remain == 0:
                # Ensure that we don't place a copy in that can then get mutated elsewhere.
                results.append(list(comb))
                return True
            if remain < 0:
                return False

            for idx in range(choice_idx, len(candidates)):
                comb.append(candidates[idx])
                find_valid(remain - candidates[idx], comb, idx)
                # remove the last candidate added at this iteration.
                comb.pop()

        find_valid(target, [], 0)
        return results

    def failed_implementation(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        The values are all positive integers so the bound check for them producing a solution,
        The input is not guaranteed to be sorted, this would be the first question asked in an
        interview situation.
        For every candidate we check to see if it's past the value wanted.
        If 2 * the candidate is <= the target branch off based on that assumption.
        """
        if not candidates:
            return []
        # sort the candidates list if it's unsorted to make traversal simpler.
        candidates.sort()
        if candidates[0] > target:
            return []
        combinations = []

        def extend_candidate(cur_candidate: list, next_candidate_idx: int):
            cur_sum = sum(cur_candidate)
            if cur_sum == target:
                combinations.append(cur_candidate)

            if cur_sum > target:
                return []

            ret_list = []
            if cur_candidate[-1] + cur_sum <= target:
                valid = extend_candidate(cur_candidate + [cur_candidate[-1]], next_candidate_idx)
                if valid:
                    ret_list.append(valid)
            if next_candidate_idx < len(candidates) and cur_sum + candidates[next_candidate_idx] <= target:
                valid = extend_candidate(cur_candidate + [candidates[next_candidate_idx]], next_candidate_idx + 1)
                if valid:
                    ret_list.append(valid)
            combinations.extend(ret_list)
            return ret_list

        for idx, cur_cand in enumerate(candidates):
            ret = extend_candidate([cur_cand], idx + 1)
            # if ret:
            #     if type(ret[0]) is list:
            #         ret = ret[0]
            #     if type(ret) is not list:
            #         ret = [ret]
            #     combinations.append(ret)
        return combinations

"""
Question: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".
Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]


Constraints:

1 <= folder.length <= 4 * 10^4
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'
folder[i] always starts with character '/'
Each folder name is unique.
"""
from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        return self.first_implementation(folder)

    def first_implementation(self, folder: List[str]) -> List[str]:
        """
        The directories are not guaranteed to be in sorted order. Sort the input in place with heapsort O(n log n)
        If they are then this problem goes into O(n) Time
        Benefit of sorting time goes from O(n^2) to O(n log n).

        Iterate over the sorted array finding common roots. As long as the next item's root is in the previous elt
        remove it. i.e. ['/a'], and comparing '/a/b' need to ensure that '/a/' is what '/a/b' starts with.
        The '/' is needed to weed out cases '/a/b/c' being seen as the subfolder for '/a/b/ca'

        Time Complexity: O(n log n)
            if input is implied to be sorted O(n)
        Space Complexity: O(n)
            if the output is not taken into account O(1)
        """
        if not folder:
            return []
        from heapq import heapify, heappop
        heapify(folder)
        # initialize the output though it could be done in true O(1) space with peaking at
        # the previous element in the heap but that would require a pop push
        result = [heappop(folder)]

        while folder:
            cur = heappop(folder)
            if not cur.startswith(result[-1] + '/'):
                result.append(cur)

        return result

    def second_implementation(self, folder: List[str]) -> List[str]:
        """
        Implementation using a Trie data type which is useful in branching traversals.
        Need to look into the object more, though it's pretty straightforward. Will revisit this once i've implemented the class.

        """
        pass

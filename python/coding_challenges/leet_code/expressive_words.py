"""
Question: https://leetcode.com/problems/expressive-words/

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy.



Example:
Input:
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.


Constraints:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters

"""
from typing import List


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        return self.pulled_implementation(S, words)

    #     def first_implementation(self, S: str, words: List[str]) -> int:
    #         """
    #         Create a Trie and iterate through it.
    #         Check to see if a word end is met by continuing on the path of the current word
    #         i.e. heeelllloooo =>
    #             h he hee ingest all remaining 'es' helllloooo
    #             he hel hell helll = Ingest remaining ls helloooo
    #             hell hello (is word end but there's still chars to ingest) helloo * Ingest all remaining os
    #             At eac iteration check if word in the Trie, else check if word startsWith in the dict.
    #             Maybe creating a method inside the Trie to do this instead of two external calls.
    #         """
    #         for word in words:
    #             # Check to see if the word could be created by modifying the input

    def pulled_implementation(self, S: str, words: List[str]) -> int:
        count = 0
        for word in words:
            i = 0
            j = 0
            match = False
            while i < len(S) and j < len(word):
                sCharCount = 0
                sChar = S[i]
                while i < len(S) and S[i] == sChar:
                    sCharCount += 1
                    i += 1
                wCharCount = 0
                match = False
                while j < len(word) and sChar == word[j]:
                    j += 1
                    wCharCount += 1
                if sCharCount < 3 and sCharCount == wCharCount:
                    match = True
                    continue
                elif sCharCount > 2 and sCharCount >= wCharCount:
                    match = True
                    continue
                else:
                    match = False
                    break
            if match and i == len(S) and j == len(word):
                count += 1
        return count

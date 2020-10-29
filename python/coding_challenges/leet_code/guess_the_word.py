"""
REVISIT: Need to annotate this problem, and walk through the solution.  Study points set algebra.
Question: https://leetcode.com/problems/guess-the-word/
This problem is an interactive problem new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret.

You may call master.guess(word) to guess a word.  The guessed word should have type string and must be from the original
 list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to
 the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10
 or less calls to master.guess and at least one of these guesses was the secret, you pass the testcase.

Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.
The letters of each word in those testcases were chosen independently at random from 'a' to 'z',
such that every word in the given word lists is unique.

Example 1:
Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

Explanation:

master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
Note:  Any solutions that attempt to circumvent the judge will result in disqualification.
"""
from collections import defaultdict
from random import choice
from typing import List


class Master(object):
    _key = 'hbaczn'

    def guess(self, word):
        return sum([1 if word[idx] == self._key[idx] else 0 for idx in range(len(self._key))])


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        return self.first_implementation(wordlist, master)

    def first_implementation(self, wordlist: List[str], master: 'Master', num_guesses: int = 10) -> None:
        """
        Find commonolaties between the words. Try to choose the words that have the most
        distinct values as the guesses.
        If each word is 6 letters long then the possible combinations are 26 ^ 6
        Sort the list to get groupings in a bit more uniformed manner.
        Use the first word as the initial basis.
        Break down the current word, and return other words in the list that have
            the same structure as it.
            Prev correct
            Base cases:
                Result = 0:
                    Eliminate all words that have an element in the same index
                    as the current word. <Best>
                Result = 6:
                    Found the word. Guess pool relays just that word <Best>
                Result = 3+:
                    Try out a string that matches the first and second half of the previous word
                    Select the pool thats got the higher match. Continue until the result is 6.
        """
        word_weights = defaultdict(dict)
        history = set()

        # Create the dictionary pointing from each word to the next in regards to similarity
        for idx, wrd in enumerate(wordlist):
            for cmp in wordlist[idx:]:
                if wrd == cmp:
                    continue
                # Find the similarity between the two words as a weighted value.
                count = 0
                for idx_j in range(len(wrd)):
                    count += 1 if wrd[idx_j] == cmp[idx_j] else 0
                word_weights[wrd].setdefault(count, set()).add(cmp)
                word_weights[cmp].setdefault(count, set()).add(wrd)

        # valid_guesses = set(wordlist)
        guess_pool = set(wordlist)
        idx = 0
        for idx in range(num_guesses):
            cur_word = choice(list(guess_pool))
            num_correct = master.guess(cur_word)
            history.add(cur_word)

            if num_correct == len(wordlist[0]):
                break
            guess_pool = guess_pool.intersection(word_weights[cur_word][num_correct]).difference(history)
            # guess_pool = valid_guesses.intersection(word_weights[cur_word][num_correct]).difference(history)
            # valid_guesses = guess_pool
        print(idx)


if __name__ == '__main__':
    wordlist = ["gaxckt", "trlccr", "jxwhkz", "ycbfps", "peayuf", "yiejjw", "ldzccp", "nqsjoa", "qrjasy", "pcldos",
                "acrtag", "buyeia", "ubmtpj", "drtclz", "zqderp", "snywek", "caoztp", "ibpghw", "evtkhl", "bhpfla",
                "ymqhxk", "qkvipb", "tvmued", "rvbass", "axeasm", "qolsjg", "roswcb", "vdjgxx", "bugbyv", "zipjpc",
                "tamszl", "osdifo", "dvxlxm", "iwmyfb", "wmnwhe", "hslnop", "nkrfwn", "puvgve", "rqsqpq", "jwoswl",
                "tittgf", "evqsqe", "aishiv", "pmwovj", "sorbte", "hbaczn", "coifed", "hrctvp", "vkytbw", "dizcxz",
                "arabol", "uywurk", "ppywdo", "resfls", "tmoliy", "etriev", "oanvlx", "wcsnzy", "loufkw", "onnwcy",
                "novblw", "mtxgwe", "rgrdbt", "ckolob", "kxnflb", "phonmg", "egcdab", "cykndr", "lkzobv", "ifwmwp",
                "jqmbib", "mypnvf", "lnrgnj", "clijwa", "kiioqr", "syzebr", "rqsmhg", "sczjmz", "hsdjfp", "mjcgvm",
                "ajotcx", "olgnfv", "mjyjxj", "wzgbmg", "lpcnbj", "yjjlwn", "blrogv", "bdplzs", "oxblph", "twejel",
                "rupapy", "euwrrz", "apiqzu", "ydcroj", "ldvzgq", "zailgu", "xgqpsr", "wxdyho", "alrplq", "brklfk"]
    Solution().first_implementation(wordlist=wordlist, master=Master(), num_guesses=10)

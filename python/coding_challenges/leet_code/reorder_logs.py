"""
Question: https://leetcode.com/problems/reorder-data-in-log-files/
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.



Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""
from typing import List


def reorder_log_files(logs: List[str]) -> List[str]:
    digits = []
    letters = []

    for log in logs:
        split_log = log.split(' ')

        if split_log[1].isnumeric():
            digits.append(log)
        else:
            ident = split_log[0]
            value = " ".join(split_log[1:])
            if len(letters) == 0:
                letters.append(log)
            else:
                # Insert the log into the right location now using insertion_sort
                for existing_idx in range(len(letters)):
                    ex_log = letters[existing_idx]
                    split_ex = ex_log.split(' ')
                    ident_ex = split_ex[0]
                    val_ex = " ".join(split_ex[1:])
                    if value < val_ex or val_ex == value and ident < ident_ex:
                        letters.insert(existing_idx, log)
                        break
                else:
                    letters.append(log)

    return letters + digits


if __name__ == '__main__':
    print(reorder_log_files(["dig1 8 1 5 1", "let4 art can", "let1 art can", "dig2 3 6", "let2 own kit dig",
                             "let3 art zero"]))

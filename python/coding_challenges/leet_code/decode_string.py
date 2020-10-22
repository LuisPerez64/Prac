"""
REVISIT: Annotate the logic, its straightforward but could use a refresh
Question: https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly
k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those
repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""


class Solution:
    def decodeString(self, s: str) -> str:
        return self.first_implementation(s)

    def first_implementation(self, s: str) -> str:
        """
        Implementation without recursion using stacks to capture the operation.
        """
        out_str = ''
        sub_op = []
        repetitions = []
        repeats = ''
        for cur in s:
            if cur.isdigit():
                repeats += cur
            elif cur == '[':
                # if repeats == '':
                #     raise Exception("Invalid input string given for decompression")
                sub_op.append('')
                repetitions.append(int(repeats))
                repeats = ''
            elif cur == ']':
                # Close the previous sub_str out and generate its uncompressed value
                # Add its value to the value of the previous operation as it will also need to be repeated
                cur_str = sub_op.pop() * repetitions.pop()
                if len(sub_op) == 0:
                    out_str += cur_str
                else:
                    sub_op[-1] += cur_str
            else:
                if len(sub_op) == 0:
                    out_str += cur
                else:
                    sub_op[-1] += cur

        return out_str

    def second_implementation(self, s: str) -> str:
        """
        Recursive method for decoding a string of type
        "ab3[c]" -> "abccc"
        """

        def decode(cur_idx: int):
            if cur_idx > len(s):
                return "", cur_idx
            cur_string = ""
            repeats = ""
            while cur_idx < len(s):
                if s[cur_idx].isdigit():
                    # if not valid i.e. "a34"
                    repeats += s[cur_idx]
                    cur_idx += 1
                else:
                    if repeats:
                        cur_idx += 1
                        sub_op, cur_idx = decode(cur_idx)
                        cur_string += (sub_op * int(repeats))
                        repeats = ""
                    elif s[cur_idx] == ']':
                        cur_idx += 1
                        break
                    else:
                        cur_string += s[cur_idx]
                        cur_idx += 1
            return cur_string, cur_idx

        return decode(0)[0]

"""
Question: https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/#!
"""
import unittest


class Decompression(object):
    @staticmethod
    def first_attempt(compressed: str) -> str:
        """
        Operations on the compressed string will grab each sub operation(compressed marker) and allocate space for them
        on a stack. The stack will then generate the expected string for each fully grouped operation based on markers.
        Num(start_marker)...(end_marker) where Num dictates the repetition of the input.
        """
        out_str = ""
        operations_stack = []
        repeats_stack = []
        open_markers = -1
        digit = ''

        # Base functionality is to ingest the input and a multiplier.
        # On each instance of a close bracket pop off the current str and append it to the final
        for idx, cur in enumerate(compressed):
            if cur.isdigit():
                # Get the digit and ingest digits until a bracket is found
                digit += cur
            elif cur == '[':
                # Met an operation grouping, and the number of repetitions should be met in the digits field.
                # Added error handling to denote if its not a digit before then its invalid.
                if digit == '':
                    raise Exception(f"Invalid compression group found. Begins at index {idx}.")
                repeats_stack.append(int(digit))
                operations_stack.append('')
                open_markers += 1
                digit = ''
            elif cur == ']':
                # process the operation and get the compressed fields decompressed in the current block.
                out_str += operations_stack.pop() * repeats_stack.pop()
                open_markers -= 1
            else:
                if open_markers >= 0:
                    operations_stack[open_markers] += cur
                else:
                    out_str += cur

        return out_str

    @staticmethod
    def second_attempt(compressed: str) -> str:
        out_str = ''
        sub_op = []
        repetitions = []
        repeats = ''
        for cur in compressed:
            if cur.isdigit():
                repeats += cur
            elif cur == '[':
                if repeats == '':
                    raise Exception("Invalid input string given for decompression")
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


class Test(unittest.TestCase):
    def test_simple_decompress(self):
        expects = 'aaabbb'
        actual = Decompression.second_attempt('3[a]3[b]')
        self.assertEqual(expects, actual)

    def test_layered_decompress_simple(self):
        expects = 'aaabaaab'
        actual = Decompression.second_attempt('2[3[a]b]')
        self.assertEqual(expects, actual)

    def test_layered_decompress_deep(self):
        expects = 'abbcbbcbbcdbbcbbcbbcd'
        actual = Decompression.second_attempt('a2[3[2[b]c]d]')
        self.assertEqual(expects, actual)

    def test_edge_case_empty_compress(self):
        with self.assertRaises(Exception) as test:
            Decompression.second_attempt('a[]b')

    def test_edge_case_zero_multiplier(self):
        expects = ''
        actual = Decompression.second_attempt('0[abc]')
        self.assertEqual(expects, actual)


if __name__ == '__main__':
    unittest.main()

"""
Queston: https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=840934449713537
Pair Sums
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are
considered different if one pair includes at least one array index which the other doesn't,
even if they include the same values.

Signature
int numberOfWays(int[] arr, int k)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000,000,000].
k is in the range [1, 1,000,000,000].
Output
Return the number of different pairs of elements which sum to k.
Example 1
n = 5
k = 6
arr = [1, 2, 3, 4, 3]
output = 2
The valid pairs are 2+4 and 3+3.
Example 2
n = 5
k = 6
arr = [1, 5, 3, 3, 3]
output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements,
 and 4th and 5th elements).
"""


def numberOfWays(arr, k):
    """
    Best solution Space/Time wise.
    Form a dict based on the frequency of each of the values that appears, and store the index in which it occurred.
    This produces a dict with the keys being the number, and the value being the list of locations in which it occurs
    TC: O(N)
    SC: O(2N) -> O(N)
        O(2N) for the worst case of all values being unique in the list. i.e. arr = [0,1,2] => {0: {0}, 1: {1}, 2: {2}}
    """
    count = 0
    num_indices = dict()
    for idx, num in enumerate(arr):
        num_indices.setdefault(num, set()).add(idx)

    # Iterate over the array once more, and find all of the compliments that would be needed to generate the solution.
    # For each of the compliments we add the value in.
    for idx, num in enumerate(arr):
        comp = k - num
        if comp in num_indices:
            add_in = len(num_indices[comp])
            if idx in num_indices[comp]:
                # Decrease the add in value by 1 in this case because K / 2 == num. Remove that one instance.
                add_in -= 1
            count += add_in

    # Dividing the count value by 2 as theres a symbiotic relationship in the data.
    # if m = k - n, then n = k - m and that would be counted twice.
    return int(count / 2)


def numberOfWaysTwo(arr, k):
    """
    Safe Solution with the optimization to iterate over the arr twice and separation of the generation of the
        num_indices into its own field. Run complexity remains the same.
    For this implementation using a set to collect the indices of the pairs and counting them at injection time.
    Because of this not being a sorted list  we have to iterate over the captured values each time.
    Moving the Inner for loop into a separate call would remove redundant calls as the array is collected at that point.
    TC: O(N^2)
    SC: O(2N) -> O(N)
    """
    pairs = set()
    num_indices = dict()
    # Pre-generating the num_indices and separating the pairs calculation in full.
    for idx, num in enumerate(arr):
        num_indices.setdefault(num, set()).add(idx)

    for idx, num in enumerate(arr):
        comp = k - num
        if comp in num_indices:
            for j_idx in num_indices[comp]:
                pairs.add((min(idx, j_idx), max(idx, j_idx)))
        # Comment this out to iterate over the main array once, and the sub arrays multiple times
        # num_indices.setdefault(num, set()).add(idx)
    return len(pairs)


def numberOfWaysThree(arr, k):
    """
    Worst Solution: Solved in this way to instate the Time Complexity trade off and the possible O(1) space complexity.
    using a two pointer solution to resolve this problem. Need to sort the input for this.
    with the help of the TimSort algo, else heapsort could be used to guarantee in place sorting but would require using
    a min and max heap to iterate over the data and much more complicated logic.

    The internal while loop would be used to iterate over multiple matches as stated in the TC explanation.
    TC: O(N * (N * M)) + O(N Log(N) -> O(N^2 * M) where M is the size of the sub slice at the Nth window
        O(N * (N * M)): Worst possible time complexity as the inner loop could be visiting every element in the array.
            Possible if inputs are arr=[3,3,3,3], k= 6.
            Producing pairs [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
            Could then see that for every slice we could potentially have to iterate over every single subarray in the
            window presented.
            The algo could be trivialized to O(N^2) if the window is guaranteed to be negligible else O(N^3)
                while M approaches N.
        O(N Log(N)): Average case for the TimSort Algo
    SC: O(N)
        Extra space required in the worst case of the TimSort algo used by Python.
    """
    arr.sort()
    left = 0
    right = len(arr) - 1
    count = 0
    while left < right:
        l_val = arr[left]
        r_val = arr[right]
        if l_val + r_val == k:
            # Found a suitor, see if any other elements in this range can be used to determine it.
            count += 1
            t_r = right - 1
            while left < t_r and l_val + arr[t_r] == k:
                # need to ingest all of the values that match as each pair within a substring is valid.
                # This takes into account repeats. i.e. [1, 5, 3, 3, 3, 3] indices would be
                count += 1
                t_r -= 1
            # If a match is met only one of the indices needs to be changed and selecting the right arbitrarily.
            left += 1
        elif l_val + r_val > k:
            # Need to move down from the right hand side as it's adding too much or we've met a match.
            right -= 1
        elif l_val + r_val < k:
            # Increase the left pointer as we're shy of the wanted end value.
            left += 1
    return count


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    k_1 = 6
    arr_1 = [1, 2, 3, 4, 3]
    expected_1 = 2
    output_1 = numberOfWays(arr_1, k_1)
    check(expected_1, output_1)

    k_2 = 6
    arr_2 = [1, 5, 3, 3, 3, 3]
    expected_2 = 7
    output_2 = numberOfWays(arr_2, k_2)
    check(expected_2, output_2)

    # Add your own test cases here

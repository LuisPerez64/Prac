"""
Given a string shuffle the string so that no concurrent characters are the same.
e.g. 'aaabc' -> 'abaca'
"""
from collections import defaultdict
from heapq import heappush, heappop


def shuffle_string(inp_str: str) -> str:
    """
    Use a frequency dict to handle the number of occurrences of the numbers met.
    After their frequencies have been calculated place them in a heap with the input format (-occurrence, char)
        The -occurrence is used to transform the min-heap into a pseudo max-heap.
    While there are still elements in the heap try to place an instance of the character with the highest frequency
        onto the output. If we see that the item is the same as the last item on the array stack then hold the item
        and place the next largest onto the result.
        The heap will either be exhausted if it's valid, or left with at most 1 char that matches the last char in the
        result array.
    """
    results = []
    hp = []
    freq = defaultdict(int)

    def add_ans():
        """
        Add an element into the output. Decreasing (because of maxheap) the frequency count for it.
        If the element has reached the point where it's go no occurrences left then do not add it back to the heap.
        """
        if not hp:
            return
        tmp = heappop(hp)
        results.append(tmp[1])
        if tmp[0] + 1 < 0:
            # Clear out any items that are exhausted from the heap. Don't push it back if none left.
            heappush(hp, (tmp[0] + 1, tmp[1]))

    for ch in inp_str:
        freq[ch] += 1

    for ch in list(freq.keys()):
        # Save some space and keep the total added space complexity at O(N) instead of O(2N)
        count = freq.pop(ch)
        heappush(hp, (-count, ch))
    del freq

    if hp and hp[0][0] * -1 > len(inp_str) // 2:
        # Invalid string that could not be shuffled e.g. 'aaab'
        # Determine this by checking if any element in the dict has a frequency > half the length of the input string.
        raise Exception(f"String {inp_str} cannot be shuffled.")

    add_ans()
    while hp:
        if hp[0][1] != results[-1]:
            add_ans()
        else:
            # The value at the top of the heap matches the last in the result stack.
            # Hold on to it, and do the normal add_ans operation.
            hold = heappop(hp)
            add_ans()
            # Add the element back into the heap to be handled, most likely on the next iteration.
            # We could do the add_ans here but no deep benefit gained.
            heappush(hp, hold)
        print(''.join(results), hp)

    return ''.join(results)


print(shuffle_string('aaaabbbbb'))

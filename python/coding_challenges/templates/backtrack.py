"""
Template for the backtrack problem approach. Useful in traversal algorithms.
Exhaustive algorithm so its time complexity tends to be O(num_start_points * num_paths^final_wanted_item)
i.e. if doing a word search moving up,down,left,right from any location (excluding the origin if revisiting not allowed)
    at every grid point num_paths=4, num_start_points=size_of_grid
    worst case scenario = O(size_of_grid * 4^len(word_being_sought)
Use Cases:
    Traversal problems that allow movement along more than one axis.

Template:
    While Exit condition not satisfied:
        Check an exit condition i.e. an empty stack.
        Check for a condition at the current location to determine continuing on the current path.
            if satisfied
                mark the current cell as the new continuation point to not visit it on the next iteration.
                call the function again from that point onwards with the next state expected and the possible paths the
                function could move towards. i.e. left,right,up,down,diagonally
            else
                reverse the marker as this is not going to lead to the wanted outcome.
                return that this was a failed path.
    Check if another start point could yield the wanted result and re-run the backtrack function.
"""

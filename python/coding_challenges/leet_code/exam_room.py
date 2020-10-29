from typing import List


class ExamRoom:

    def __init__(self, N: int):
        self.capacity = N - 1
        self.seats = [0] * N

    def seat(self) -> int:
        # The distance between the two points that could be best achieved is through
        # Finding and maintaing the total capacity and the intervals between that
        # Try to sit the student in the first or last seat. The two base cases.
        if sum(self.seats) == 0:
            seated = self.sit(0)
        elif sum(self.seats) == 1 and self.seats[0] == 1:
            seated = self.sit(len(self.seats) - 1)
        else:
            # Find the Intervals of unseated students.
            gaps: List[list] = []
            last_filled = 0

            for idx in range(len(self.seats)):
                if not self.seats[idx] and gaps:
                    gaps[-1][1] = idx + 1
                else:
                    # Implant a new gap starting at this seat.
                    gaps.append([idx, idx])
            max_gap = gaps[0]
            for gap in gaps[1:]:

                # Implied that there's not going to be a capacity problem so there will always be at least one seat.
                if (max_gap[1] - max_gap[0]) // 2 < (gap[1] - gap[0]) // 2:
                    max_gap = gap
            seated = self.sit(max_gap[0] + (max_gap[1] - max_gap[0]) // 2)
            # print(gaps, self.seats)
        return seated

    def sit(self, chair: int) -> int:
        if self.seats[chair] == 0:
            self.seats[chair] = 1
            return chair
        return -1

    def leave(self, p: int):
        self.seats[p] = 0


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)

"""
Test Cases:

["ExamRoom","seat","seat","seat","seat","leave","seat"]
[[10],[],[],[],[],[4],[]]
"""

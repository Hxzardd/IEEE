from sortedcontainers import SortedList

class IntervalMerger:
    """
    A data structure to maintain a set of non-overlapping intervals and efficiently merge them when new intervals are added.
    Supports:
      - addInterval(start, end): O(log n) insertion and merging using sorted lists.
      - getIntervals(): O(n) retrieval of all merged intervals.
    """

    def __init__(self):
        # Using SortedList to maintain ordered intervals efficiently
        self.intervals = SortedList(key=lambda x: x[0]) # Ensure sorting by start values automatically

    def addInterval(self, start, end):
        pos = self.intervals.bisect_left((start, end))  # Find insert position
        
        new_start, new_end = start, end
        
        # Merge with left interval if overlapping
        left_pos = pos - 1
        if left_pos >= 0:
            left_s, left_e = self.intervals[left_pos]
            if left_e >= new_start:  # Overlap detected
                new_start = min(new_start, left_s)
                new_end = max(new_end, left_e)
                self.intervals.pop(left_pos)
                pos -= 1

        # Merge with right intervals while they overlap
        while pos < len(self.intervals):
            cur_s, cur_e = self.intervals[pos]
            if cur_s <= new_end:
                new_start = min(new_start, cur_s)
                new_end = max(new_end, cur_e)
                self.intervals.pop(pos)  # Remove merged interval
            else:
                break  # stop if no more overlap

        # Insert the new merged interval
        self.intervals.add((new_start, new_end))

    def getIntervals(self):
        # Return the current merged, non overlapping interval
        return list(self.intervals)


# --------------------------------------------------------------
# TESTING
# --------------------------------------------------------------

# 
# if __name__ == "__main__":
#     im = IntervalMerger()

#     im.addInterval(1, 5)
#     im.addInterval(6, 8)
#     print(im.getIntervals())  # Output: [(1, 5), (6, 8)]

#     im.addInterval(4, 7)
#     print(im.getIntervals())  # Output: [(1, 8)]

#     # Further testing
#     im.addInterval(10, 12)
#     im.addInterval(9, 9)
#     print(im.getIntervals())  # Output: [(1, 8), (9, 9), (10, 12)]

#     im.addInterval(8, 11)
#     print(im.getIntervals())  # Output: [(1, 12)]

from sortedcontainers import SortedList

class IntervalMerger:
    """
    A data structure to maintain a set of non-overlapping intervals and efficiently merge them when new intervals are added.
    Supports:
      - addInterval(start, end): O(log n) insertion and merging using sorted lists.
      - getIntervals(): O(n) retrieval of all merged intervals.
    """
    def __init__(self):
        self.intervals = SortedList(key=lambda x: x[0])  # sorted list maintains ordered intervals already based on the start value

    def addInterval(self, start, end):
        insert_pos = self.intervals.bisect_left((start, end))  # finds position where the interval should be inserted
        new_start, new_end = start, end  # initialize the new interval bounds that are to be found

        # Check if the left interval overlaps and merge
        if (insert_pos > 0) and (self.intervals[insert_pos - 1][1] >= start):
            new_start = self.intervals[insert_pos - 1][0]  # taking the left interval's starting position
            new_end = max(self.intervals[insert_pos - 1][1], end)  # checking and extending the ending position if required
            self.intervals.pop(insert_pos - 1)  # Removing the merged left interval
            insert_pos -= 1  # Adjusting the  inserting  position

        # Merge with overlapping right intervals
        while (insert_pos < len(self.intervals)) and (self.intervals[insert_pos][0] <= new_end):
            new_end = max(new_end, self.intervals[insert_pos][1])  # Extend the merged interval if overlapping
            self.intervals.pop(insert_pos)  # Removeing the merged right interval

        # Insert the final merged interval
        self.intervals.add((new_start, new_end))

    def getIntervals(self):
        return list(self.intervals)


# -------------------
# TEST CASES
# -------------------
# if __name__ == "__main__":
#     im = IntervalMerger()

#     im.addInterval(1, 5)
#     im.addInterval(6, 8)
#     print(im.getIntervals())  # Output: [(1, 5), (6, 8)]

#     im.addInterval(4, 7)
#     print(im.getIntervals())  # Output: [(1, 8)]

#     im.addInterval(10, 12)
#     im.addInterval(9, 9)
#     print(im.getIntervals())  # Output: [(1, 8), (9, 9), (10, 12)]

#     im.addInterval(8, 11)
#     print(im.getIntervals())  # Output: [(1, 12)]

from typing import List


# merge intervals basic question
# sort by start time, merge next
# key: two pointers first point to current, next always point to the one can get merged.If next cant get merged
# repoint first to next
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    i = 0
    out = []
    while i < len(intervals):
        j = i + 1
        cur = intervals[i]
        while j < len(intervals):
            nxt = intervals[j]
            if nxt[0] <= cur[1]:
                cur[1] = max(cur[1], nxt[1])
                j += 1
            else:
                break
        i = j
        out.append(cur)
    return out


def main():
    intervals = [[1, 4], [2, 3]]
    print(merge(intervals=intervals))


if __name__ == '__main__':
    main()

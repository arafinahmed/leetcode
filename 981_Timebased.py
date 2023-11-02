import collections
import bisect

class TimeMap:

    def __init__(self):
        self.timemaps = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemaps[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_right(self.timemaps[key], timestamp)
        return self.values[key][i-1] if i else ''
    
import sys
from copy import copy

class eRange:
    def __init__(self, start, end = None, span = None) -> None:
        self.start = start
        if end:
            self.end = end
        elif span:
            self.end = start + (span - 1)
        else:
            self.end = start

    def __repr__(self) -> str:
        return f'({self.start}, {self.end})'

    def does_overlap(self, c_range):
        if c_range.start <= self.start <= c_range.end:
            return True
        elif self.start <= c_range.start <= self.end:
            return True
        elif c_range.start <= self.end <= c_range.end:
            return True
        elif self.start <= c_range.end <= self.end:
            return True
        return False
    
    def combine_with(self, c_range):
        if self.does_overlap(c_range):
            return eRange(start = min(self.start, c_range.start), end = max(self.end, c_range.end))
        return None

    def intersect_with(self, c_range):
        if self.does_overlap(c_range):
            return eRange(start = max(self.start, c_range.start), end = min(self.end, c_range.end))
        else:
            return None

    def subtract(self, c_range):
        # Self contained by c_range
        if c_range.start <= self.start and self.end <= c_range.end:
            return None
        # c_range contained by self
        elif self.start < c_range.start and self.end > c_range.end:
            return [eRange(start = self.start, end = c_range.start - 1), eRange(start = c_range.end + 1, end = self.end)]
        # Partial overlap between self and c_range (right overhang)
        elif c_range.start <= self.start <= c_range.end and self.end > c_range.end:
            return [eRange(start = c_range.end + 1, end = self.end)]
        # Partial overlap between self and c_range (left overhang)
        elif self.start < c_range.start and c_range.start <= self.end <= c_range.end:
            return [eRange(start = self.start, end = c_range.start - 1)]
        # No overlap between self and c_range
        else:
            return [self]

    def rebase(self, amount):
        return eRange(start = (self.start + amount), end = (self.end + amount))


class eRangeCollection:
    def __init__(self):
        self.ranges = []

    def __repr__(self) -> str:
        r = '['
        for e_range in self.ranges:
            r += f'({e_range.start}, {e_range.end})'
        r += ']'
        return r
    
    def copy(self):
        copy = eRangeCollection()
        copy.ranges = self.ranges[:]
        return copy

    def add_range(self, new_range):
        if len(self.ranges) == 0:
            self.ranges.append(new_range)
        else:
            range_idx = 0
            while range_idx < len(self.ranges) and new_range.start > self.ranges[range_idx].end:
                range_idx += 1
            if range_idx == len(self.ranges) or new_range.end < self.ranges[range_idx].start:
                self.ranges.insert(range_idx, new_range)
            else:
                combined_range = new_range
                combined_indices = []
                while range_idx <= len(self.ranges) - 1 and new_range.does_overlap(self.ranges[range_idx]):
                    combined_range = combined_range.combine_with(self.ranges[range_idx])
                    combined_indices.append(range_idx)
                    range_idx += 1
                self.ranges = self.ranges[:combined_indices[0]] + [combined_range] + self.ranges[combined_indices[-1] + 1:]
    
    def subtract_range(self, c_range):
        range_idx = 0
        while range_idx < len(self.ranges) and c_range.start > self.ranges[range_idx].end:
            range_idx += 1
        if range_idx == len(self.ranges) or c_range.end < self.ranges[range_idx].start:
            pass
        else:
            offset = 0
            while range_idx - offset <= len(self.ranges) - 1 and c_range.does_overlap(self.ranges[range_idx - offset]):
                if (diff := self.ranges[range_idx - offset].subtract(c_range)):
                    self.ranges = self.ranges[:range_idx - offset] + diff + self.ranges[range_idx - offset + 1:]
                else:
                    self.ranges.pop(range_idx - offset)
                    offset += 1
                range_idx += 1
        return self


# a = eRangeCollection()
# a.add_range(eRange(start = 0, end = 10))
# a.add_range(eRange(start = 20, end = 30))
# print(a)
# print(a.subtract_range(eRange(start = 0, end = 4)))
# print(a.subtract_range(eRange(start = 20, end = 30)))

# a = eRangeCollection()
# a.add_range(eRange(start = 46, end = 56))
# a.add_range(eRange(start = 74, end = 87))
# a.add_range(eRange(start = 90, end = 98))
# print(a)
# print(a.subtract_range(eRange(start = 56, end = 92)))
# print(a.subtract_range(eRange(start = 93, end = 96)))

with open('./input.txt') as data:
    lines = data.readlines()
    seeds_to_plant = []
    seed_values = list(map(lambda x: int(x), lines.pop(0).strip().split(': ')[1].split(' ')))
    next_ranges = eRangeCollection()
    for value_index in range(1, len(seed_values), 2):
        next_ranges.add_range(eRange(start=seed_values[value_index - 1], span=seed_values[value_index]))
    current_ranges = eRangeCollection()
    smallest_location = sys.maxsize
    for line in lines:
        line = line.strip()
        if line.endswith(':'):
            for r in current_ranges.ranges:
                next_ranges.add_range(r)
            current_ranges = next_ranges.copy()
            next_ranges = eRangeCollection()
        elif len(line) == 0:
            pass
        elif line[0].isdigit():
            map_values = list(map(lambda x: int(x), line.split(' ')))
            dest_offset = map_values[0] - map_values[1]
            source_range = eRange(start = map_values[1], span = map_values[2])
            for e_range in current_ranges.ranges.copy():
                if (overlap := e_range.intersect_with(source_range)):
                    next_ranges.add_range(overlap.rebase(dest_offset))
                    current_ranges.subtract_range(overlap)
    for r in current_ranges.ranges:
        next_ranges.add_range(r)
    smallest_location = sys.maxsize
    for r in next_ranges.ranges:
        if r.start < smallest_location:
            smallest_location = r.start
    print(smallest_location)



        

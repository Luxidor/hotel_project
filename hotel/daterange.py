# Holds a start and end date to represent a range of dates
class DateRange:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # Returns true if passed range overlaps any date in our range
    def overlaps(self, other_range):
        # this checks if "self" overlaps with "other_range" by checking whether 
        # the start date of either is contained inside of the other's date range.
        overlap_1 = self.start <= other_range.start and other_range.start <= self.end 
        overlap_2 = other_range.start <= self.start and self.start <= other_range.end
        return overlap_1 or overlap_2

    def to_display(self):
        return self.start + ' through ' + self.end
class loop_colored_partition(object):
    def __init__(self, blocks, num_colors):
        # pairs, where the first item is the length and the second item is the starting value
        self.blocks = blocks
        self.num_colors = num_colors

    def partitions_from_profile(profile):
        return

    def __str__(self):
        string = ""
        for row in self.blocks:
            for i in xrange(row[0]):
                string += str((row[1] + i) % self.num_colors)
            string += "\n"
        return string


def get_row_from_weight(weight, num_colors):
    return [weight / num_colors + 1, weight % num_colors]


def profile_of_row(length, num_colors, start):
    return [(length / num_colors + 1
             if (i - start) % num_colors < length % num_colors
             else length / num_colors) for i in xrange(num_colors)]


def dominates(l1, l2):
    return all(l1[i] >= l2[i] for i in xrange(len(l1)))


def partitions_from_profile_max_size(profile, max_weight, unique_parts = False):
    partitions = []
    if all(p == 0 for p in profile):
        partitions.append([])
        return partitions
    num_colors = len(profile)
    for weight in reversed(xrange(max_weight if unique_parts else max_weight + 1)):
        row = get_row_from_weight(weight, num_colors)
        this_row_profile = profile_of_row(row[0], num_colors, row[1])
        if dominates(profile, this_row_profile):
            remaining = [profile[i] - this_row_profile[i]
                         for i in xrange(len(profile))]
            for partition in partitions_from_profile_max_size(remaining, weight):
                partition.append(row)
                partitions.append(partition)
    return partitions


def partitions_from_profile(profile):
    lst = []
    for p in partitions_from_profile_max_size(profile, len(profile) * sum(profile)):
        lst.append(loop_colored_partition(reversed(p), len(profile)))
    return lst
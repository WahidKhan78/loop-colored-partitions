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


def partitions_from_profile_max_size(profile, max_weight, kwargs):
    partitions = []
    if all(p == 0 for p in profile):
        partitions.append([])
        return partitions
    num_colors = len(profile)
    next_max = max_weight + 1
    if kwargs.get('unique_parts', False):
        next_max = max_weight
    elif kwargs.get('unique_sizes', False):
        next_max = (max_weight / num_colors) * num_colors
    for weight in reversed(xrange(next_max)):
        if 'length_list' in kwargs and (weight/num_colors)+1 not in kwargs['length_list']:
            continue
        row = get_row_from_weight(weight, num_colors)
        this_row_profile = profile_of_row(row[0], num_colors, row[1])
        if dominates(profile, this_row_profile):
            remaining = [profile[i] - this_row_profile[i]
                         for i in xrange(len(profile))]
            for partition in partitions_from_profile_max_size(remaining, weight, kwargs):
                partition.append(row)
                partitions.append(partition)
    return partitions


# Options are thus:
# unique_parts = True generates only partitions with distinct parts.
# 12/21/2/1 is generated under this condition.
# unique_sizes = True generates only partitions whose rows are distinct sizes.
# 12/21/2/1 is not generated under this condition.
# max_part = k generates partitions with largest part at most length k.
# length_list = a[n] generates partitions all of whose lengths are in the list a.
def partitions_from_profile(profile, **kwargs):
    lst = []
    for p in partitions_from_profile_max_size(
            profile,
            len(profile) * kwargs.get('max_part', sum(profile)),
            kwargs):
        lst.append(loop_colored_partition(reversed(p), len(profile)))
    return lst


for p in partitions_from_profile([5, 5, 5], length_list = [1,3,5,7,9,11,13,15,17]):
    print p

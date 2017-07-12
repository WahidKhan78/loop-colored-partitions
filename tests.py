from Profiles import *
from LoopColoredPartition import *
profs = [prof for i in xrange(15) for prof in get_bracelets(2, i)]

# for prof in profs:
#     print [prof,
#            len(partitions_from_profile(prof)),
#            len(partitions_from_profile(prof, unique_parts = True)),
#            len(partitions_from_profile(prof, unique_sizes = True)),
#            len(partitions_from_profile(prof, length_list = [1,3,5,7,9,11])),
#            len(partitions_from_profile(prof, length_list = [1,3,5,7,9,11], unique_parts = True)),
#            len(partitions_from_profile(prof, length_list = [2,4,6,8,10,12])),
#            len(partitions_from_profile(prof, num_parts_list = [1,3,5,7,9,11])),
#            len(partitions_from_profile(prof, length_list = [1,4,7,10,13])),
#            len(partitions_from_profile(prof, length_list = [1,4,7,10,13], unique_parts = True))]

k=6
for prof in profs:
    a = prof[0]
    b = prof[1]
    print (
        len(partitions_with_fixed_parts([a, b], k))
        - len(partitions_with_fixed_parts([a - k, b - k], k))
        - len(partitions_with_fixed_parts([a - 1, b], k - 1))
        - len(partitions_with_fixed_parts([a, b - 1], k - 1))
        - 2 * len(partitions_with_fixed_parts([a - 1, b - 1], k - 1))
        + len(partitions_with_fixed_parts([a - 1, b - 1], k - 2))
        + 2 * len(partitions_with_fixed_parts([a - 2, b - 1], k - 2))
        + 2 * len(partitions_with_fixed_parts([a - 1, b - 2], k - 2))
        + len(partitions_with_fixed_parts([a - 2, b - 2], k - 2))
        - len(partitions_with_fixed_parts([a - 3, b - 2], k - 3))
        - len(partitions_with_fixed_parts([a - 2, b - 3], k - 3))
        - 2 * len(partitions_with_fixed_parts([a - 2, b - 2], k - 3))
        + len(partitions_with_fixed_parts([a - 3, b - 3], k - 4)))
